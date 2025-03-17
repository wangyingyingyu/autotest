import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
"""练习：企业微信跳过登录
前提：每个人注册一个企业微信账号，企业微信注册地址

使用 cookie 复用和浏览器复用分别完成企业微信登录操作。
具体实现方法包括以下几个步骤：

打开浏览器并登录，确保登录成功后获取 Cookie 信息。

将获取到的 Cookie 信息存储到本地文件中，以便于下次使用。通过文件读写操作，可以将 Cookie 信息保存到一个文本文件中。

检查本地文件中是否已经成功获取了 Cookie 信息。

再次打开浏览器并植入 Cookie 信息进入主页

通过以下两个方法，可以在自动化测试过程中模拟用户的登录状态，以便于进行后续的测试操作：

获取当前页面所有 cookie 信息，确保正确的 cookie 写入到一个本地文件中，通过driver.get_cookies()方法获取浏览器的当前所有 Cookie，具体代码参考方法：test_get_cookies()。
读取 Cookie 信息，并向浏览器添加 Cookie: driver.add_cookie(cookie)。，具体代码参考方法：test_add_cookie()。
"""
class TestCookie:
    def setup_class(self):
        service = Service(r'D:\chrome\chrome-driver\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
    def teardown_class(self):
        self.driver.quit()
    def test_get_cookie(self):





