import redis

from lib.core.config import Configure
from lib.core.logger import log


class MyRedis(object):
    def __init__(self):
        self.config = Configure()
        self.conf = self.config.read('redis')
        self.r = redis.Redis(**self.conf)

    @log(4)
    def get_code(self, code_cookie):
        code = self.r.get('p4p:dvCode:%s' % code_cookie).decode()
        return code
