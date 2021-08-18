# sfuitest
这是一个基于Python语言的ui自动化测试框架

环境搭建参考：
- Windows：[https://www.cnblogs.com/feng0815/p/8179714.html](https://www.cnblogs.com/feng0815/p/8179714.html)
- macOS：[https://www.cnblogs.com/feng0815/p/8215587.html](https://www.cnblogs.com/feng0815/p/8215587.html)

使用前请执行 `pip3 install -r requirements.txt` 命令安装依赖插件，否则我保证你运行不起来……

  
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
&emsp;&emsp;&emsp;&emsp;handle.py: 装饰器，用来处理页面弹窗等异常情况，保存成功和失败的图片，生成测试步骤<br/>
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
log:存放各种日志<br/>
sftest.py:辅助函数，存放一些公共方法，用于脚本运行时调用<br/>

功能：<br/>
1、采用数据驱动的方式，所有定位元素数据存放在一份ymal文件中，方便后续维护

2、采用PO思想，每个页面为一个类，页面中每个功能为一个方法，页面之间支持跳转

3、编写用例时无需考虑具体实现细节，直接调用即可

4、用例支持失败重跑，可设置重跑次数，避免环境不稳定造成的失败

5、增加辅助函数功能，提供一些公共函数，脚本运行中可以直接调用，避免一些输入唯一性的校验

6、页面元素定位不找支持跳过，主要针对一些非必填选择输入框，没有数据时不报错，不阻碍流程

7、提供异常处理功能，对于一些页面可能出现的弹框等异常做处理



