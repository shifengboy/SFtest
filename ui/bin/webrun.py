import os

from ui.lib.core.path import CASEPATH,WEBREPORT


class TestCase:
    def koubei(self):
        case_path = CASEPATH+'webCase'+os.path.sep+'koubei'+os.path.sep
        os.system(f'pytest {case_path} -s -q --alluredir={WEBREPORT} --clean-alluredir')
        os.system(f'allure serve {WEBREPORT}')



if __name__ == '__main__':
    TestCase().koubei()