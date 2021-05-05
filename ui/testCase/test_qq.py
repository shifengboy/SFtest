import unittest

from lib.page.app.page import Page


class AppDemo(unittest.TestCase):
    def __repr__(self):
        return 'appdemo'

    @classmethod
    def setUpClass(cls):
        cls.page = Page()

    def test_a_qq_login(self):
        self.page.reset_package()
        self.page.login()
        self.page.username()
        self.page.passwd()
        self.page.login()
        self.assertTrue(self.page.login_check(self.test_a_qq_login.__name__), 'msg')

    def test_b_set_device_lock_qq(self):
        self.page.photo()
        self.page.set_up()
        self.page.set_up_of_account()
        self.page.set_gesture_passwd()
        self.page.create_gesture()
        self.page.set_gesture()
        self.assertTrue(self.page.set_lock_check(self.test_b_set_device_lock_qq.__name__), 'msg')

    def test_c_relieve_device_lock_qq(self):
        self.page.close_app()
        self.page.launch_app()
        self.page.relieve_device_lock_qq(4)

    def test_d_remove_device_lock_qq(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.page.quit()

if __name__ == '__main__':
    unittest.main()