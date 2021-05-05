import os

BASEPATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 报告地址
REPORTPATH = BASEPATH + os.path.sep + 'report'

# UI自动化报告地址
WEBREPORT = REPORTPATH + os.path.sep + 'web' + os.path.sep

# app自动化报告地址
APPREPORT = REPORTPATH + os.path.sep + 'app' + os.path.sep

# UI自动化报错图片路径
WEBPICTUREPATH = REPORTPATH + os.path.sep + 'web_picture' + os.path.sep

# APP错误图片地址
APPPICTUREPATH = REPORTPATH + os.path.sep + 'app_picture' + os.path.sep + '{}' + os.path.sep

# 生成报告时的地址
APPERROR = '../app_picture/{}/'

# 日志地址
LOGPATH = BASEPATH + os.path.sep + 'log' + os.path.sep

WEBLOGPATH = LOGPATH + 'server.log'

# 用例地址
CASEPATH = BASEPATH + os.path.sep + 'testCase' + os.path.sep

# 配置数据地址
CONFPATH = BASEPATH + os.path.sep + 'conf' + os.path.sep

WEBPATH = CONFPATH + 'conf.json'

# APP配置地址
APPPATH = CONFPATH + 'appController.yml'

if __name__ == '__main__':
    print(BASEPATH)

