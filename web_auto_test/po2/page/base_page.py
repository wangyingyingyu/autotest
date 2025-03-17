from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver: WebDriver = None):
        if driver:
            self._driver = driver
        else:
            service = Service(executable_path=r'D:\Env\selenium_driver\chromedriver-win64\chromedriver.exe')
            options = Options()
            options.debugger_address = '127.0.0.1:9222'
            self._driver = webdriver.Chrome(service=service, options=options)
            self._driver.implicitly_wait(10)

    def find(self, by, value):
        return self._driver.find_element(by, value)

    def find_click(self, by, value):
        self.find(by, value).click()

    def find_and_send(self, by, value, text):
        self.find(by, value).send_keys(text)

    def get_attr(self, by, value, name):
        return self.find(by, value).get_attribute(name)

    def wait_element_located(self, by, value):
        return WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((by, value)))
