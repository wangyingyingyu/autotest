import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCss:
    def setup_method(self):
        service = Service(r'D:\chrome\chrome-driver\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(10)
        self.var = {}
    def teardown_method(self):
        self.driver.quit()
    def test_css(self):
        self.driver.get('https://ceshiren.com/')  #body>section>div>div>div>div>div>div>ul>li:nth-child(4)
        self.driver.maximize_window()          #[id='#ember1359'][title='按类别分组的所有话题']
        value=self.driver.find_element(By.CSS_SELECTOR,"body>section>div>div>div>div>div>div>ul>li:nth-child(4)").get_attribute('value')
        print(f"输入框的值为: {value}")
        #assert value == "Jane", f"输入框的值应为 'Jane'，但实际为 '{value}'"
        #assert value == '',f'输入框的值应为""，但实际为{value}'