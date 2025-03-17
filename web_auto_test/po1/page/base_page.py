import pytest
import time

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from week9_day2.util.log_util import logger  # 从 log_util 导入 logger

# 测试人社区搜索 添加 allure 数据
class BasePage:

    def __init__(self):
        # 设置 ChromeDriver 路径
        service = Service(executable_path=r'D:\chrome\chrome-driver\chromedriver-win64\chromedriver.exe')
        # 复用浏览器
        option = Options()
        option.add_argument("--no-sandbox")  # 禁用沙盒模式
        option.add_experimental_option("detach", True)  # 保持浏览器打开
        # option.address_debugger="localhost:9222"
        self.driver = webdriver.Chrome(options=option,service=service)

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # 隐式等待 10 秒
        self.vars = {}

        # 1. 访问企业微信主页/登录页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 2. 等待20s，人工扫码操作
        time.sleep(10)
        # 3. 等成功登陆之后，再去获取cookie信息
        cookie = self.driver.get_cookies()
        # 4. 将cookie存入一个可持久存储的地方，文件
        # 打开文件的时候添加写入权限
        with open("../data/cookie.yaml", "w") as f:
            # 第一个参数是要写入的数据
            yaml.safe_dump(cookie, f)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        time.sleep(1)
        # 2. 定义cookie，cookie信息从已经写入的cookie文件中获取
        cookie = yaml.safe_load(open("../data/cookie.yaml"))
        # 3. 植入cookie
        for c in cookie:
            self.driver.add_cookie(c)
        time.sleep(2)
        # 4.再次访问企业微信页面，发现无需扫码自动登录，而且可以多次使用
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")




    # def teardown_method(self):
    #     self.driver.quit()



