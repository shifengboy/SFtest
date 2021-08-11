# 在百度搜索框输入  python ，复制粘贴搜狗输入框进行搜索
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
driver.find_element_by_css_selector('#kw').send_keys('python')
sleep(2)
driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL, 'a')  # 全选
driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL, 'c')  # 复制
driver.find_element_by_css_selector('#kw').send_keys(Keys.CONTROL, 'x')  # 剪切
sleep(2)
driver.get('http://www.sogou.com')
driver.find_element_by_css_selector('.sec-input').send_keys(Keys.CONTROL, 'v')  # 粘贴
sleep(2)
driver.find_element_by_css_selector('#stb').click()
sleep(2)
driver.quit()