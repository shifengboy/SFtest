import json
import logging
import yaml

from lib.core.path import WEBPATH, APPPATH


BASECONF = {}


class ConfType(object):
    MYSQL = 'mysql'
    BROWSER = 'browser'
    REDIS = 'redis'
    MAIL = 'mail'
    Level = 'level'
    LOG = 'log'
    URL = 'url'


class Configure(object):

    # 配置信息
    @classmethod
    def make(cls):
        fw = open(WEBPATH, 'w')

        # CASE 级别
        BASECONF[ConfType.Level] = 'all'

        # 测试环境
        BASECONF[ConfType.URL] = 'http://pre.p4p.pangu.163.com'

        # 浏览器 配置
        BASECONF[ConfType.BROWSER] = 'chrome'

        # LOG打印级别设置
        BASECONF[ConfType.LOG] = {}
        BASECONF[ConfType.LOG]['console'] = logging.DEBUG
        BASECONF[ConfType.LOG]['main'] = logging.DEBUG

        # MYSQL 配置
        BASECONF[ConfType.MYSQL] = {}
        BASECONF[ConfType.MYSQL]['host'] = '116.196.122.78'
        BASECONF[ConfType.MYSQL]['port'] = 3306
        BASECONF[ConfType.MYSQL]['user'] = 'zbox'
        BASECONF[ConfType.MYSQL]['passwd'] = 'Houyafan123'
        BASECONF[ConfType.MYSQL]['db'] = 'zbox'
        BASECONF[ConfType.MYSQL]['charset'] = 'utf8'

        # REDIS 配置
        BASECONF[ConfType.REDIS] = {}
        BASECONF[ConfType.REDIS]['host'] = '10.165.124.28'
        BASECONF[ConfType.REDIS]['port'] = 8801
        BASECONF[ConfType.REDIS]['password'] = 123456
        BASECONF[ConfType.REDIS]['db'] = 0

        # MAIL 配置
        BASECONF[ConfType.MAIL] = {}
        BASECONF[ConfType.MAIL]['sender'] = 'uitestp4p@163.com'
        BASECONF[ConfType.MAIL]['passwd'] = 'p4pp4pp4p'
        BASECONF[ConfType.MAIL]['smtpserver'] = 'smtp.163.com'
        BASECONF[ConfType.MAIL]['username'] = 'uitestp4p@163.com'
        BASECONF[ConfType.MAIL]['receiverList'] = [
            'bjhouyafan@corp.netease.com',
        ]
        fw.write(json.dumps(BASECONF))
        fw.flush()
        fw.close()
        return BASECONF

    # 读取配置
    def read(self, conf_type):
        fr = open(WEBPATH, 'r')
        data = json.load(fr)
        if conf_type == ConfType.BROWSER:
            return data.get(ConfType.BROWSER)
        elif conf_type == ConfType.MYSQL:
            return data.get(ConfType.MYSQL)
        elif conf_type == ConfType.REDIS:
            return data.get(ConfType.REDIS)
        elif conf_type == ConfType.MAIL:
            return data.get(ConfType.MAIL)
        elif conf_type == ConfType.Level:
            return data.get(ConfType.Level)
        elif conf_type == ConfType.LOG:
            return data.get(ConfType.LOG)
        elif conf_type == ConfType.URL:
            return data.get(ConfType.URL)
        fr.close()

    @property
    def app_data(self):
        with open(APPPATH, 'rb') as f:
            data = yaml.safe_load(f)
        return data


if __name__ == "__main__":
    print(Configure().app_data)
