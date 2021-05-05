# 27号加一天课 （selenium框架搭建+实战）
# 28号开始学习appium
# 3号appium框架搭建
# 20号（selenium的api）
# selenium build（欠着）
# uirecorder（工具）
'''
# 1、selenium源码分析
#安装、pip install selenium
    # 在site-packages

# 2、api讲解
#     a、webdriver的api
#     b、element api
#     c、鼠标悬浮
#     d、下拉框处理
#     e、iframe、windows tag、alert
# 3、练习
'''

# from selenium import webdriver
# driver = webdriver.Chrome()
#
# # 请求目标网址
# driver.get("http://ui.imdsx.cn/uitester/")

# selenium是经典的server-client的设计模式。
# webdriver在启动的时候启动了server（浏览器），client（代码）。
# 创建了一个浏览器，通过session去指定我们要链接的浏览器
# http请求，调用浏览器源生api，处理我们的请求，点击、拖拽。执行完成之后
# 返回结果。
# selenium 2.x selenium RC的方式，解析我们的客执行户端代码，转换成js代码执行操作。弊端：完全依赖于转化js的转换
# selenium 3.x 完全用WebDriver
import time

from selenium import webdriver
'''
# Chrome的配置
# option = webdriver.ChromeOptions()
# # 增加启动就放大浏览器
# option.add_argument("--start-maximized")
# # 启动浏览器
# driver = webdriver.Chrome(chrome_options=option)

# 请求目标网址
# driver.get("http://ui.imdsx.cn/uitester/")

# 定位方式 也叫选择器（selenium 提供了大概18种方式）
# 1、单数模式 8种
# 全屏浏览器
# driver.maximize_window()
# id定位方式 1
# element = driver.find_element_by_id('i1')
# class 定位 2
# element = driver.find_element_by_class_name('classname')
# named定位 3
# element = driver.find_element_by_name('name')
# css 定位方式 4
# element = driver.find_element_by_css_selector('[placeholder="请通过CSS SELECTOR定位元素"]')
# xpath 定位方式 5
# element = driver.find_element_by_xpath('//*[@placeholder="请通过XPATH定位元素"]')
# link_text 6
# element = driver.find_element_by_link_text('跳转大师兄博客地址')
# partial_link_text  包涵link 7
# 执行js
# element = driver.find_element_by_partial_link_text("跳转")
# tag_name 标签名 8
# element = driver.find_element_by_tag_name('input')

# 复数模式 以tag为例 返回的是相同所有元素，以list的方式返回
# element = driver.find_elements_by_tag_name('input')[5]
# driver.find_elements_by_class_name()
# driver.find_elements_by_id()
# driver.find_elements_by_link_text()
# driver.find_elements_by_partial_link_text()
# driver.find_elements_by_name()
# driver.find_elements_by_xpath()
# driver.find_elements_by_css_selector()
# 以上8 中复数定位方式
# 底层的剩余两种
# driver.find_element()
# driver.find_elements()
#  向文本框发送字符串
# element.send_keys('UI自动化')　＊＊＊＊＊＊
# 点击
# element.click()　　＊＊＊＊＊＊
# 2、复数模式 8种
# 3、底层实现 2种


driver = webdriver.Chrome()
# 获取浏览器大小
# size = driver.get_window_size()
# # 设置浏览器大小
# driver.set_window_size(1200,100)

# 获取当前浏览器的tag的名字或者理解为对象
# print(driver.current_window_handle) *****
driver.get('http://ui.imdsx.cn/uitester/')
time.sleep(1)
driver.execute_script('window.scrollTo(0,0);')

driver.find_element_by_css_selector('[href="/new-index/"]').click()
# 获取所有浏览器窗口的名字
# print(driver.window_handles) ******
# 返回当前url
# print(driver.current_url)
# 返回浏览器名
# print(driver.name)
# 页面面源码
# print(driver.page_source)
# 标题
# print(driver.title)
# driver.get_screenshot_as_file('测试.png')  *******
#　全部退出关于WebDriver的浏览器
# driver.quit()
# 只推出当前tag
# driver.close()
'''
# element.send_keys('qingleta')
# time.sleep(2)
# 清楚文本框的内容
# element.clear()
# 获取属性
# print(element.get_attribute('display'))


