import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from week9_day2.util.log_util import logger  # 从 log_util 导入 logger

# 测试人社区搜索 添加 allure 数据
class TestDefaultSuite:

    def setup_method(self, method):
        # 设置 ChromeDriver 路径
        service = Service(executable_path=r'D:\chrome\chrome-driver\chromedriver-win64\chromedriver.exe')
        # 复用浏览器
        option = Options()
        #option.address_debugger="localhost:9222"
        self.driver = webdriver.Chrome(options=option,service=service)
        self.driver.implicitly_wait(10)  # 隐式等待 10 秒
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()
    def test_action(self):
        self.driver.get("https://ceshiren.com")

