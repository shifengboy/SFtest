import json
import os
from lib.core.path import WEBPICTUREPATH, APPPICTUREPATH, APPERROR
import threading


class LoadsDumps(object):
    def loads_and_dumps(self, data):
        return self.dumps(json.loads(data))

    def dumps(self, data):
        if data:
            try:
                data = json.dumps(data, indent=4, ensure_ascii=False)
            except Exception as e:
                data = json.dumps(str(data), indent=4, ensure_ascii=False)
        return data

    def loads(self, data):
        return json.loads(data)


class Relation(object):
    @staticmethod
    def relation(t):
        if t == 'before':
            def befor(f):
                def r(*args, **kwargs):
                    befor_data = f(*args, **kwargs)
                    Relation.before_data = befor_data
                    return befor_data

                return r

            return befor
        elif t == 'after':
            def after(f):
                def r(*args, **kwargs):
                    kwargs.update({'before_data': Relation.before_data})
                    data = f(*args, **kwargs)
                    return data

                return r

            return after


class Tool(object):
    def __init__(self):
        self.filelist = os.listdir(WEBPICTUREPATH)

    # 处理手机名称异常的问题
    def exce_device_name(self, name):
        if name == '127.0.0.1:62001':
            return '127'
        return 0

    def error_picture(self):
        picture = []
        for item in self.filelist:
            if item.endswith('.jpg'):
                picture.append((item,))
        return picture

    def clear_picture(self):
        list(map(os.remove, map(lambda file: WEBPICTUREPATH + file, self.filelist)))

    def app_error_picture(self):
        # 处理夜游神设备名异常情况
        name = self.exce_device_name(threading.current_thread().getName())
        if name:
            app = APPPICTUREPATH.format(name)
        else:
            # 根据当前设备的线程名称进行目录的拼接
            app = APPPICTUREPATH.format(threading.current_thread().getName())
        app_list = os.listdir(app)
        app_picture = []
        for item in app_list:
            if item.endswith('.jpg'):
                app_picture.append((APPERROR.format(threading.current_thread().getName()) + item,))
        return app_picture

    @staticmethod
    def app_clear(app):
        app_list = os.listdir(app)
        list(map(os.remove, map(lambda file: app + file, app_list)))
