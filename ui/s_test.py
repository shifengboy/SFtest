import os

import yaml

from ui.lib.core.path import CONFPATH

main_page_file = CONFPATH + 'web' + os.path.sep + 'koubei' + os.path.sep + 'main_page.yml'

with open(main_page_file, encoding='UTF-8') as f:
    datas = yaml.safe_load(f)
    data = datas['login']
    for i in data:
        print(i['action'].split(',')[0])