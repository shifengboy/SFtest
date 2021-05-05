from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class Pyse(object):
    def __init__(self, browser='chrome'):
        if browser.lower() == 'chrome':
            option = webdriver.ChromeOptions()
            option.add_argument('--start-maximized')
            driver = webdriver.Chrome(chrome_options=option)
        elif browser.lower() == 'firefox':
            driver = webdriver.Firefox()
        elif browser.lower() == 'ie':
            driver = webdriver.Ie()
        self.driver = driver

    def get_element(self, css):
        '''
         获取元素
        :param css:
        :return:
        '''
        by = css.split('=>')[0]
        value = css.split('=>')[1]

        self.wait_element(css)

        if by == 'css':
            element = self.driver.find_element_by_css_selector(value)
        elif by == 'id':
            element = self.driver.find_element_by_id(value)
        elif by == 'name':
            element = self.driver.find_element_by_name(value)
        elif by == 'class':
            element = self.driver.find_element_by_class_name(value)
        return element

    def wait_element(self, css, timeout=10, poll=0.5):
        '''
         等待元素是出现
        :param css:
        :param timeout: 最终超时时间
        :param poll: 每隔多少秒扫描一次
        :return:
        '''
        by = css.split('=>')[0]
        value = css.split('=>')[1]
        if by == 'css':
            WebDriverWait(self.driver, timeout, poll).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        elif by == 'id':
            WebDriverWait(self.driver, timeout, poll).until(EC.presence_of_element_located((By.ID, value)))
        elif by == 'xpath':
            WebDriverWait(self.driver, timeout, poll).until(EC.presence_of_element_located((By.XPATH, value)))
        elif by == 'name':
            WebDriverWait(self.driver, timeout, poll).until(EC.presence_of_element_located((By.NAME, value)))
        elif by == 'class':
            WebDriverWait(self.driver, timeout, poll).until(EC.presence_of_element_located((By.CLASS_NAME, value)))

    def get(self, url):
        '''
        请求url方法
        :param url:
        :return:
        '''
        self.driver.get(url)

    def click(self, css):
        '''
        点击操作
        :param css:
        :return:
        '''
        ele = self.get_element(css)
        ele.click()

    def type(self, css, value):
        '''
        发送文本内容
        :param css:
        :param value:
        :return:
        '''
        ele = self.get_element(css)
        ele.send_keys(value)

    def max_window(self):
        self.driver.maximize_window()

    def clear(self, css):
        ele = self.get_element(css)
        ele.clear()

    def move_to_element(self, css):
        ele = self.get_element(css)
        ActionChains(self.driver).move_to_element(ele).perform()

    def drag_to_drop(self, source, target):
        source_element = self.get_element(source)
        target_element = self.get_element(target)
        ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def F5(self):
        self.driver.refresh()

    def back(self):
        self.driver.back()

    def go_on(self):
        self.driver.forward()

    def select_to_value(self, css, value):
        sele = self.get_element(css)
        Select(sele).select_by_value(value)

    @property
    def window_handles(self):
        return self.driver.window_handles

    def window(self, i):
        '''
        接收 0 或 -1
        0：代表当前windos
        :param i:
        :return:
        '''
        self.driver.switch_to.window(self.window_handles[i])

    def new_window(self):
        current  = self.driver.current_window_handle
        for handle in self.window_handles:
            if handle != current:
                self.driver.switch_to.window(handle)

    def iframe(self,css):
        ifra = self.get_element(css)
        self.driver.switch_to.frame(ifra)

    def parent_iframe(self):
        self.driver.switch_to.parent_frame()

    def defult_content(self):
        self.driver.switch_to.default_content()

    def accept(self):
        self.driver.switch_to.alert.accept()

    def dismiss(self):
        self.driver.switch_to.alert.dismiss()

    @property
    def alert_text(self):
        return self.driver.switch_to.alert.text


    def screenshot_as_file(self):
        self.driver.get_screenshot_as_file()

    def wait_to_exception_save_file(self,css):
        try:
            self.wait_element(css)
        except Exception as e:
            self.screenshot_as_file()
    def js(self,js):
        self.driver.execute_script(js)


if __name__ == '__main__':
    driver = Pyse()
    driver.get('http://ui.imdsx.cn/move/')
    driver.drag_to_drop('css=>#dragger', 'css=>#i1')
    driver.quit()

