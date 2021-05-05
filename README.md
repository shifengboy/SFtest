
这是一个基于Python语言的接口和ui自动化测试框架

环境搭建参考：
- Windows：[https://www.cnblogs.com/feng0815/p/8179714.html](https://www.cnblogs.com/feng0815/p/8179714.html)
- macOS：[https://www.cnblogs.com/feng0815/p/8215587.html](https://www.cnblogs.com/feng0815/p/8215587.html)

使用前请执行 `pip3 install -r requirements.txt` 命令安装依赖插件，否则我保证你运行不起来……

# interface: 接口自动化框架
&emsp;&emsp;该框架采用httprunner接口测试框架，由于这个框架太好用，暂时还不知道该添加什么功能……

使用文档参考：https://www.cnblogs.com/feng0815/p/14402863.html
 
  
# ui: UI自动化框架<br/>
采用 selenium+appium+pytest+allure框架，基于 page object 模式进行基于数据驱动的二次封装<br/>
结构说明：<br/>
conf:存放驱动数据<br/>
&emsp;&emsp;web:PC端<br/>
&emsp;&emsp;app:移动端<br/>
&emsp;&emsp;&emsp;&emsp;appController.yml:dirvie启动初始参数<br/>
lib:主要代码<br/>
&emsp;&emsp;core：存放核心代码<br/>
&emsp;&emsp;&emsp;&emsp;ext: 放了一些过时的和不需要的东西，不用看<br/>
&emsp;&emsp;&emsp;&emsp;appController.py  启动appium服务、启动driver（对于server和deriver的一些管理操作，支持多线程）<br/>
&emsp;&emsp;&emsp;&emsp;base.py: 基于selenium的二次封装，ing...<br/>
&emsp;&emsp;&emsp;&emsp;baapp.py: 基于appium的二次封装，ing...<br/>
&emsp;&emsp;&emsp;&emsp;handle_black.py: 装饰器，用来处理页面弹窗等异常情况，保存成功和失败的图片，生成测试步骤<br/>
&emsp;&emsp;&emsp;&emsp;tool.py 主要封装了工具类<br/>
&emsp;&emsp;&emsp;&emsp;path.py: 存放各种路径地址<br/>
&emsp;&emsp;page 存放各个页面的功能方法<br/>
&emsp;&emsp;&emsp;&emsp;app:存放移动端页面功能<br/>
&emsp;&emsp;&emsp;&emsp;web: PC端页面功能<br/>
testCase 存放我们的case<br/>
&emsp;&emsp;appCase: 移动端case<br/>
&emsp;&emsp;webCase: PC端case<br/>
report: 存放测试报告和图片<br/>
bin: 运行入口<br/>
&emsp;&emsp;apprun: 运行移动端case<br/>
&emsp;&emsp;webrun: 运行PC端case<br/>



