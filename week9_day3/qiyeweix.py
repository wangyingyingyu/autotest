import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

option = Options()
option.debugger_address = "localhost:9222"
service = Service(executable_path=r'D:\chrome\chrome-driver\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(options=option,service=service)
# service = Service(executable_path=r'D:\chrome\chrome-driver\chromedriver-win64\chromedriver.exe')
driver.implicitly_wait(10)
driver.get("https://work.weixin.qq.com/wework_admin/frame")
# 人工扫码
time.sleep(10)
# 点击通讯录
driver.find_element(By.XPATH,'//*[@id="menu_contacts"]/span').click()


# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
#
# option = Options()
# option.debugger_address = "localhost:9222"
# driver = webdriver.Chrome(options=option)
# driver.implicitly_wait(10)
# # driver.get("https://work.weixin.qq.com/wework_admin/frame")
# # 人工扫码
# # time.sleep(10)
# # driver.find_element(By.XPATH,'//*[text()="通讯录"]').click()
# # 点击添加成员
# driver.find_elements(By.XPATH,'//*[text()="添加成员"]')[1].click()

