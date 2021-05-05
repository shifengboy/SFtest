这是一个基于Python语言的接口和ui自动化测试框架
环境搭建参考：
        Windows：https://www.cnblogs.com/feng0815/p/8179714.html
        macOS：https://www.cnblogs.com/feng0815/p/8215587.html
使用前请执行 `pip3 install -r requirements.txt` 命令安装依赖插件，否则我保证你运行不起来……

interface: 接口自动化框架
    该框架采用httprunner接口测试框架，由于这个框架太好用，暂时还不知道该添加什么功能……
    使用文档参考：https://www.cnblogs.com/feng0815/p/14402863.html
    
ui: UI自动化框架
    采用 selenium+appium+pytest+allure框架，基于 page object 模式进行基于数据驱动的二次封装
    conf:存放驱动数据
        web:PC端
        app:移动端
            appController.yml:dirvie启动初始参数
    lib:主要代码
        core：存放核心代码
            ext: 放了一些过时的和不需要的东西，不用看
            appController.py  启动appium服务、启动driver（对于server和deriver的一些管理操作，支持多线程）
            base.py: 基于selenium的二次封装，ing...
            baseapp.py: 基于appium的二次封装，ing...
            handle_black.py: 装饰器，用来处理页面弹窗等异常情况，保存成功和失败的图片，生成测试步骤
            tool.py 主要封装了工具类
            path.py: 存放各种路径地址
        page 存放各个页面的功能方法
            app:存放移动端页面功能
            web: PC端页面功能
    testCase 存放我们的case
        appCase: 移动端case
        webCase: PC端case
    report: 存放测试报告和图片
    bin: 运行入口
        apprun: 运行移动端case
        webrun: 运行PC端case