# driver.find_element_by_css_selector('[href="/new-index/"]').click()
# # driver.current_window_handle
# # driver.window_handles[-1]
# driver.switch_to.window(driver.window_handles[-1])
# element = driver.find_element_by_css_selector('#newtag')
# time.sleep(1)
# element.send_keys(11111)
# driver.close()
# time.sleep(1)
# driver.switch_to.window(driver.window_handles[0])
# time.sleep(1)
# driver.find_element_by_css_selector('#i1').send_keys(11111)
# time.sleep(1)
# driver.quit()

# 上午学到的重点
# 1、18定位方式 主要其中8种单数定位方式。
# 2、click send_keys clear quit close
# 3、switch_to window 结合着用  window_handles

# switch模块
from selenium.webdriver.remote.switch_to import SwitchTo


# 跳到新建标签页面
# element = driver.find_element_by_css_selector('[name="top-frame"]')
# driver.switch_to.frame(element)
# # 跳到百度页面
# bank=driver.find_element_by_css_selector('[name="baidu-frame"]')
# driver.switch_to.frame(bank)
# time.sleep(2)
# driver.find_element_by_css_selector('#kw').send_keys(123123)
# # 返回当前iframe的上一层
# # driver.switch_to.parent_frame()
# driver.switch_to.default_content()
# driver.find_element_by_css_selector('#i1').send_keys(11111)

# iframe 的重点
# 1、iframe 一层一层跳转
# 2、driver.switch_to.frame(bank) 向下条一层
# 3、driver.switch_to.parent_frame() 向上跳一层
# 4、driver.switch_to.default_content() 跳到最外层


# driver.find_element_by_css_selector('#confirm').click()
# time.sleep(3)
# driver.switch_to.alert.accept() 确认
# driver.switch_to.alert.dismiss() 取消
# print(driver.switch_to.alert.text) 获取文案

# select 模块

# 鼠标悬浮操作 action
from selenium.webdriver.common.action_chains import ActionChains
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('http://ui.imdsx.cn/move/')
# driver.execute_script('window.scrollTo(0,0);')
# action = ActionChains(driver)
# ele = driver.find_element_by_css_selector('#a')
# ale = driver.find_element_by_css_selector('#dis1')
# 鼠标悬浮到目标元素，在click
# action.move_to_element(ele).click(ale).perform()
# ele =driver.find_element_by_css_selector('#dragger')
# tag = driver.find_element_by_css_selector('#i1')
# action.drag_and_drop(ele,tag).drag_and_drop().click()





# select 模块
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('http://ui.imdsx.cn/html/')
# driver.execute_script('window.scrollTo(0,1800);')
# ele = driver.find_element_by_xpath("//select[@name='city'][2]")
# # 取消选中 只用于多选
# Select(ele).deselect_by_value('2')
# # Select(ele).select_by_index(3)
# # ele.find_elements_by_css_selector("[value='4']")


# 1、服务环境不稳定
# 2、网络环境不稳定

# 等待
# 普通人用time （最不可取）
# 聪明人用 隐示等待
# 大神 用显示等待
# driver = webdriver.Chrome()
# driver.maximize_window()
# 隐士等待
# driver.implicitly_wait(4)

# 显示等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# WebDriverWait(driver,10).until(EC.current_url('www.imdsx.cn'))
# 不间断扫描dom  保证元素第一次出现后 不再做无谓的等待
# WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.ID, 'i1')))



# 浏览器的按钮操作
driver = webdriver.Chrome()
# driver.maximize_window()
# 刷新
# driver.refresh()
# 前进
# driver.forward()
# 后退
# driver.back()
import time
time.sleep(1)
driver.get('http://ui.imdsx.cn/js/')
data = driver.execute_script("document.getElementById('inner1').innerText")
print(data)