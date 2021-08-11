from lib.core.appController import Controller, device_q
from lib.core.logger import logger
from lib.core.ext import Result
from ui.appCase.test_thread_case import AppDemo
from lib import HTMLTestAppRunner
from lib.core.path import APPREPORT
import threading
import unittest
import queue

local_case = threading.local()
res_q = queue.Queue()


class App(object):
    def __init__(self):
        self.controller = Controller()
        self.threads = []

    @staticmethod
    def case():
        # 通过导入测试类来实现生成测试集
        suite = unittest.TestLoader().loadTestsFromTestCase(AppDemo)
        # 实例化结果对象
        # 生成一个空的结果集
        local_case.r = Result()

        # 运行case,并更新结果集，记录正确的case 失败的case
        res = suite.run(local_case.r)

        # 将结果通过测试手机名称分割
        logger.debug('当前线程的的名字：%s'%threading.current_thread().getName())
        res = {threading.current_thread().getName(): res}

        # 处理夜游神名称问题 直接从源头解决 在配置devicesname时如果为127.0.0.1:62001 则直接update名字
        for deviceName, result in res.items():
            html = HTMLTestAppRunner.HTMLTestRunner(stream=open(APPREPORT + '{}.html'.format(deviceName), "wb"),
                                                    verbosity=2,
                                                    title='测试')

            # 这个方法就是生成报告的主要函数
            html.generateReport('', result)

    def run(self):
        self.controller.server()
        # test_server 偶现 校验失败 需要特殊里返回直接过
        if self.controller.test_server:
            driver = self.controller.driver()
            logger.info('开始执行CASE！当前启动[%s]个DRIVER！' % driver.qsize())

            # 当前执行的case
            for case in range(driver.qsize()):
                # 根据driver启动多线程跑case,对每个线程通过手机名 命名
                t = threading.Thread(target=self.case, name=device_q.get())
                self.threads.append(t)
                t.start()
            for t in self.threads:
                t.join()


if __name__ == '__main__':
    App().run()

