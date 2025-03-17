# def wait_until():
#     driver = webdriver.Chrome()
#     driver.get("https://vip.ceshiren.com/#/ui_study")
#     WebDriverWait(driver, 10).until(
#         expected_conditions.element_to_be_clickable(
#             (By.CSS_SELECTOR, '#success_btn')))
#     driver.find_element(By.CSS_SELECTOR, "#success_btn").click()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class WaitTest:
    @classmethod
    def setUpClass(cls):
        # 设置Chrome选项（如果需要）
        chrome_options = Options()
        # 初始化WebDriver
        cls.driver = webdriver.Chrome(options=chrome_options)
        # 设置隐式等待
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        # 退出WebDriver
        cls.driver.quit()

    @classmethod
    def wait_untils(cls):
        cls.driver.get("https://vip.ceshiren.com/#/ui_study")
        # 使用显式等待直到元素可点击
        res_element = WebDriverWait(cls.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#success_btn"))
        )
        res_element.click()

# 调用测试方法
if __name__ == "__main__":
    WaitTest.setUpClass()
    try:
        WaitTest.wait_untils()
    finally:
        WaitTest.tearDownClass()