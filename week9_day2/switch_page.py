import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
"""必应搜索霍格沃兹测试开发，点击霍格沃兹开发学社"""
class TestCookie:
    def setup_class(self):
        service = Service(r'D:\chrome\chrome-driver\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
    def teardown_class(self):
        self.driver.quit()

    def test_switch(self):
        self.driver.get("https://www.bing.com")
        # 查找搜索框
        search_box=self.driver.find_element(By.NAME,'q')
        # 输入霍格沃兹测试开发
        search_box.send_keys('霍格沃兹测试开发')
        # 提交搜索
        #search_box.submit()
        self.driver.find_element(By.CSS_SELECTOR,'#search_icon').click()
        # 点击霍格沃兹测试开发学社官网
        self.driver.find_element(By.XPATH,"//*[@class='b_algo']//*[contains(text(),'测试开发训练营 大厂私教职场守护')]/../../h2/a")
        #将获取到的window_handles赋值给一个变量handles
        handles = self.driver.window_handles
        time.sleep(2)
        # 切换句柄
        self.driver.switch_to.window(handles[-1])

        assert len(self.driver.find_element((By.CSS_SELECTOR,'.navbar-brand'))) == 1






















