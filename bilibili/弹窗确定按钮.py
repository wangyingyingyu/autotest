import time

from flask import Response
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def she(self):
    # 设置浏览器选项
    q1 = Options()
    q1.add_argument("--no-sandbox")  # 禁用沙盒模式
    q1.add_experimental_option("detach", True)  # 保持浏览器打开

    # 启动浏览器
    a1 = webdriver.Chrome(service=Service(r'chromedriver.exe'))
    a1.implicitly_wait(30)  # 设置隐式等待时间为 30 秒
    a1.get('https://bahuyun.com/bdp/form/1327923698319491072')  # 打开指定 URL

    return a1  # 返回 WebDriver 实例
a1 = she()
a1.get("https://sahitest.com/demo/alertTest.html")
a1.find_element(By.XPATH,'').click()
time.sleep(3)
# 获取弹窗内的文本内容要在点击弹窗确定按钮前面
print(a1.switch_to.alert.text)
# 点击弹窗确定按钮，弹窗自动小时
a1.switch_to.alert.accept()


def make_response(*args):
    response = Response(*args)
    return response