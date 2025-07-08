import time

import yaml
from web_auto_ERP_test.po.page.main_page import MainPage

from web_auto_ERP_test.po.page.base_page import BasePage
class Login(BasePage):
    def login(self):
        # 1、访问八爪云主页/登录页面
        self._driver.get('http://wxorder.taover.com/login?redirect=%2Fdashboard')
        # 2、定义cookie,cookie信息从已经写入的cookie文件中获取
        cookie = yaml.safe_load(open("../data/cookie.yaml"))
        # 3、植入cookie
        for c in cookie:
            self._driver.add_cookie(c)
        time.sleep(3)
        self._driver.get('http://wxorder.taover.com/login?redirect=%2Fdashboard')
        return MainPage(self._driver)

