from appium import webdriver
from lib.core.config import Configure

app = Configure().app_data
package = app.get('tester')
deivce = app.get('devices').get('android')[0]
deivce.update(package)
print(deivce)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', deivce)
# webview切换例子
element = driver.find_element_by_id('url')
import time
time.sleep(1)
element.send_keys('http://ui.imdsx.cn/uitester/')
time.sleep(2)
driver.press_keycode(66)
driver.switch_to.context(driver.contexts[1])
driver.find_element_by_css_selector('#i1').send_keys(11111)
driver.quit()

# 滚动操作
# element = driver.find_element_by_id('url')
# import time
#
# time.sleep(1)
# element.send_keys('http://www.taobao.com')
# time.sleep(1)
# driver.press_keycode(66)
# l = driver.get_window_size()
# x1 = l['width'] * 0.5
# y1 = l['height'] * 0.9
# y2 = l['height'] * 0.2
# time.sleep(5)
# driver.swipe(x1, y1, x1, y2, 300)

# 定位方式

# class 定位方式尝试 支持先定位到一个父级 然后在定位其中的子集
# element = driver.find_elements_by_class_name('android.widget.LinearLayout')[-1]
# ele = element.find_elements_by_class_name('android.widget.TextView')
# ele[-1].click()
# ele.click()



# 1、appium原理
# 2、appium初始化配置参数
# 3、获取package和activity的方式 aapt 和 findstr start
# 4、uiautomatorviewer的使用方法
# 5、appium-desktop使用方法
# 6、appiuim定位方式
# 7、定位方式总结
# 8、常用appium api
# 9、native_app和webview切换
# 10、pyapp封装
# 11、yaml
# 12、 队列
# 13、logger
# 14、subprocess
# 15、装饰器
