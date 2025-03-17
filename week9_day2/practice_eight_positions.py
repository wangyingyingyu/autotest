"""练习：八大定位网站练习
练习网址 https://vip.ceshiren.com/#/ui_study/locate
基本练习： - 通过 id 属性定位页面中的【id】标签 - 通过 class 属性定位页面中的【class】标签
关系定位： - 通过父子关系定位页面中的【father】标签
顺序关系：父子关系+顺序 - 通过顺序关系定位到页面中的【sister】标签"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

class TestEightPosition:
    # 实例化谷歌浏览器操作对象
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://vip.ceshiren.com/#/ui_study/locate")
    def teardown(self):
        self.driver.quit()
    def test_locate(self):
        self.driver.find_element(By.ID,'located_id')
        self.driver




