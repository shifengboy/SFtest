import sys

from lib.core.ext import Configure
from lib.core.path import LOGPATH
from lib.core.tool import Tool
import subprocess
import threading
from lib.core.logger import logger
import os
from appium import webdriver
import queue
import time


# 多线程数据隔离
local_driver = threading.local()

# driver的对列
driver_q = queue.Queue()

# devicename的对列,用于区分报告
device_q = queue.Queue()


class Controller(object):
    def __init__(self):
        self.yml = Configure().app_data
        self.devices = self.yml.get('devices')
        self.tester = self.yml.get('tester')
        self.device_type = self.yml.get('device_type')
        self.threads_server = []
        self.threads_driver = []
        self.ports = []
        self.tool = Tool()

    @staticmethod
    def kill_server():
        """
        夜游神模拟器如果重启 adb服务后将不被 adb devices所查找
        :return:
        """
        if sys.platform == 'win':
            logger.debug('执行[KILL SERVER]操作:%s' % subprocess.getoutput("taskkill /F /IM node.exe /t"))
        else:
            logger.debug('执行[KILL SERVER]操作:%s' % subprocess.getoutput("pkill -9 node"))
        logger.debug('重启ADB服务！%s' % subprocess.getoutput("adb kill-server"))

    # 存在偶现问题 增加ip 加端口判断 以确保服务准确启动
    # @property
    def test_server(self):
        while True:
            for port in self.ports:
                # 通过查看是否有返回值来确定是否启动
                if sys.platform == 'win':
                    test_out_put = subprocess.getoutput("netstat -ano | findstr %s" % port)
                else:
                    test_out_put = subprocess.getoutput("netstat -an | grep %s" % port)
                # 如果有 则从list中删除整个端口 直到这个list为空时 代表启动成功 跳出循环
                if test_out_put:
                    logger.debug('检验服务启动：%s' % test_out_put)
                    self.ports.remove(port)
                else:
                    logger.debug('端口 [%s] 服务启动失败5秒钟后尝试' % port)
            if not self.ports:
                break
            time.sleep(5)
        logger.debug('全部服务启动成功！')
        return True

    @staticmethod
    def server_command(**kwargs):
        commond = 'appium -a {ip} -p {port} -U {deviceName} -g {log}'.format(ip=kwargs.get('ip'),
                                                                             port=kwargs.get('port'),
                                                                             deviceName=kwargs.get(
                                                                                 'deviceName'),
                                                                             log=kwargs.get('log_path'))

        logger.info('启动服务: {}'.format(commond))
        res = subprocess.Popen(commond, stdout=open(kwargs.get('log_path'), 'a+'), stderr=subprocess.PIPE, shell=True)

    def server(self):
        """
            netstat -ano | findstr xxxx
        :return:
        """
        self.kill_server()
        # 循环每一个手机配置
        for device in self.devices.get(self.device_type):
            # print(device)
            # 处理异常手机名称无法生成log的问题
            flag = self.tool.exce_device_name(device.get('deviceName'))
            if flag == 0:
                # 真机增加以手机名 命名的log地址
                device.update({'log_path': os.path.join(LOGPATH, device.get('deviceName') + '.log')})
            else:
                # 夜游神虚拟机更改log名称问题
                device.update({'log_path': os.path.join(LOGPATH, flag + '.log')})

            # 提取校验服务启动成功的端口
            self.ports.append(device.get('port'))

            logger.debug('配置参数：%s' % device)
            # 启动多线程开启服务
            t = threading.Thread(target=self.server_command, kwargs=device)
            self.threads_server.append(t)
            t.start()
        for t in self.threads_server:
            t.join()
        return None

    def driver_commend(self, **kwargs):
        local_driver.desired_caps = {'platformName': '', 'platformVersion': '', 'deviceName': '',
                                     "unicodeKeyboard": "True",
                                     "resetKeyboard": "True", 'udid': '', 'noReset': 'True'}
        # 更新配置文件
        local_driver.desired_caps.update(kwargs)
        url = 'http://{ip}:{port}/wd/hub'.format(port=local_driver.desired_caps.get('port'),
                                                 ip=local_driver.desired_caps.get('ip'))
        driver = webdriver.Remote(url, local_driver.desired_caps)

        # 生成的driver通过对列传递
        driver_q.put(driver)

        # # 修改夜游神创建目录问题
        # name = self.tool.exce_device_name(local_driver.desired_caps.get('deviceName'))
        # if name:
        #     app = APPPICTUREPATH.format(name)
        # else:
        #     app = APPPICTUREPATH.format(local_driver.desired_caps.get('deviceName'))
        # # 清除上一次运行是失败的图片
        # # 如果存在则清除目录下的所有内容
        # if os.path.exists(app):
        #     # 调用写好的clear方法
        #     self.tool.app_clear(app)
        # else:
        #     # 如果不存在path 则递归创建目录
        #     os.makedirs(app)

        # 将手机名传入对列 后续处理报告使用
        device_q.put(local_driver.desired_caps.get('deviceName'))

    def driver(self):
        for device in self.devices.get(self.device_type):
            # 将测试的app 增加到手机配置文件中
            device.update(self.tester)
            t = threading.Thread(target=self.driver_commend, kwargs=device)
            self.threads_driver.append(t)
            t.start()
        for driver in self.threads_driver:
            driver.join()
        # 返回队列 确保有多少个driver启动
        return driver_q


if __name__ == '__main__':
    s = Controller()
    # print(s.devices)
    s.server()
    s.test_server()
    s.driver()
    # s.kill_server()
    # import sys
    # print(sys.platform)