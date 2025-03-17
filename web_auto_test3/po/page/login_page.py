import logging

from selenium.webdriver.common.by import By

from web_auto_test3.po.page.base_page import LiteMall
from web_auto_test3.po.page.home_page import HomePage

# 登录页面,返回首页
class Login(LiteMall):
    # 点击登录按钮

    def login(self):
        self._driver.get("https://litemall.hogwarts.ceshiren.com/")
        logging.info("打开litemall网页")
        self.get_picture_source()
        self.find_click(*self._CLICK_LOGIN)
        logging.info("点击登录")
        self.get_picture_source()

        return HomePage(self._driver)
    #   Homepage是Homepage的实例对象