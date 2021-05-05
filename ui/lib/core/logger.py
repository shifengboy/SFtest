from logging import handlers
import requests
from ui.lib.core.ext.config import *
from ui.lib.core.path import WEBLOGPATH
from ui.lib.core.tool import LoadsDumps

fm = LoadsDumps()


class Logger(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Logger.__instance:
            Logger.__instance = object.__new__(cls, *args)
        return Logger.__instance

    def __init__(self):
        self.config = Configure()
        self.conf = self.config.read(ConfType.LOG)
        # 格式化log的模板
        self.formater = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] [%(filename)s:%(funcName)s:%(lineno)d] %(message)s')

        # 声明一个log对象
        self.logger = logging.getLogger('log')
        # 设置全局log级别
        self.logger.setLevel(self.conf.get('main'))

        # 文件log
        self.filelogger = handlers.RotatingFileHandler(WEBLOGPATH,
                                                       maxBytes=5242880,
                                                       backupCount=3
                                                       )
        # 屏幕log
        self.console = logging.StreamHandler()
        # 对屏幕设置级别
        self.console.setLevel(self.conf.get('console'))

        self.filelogger.setFormatter(self.formater)
        self.console.setFormatter(self.formater)
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)

    def log(self):
        return self.logger


logger = Logger().log()


def log(t):
    if t == 1:
        def http_log(f):
            def r(*args, **kwargs):
                logger.info('URL:{}'.format(kwargs['url']))
                logger.info('DATA:\n{}'.format(fm.dumps(kwargs['data'])))
                data = f(*args, **kwargs)
                logger.info('response : \n{}'.format(fm.loads_and_dumps(data.text)))
                return data
            return r

        return http_log
    elif t == 5:
        def http_log(f):
            def r(*args, **kwargs):
                logger.debug('URL:{}'.format(args[1]))
                logger.debug('DATA:\n{}'.format(fm.dumps(kwargs)))
                data = f(*args, **kwargs)
                return data

            return r

        return http_log
    elif t == 2:
        def cookie_log(f):
            def r(*args, **kwargs):
                data = f(*args, **kwargs)
                logger.debug('SetCookieDict : \n{}'.format(fm.dumps(requests.utils.dict_from_cookiejar(data[1]))))
                return data[0]

            return r

        return cookie_log
    elif t == 3:
        def sql_log(f):
            def r(*args, **kwargs):
                logger.debug('SQL : {}'.format(args[1]))
                data = f(*args, **kwargs)
                datetime = __import__('datetime')
                for d in data:
                    for k, v in d.items():
                        if isinstance(v, datetime.datetime) or isinstance(v, datetime.date):
                            d[k] = str(d.get(k))
                    logger.debug('DataBase Data : \n{}'.format(fm.dumps(d)))
                return data

            return r

        return sql_log
    elif t == 4:
        def redis_log(f):
            def r(*args, **kwargs):
                code = f(*args, **kwargs)
                logger.info('验证码 : {}'.format(code))
                return code

            return r

        return redis_log
    elif t == 6:
        def case_log(f):
            def r(*args, **kwargs):
                logger.info('【{}】'.format(kwargs['doc']))
                data = f(*args, **kwargs)
                return data

            return r

        return case_log
    elif t == 7:
        def case_log(f):
            def r(*args, **kwargs):
                logger.debug('SQL : {}'.format(args[1]))
                data = f(*args, **kwargs)
                return data

            return r

        return case_log
