"""Alert弹窗获取文本与确认操作"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def test_alert():
    driver = webdriver.Chrome()
    driver.get("http://sahitest.com/demo/alertTest.htm")
    driver.find_element(By.NAME, "b1").click()
    # 添加显式等待，等待弹框的出现
    WebDriverWait(driver, 5, 0.5).until(ec.alert_is_present())
    # 切换到弹框
    alert = driver.switch_to.alert
    # 打印弹框的文本
    print(alert.text)
    # 点击确定
    alert.accept()
    # 点击取消或者关闭弹框
    # alert.dismiss()
