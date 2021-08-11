from lib.core.config import *
from lib.core.logger import log
import pymysql


class MyMysql(object):
    def __init__(self):
        self.config = Configure()
        self.config = self.config.read(ConfType.MYSQL)
        self.db = pymysql.connect(**self.config)
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)

    @log(7)
    def execute_sql(self, sql):
        row = self.cursor.execute(sql)
        self.db.commit()
        return row

    @log(3)
    def query_data(self, sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def __del__(self):
        self.db.close()


if __name__ == '__main__':
    MyMysql().query_data("SELECT *FROM zt_bug;")
