import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestDefaultSuite:

    def setup_method(self, method):
        # 设置 ChromeDriver 路径
        service = Service(r'D:\chrome\chrome-driver\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(10)  # 隐式等待 10 秒
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_testdemo(self):
        # 访问 Flask 服务器的 URL
        self.driver.get("http://127.0.0.1:5052/html")
        self.driver.maximize_window()

        # 显式等待页面加载完成
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "information"))
        )

        # 获取输入框的值并打印

        # value = self.driver.find_element(By.ID, "fname").get_attribute('value')
        # value = self.driver.find_element(By.CLASS_NAME, "information").get_attribute('value')
        #
        # value = self.driver.find_element(By.CSS_SELECTOR, "#fname").get_attribute('value')
        # value = self.driver.find_element(By.CSS_SELECTOR, ".information").get_attribute('value')
        # value = self.driver.find_element(By.CSS_SELECTOR, "from>#fname").get_attribute('value')
        # value = self.driver.find_element(By.CSS_SELECTOR, "from #fname").get_attribute('value')
        # value = self.driver.find_element(By.CSS_SELECTOR, "[id='fname' ]").get_attribute('value')
        #
        # value = self.driver.find_element(By.LINK_TEXT, "Selenium Official Page").get_attribute('href')
        # value = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Official Page").get_attribute('href')
        #
        # value = self.driver.find_element(By.TAG_NAME, "//form/input[@id='fname']").get_attribute('value')
        value = self.driver.find_element(By.XPATH, "//input[@id='fname']").get_attribute('value')

        print(f"输入框的值为: {value}")
        # self.driver.find_element(By.CSS_SELECTOR, "#fname")
        # self.driver.find_element(By.ID, "lname")
        # self.driver.find_element(By.NAME, "newsletter")
        # self.driver.find_element(By.LINK_TEXT, "Selenium Official Page")
        # self.driver.find_element(By.PARTIAL_LINK_TEXT, "Official Page")
        # self.driver.find_element(By.TAG_NAME, "a")
        # self.driver.find_element(By.XPATH, "//input[@value='f']")


        # 断言输入框的值是否为 "Jane"
        assert value == "Jane", f"输入框的值应为 'Jane'，但实际为 '{value}'"