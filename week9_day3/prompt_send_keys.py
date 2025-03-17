"""Prompt 弹窗获取文本、输入内容、确认操作"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def test_confirm():
    service = Service(r"D:\chrome\chrome-driver\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("http://sahitest.com/demo/promptTest.htm")
    driver.find_element(By.NAME,"b1").click()
    #添加显式等待，等待弹框的出现
    WebDriverWait(driver, 5).until(ec.alert_is_present())
    #切换到弹框
    alert = driver.switch_to.alert
    #向弹框输入一段文本

    alert.send_keys('Selenium Alert弹出窗口输入信息')
    time.sleep(2)
    #点击确定

    alert.accept()
    time.sleep(2)
