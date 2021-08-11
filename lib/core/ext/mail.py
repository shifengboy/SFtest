# 导入smtplib模块
import smtplib
import time
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from lib.core.logger import logger
from lib.core.tool import getError


# 定义发送邮件方法
def sendMail():
    content = '''
    hi ALL ：
            UI自动化执行完成，请见报告。


                                tester
    '''
    config = Configure().read(ConfType.MAIL)
    title = '主流程回归'
    # 发送的文件
    filepath = getError.getpng()
    # 邮件发送者
    sender = config.get('sender')
    # 邮件发送者用户名
    senderName = config.get('username')
    # 邮件发送者密码
    senderPwd = config.get('passwd')
    # 邮件接收人
    receiverList = eval(config.get('receiverlist'))
    # 发送时间
    timeStr = time.strftime("%Y%m%d%H%M%S", time.localtime())
    # 标题
    subject = u"【UI自动化测试报告】" + title + "_" + timeStr
    # 邮件对象
    msg = MIMEMultipart()
    # 你所发的文字信息将以html形式呈现
    part = MIMEText(content, _subtype='html', _charset="utf-8")
    msg.attach(part)
    for v in filepath:
        if v[0].endswith('.html'):
            logger.debug('打开的文件: %s' % v[1])
            part = MIMEText(open(v[1], 'r', encoding='utf8').read())
            part["Content-Type"] = 'application/octet-stream'
            part["Content-Disposition"] = 'attachment; filename="%s"' % v[0]  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            msg.attach(part)
        elif v[0].endswith('.png'):
            part = MIMEImage(open(v[1], 'rb').read())
            part["Content-Type"] = 'application/octet-stream'
            part["Content-Disposition"] = 'attachment; filename="%s"' % v[0]  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            msg.attach(part)
    msg['Subject'] = Header(subject, 'utf-8')
    # 来自...
    msg['From'] = sender
    # 给谁...
    if len(receiverList) > 1:
        msg['To'] = ";".join(receiverList)
    else:
        msg['To'] = receiverList[0]
    logger.info('邮件接收LIST: %s' % msg['To'])
    try:
        smtp = smtplib.SMTP()
        smtp.connect(config.get('smtpserver'), 25)  # 连接至邮件服务器
        smtp.login(senderName, senderPwd)  # 登录邮件服务器
        smtp.sendmail(sender, receiverList, msg.as_string())  # 发送邮件
    except Exception as e:
        print(e)