import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def window_start():

    #创建Chrome浏览器对象
    options = webdriver.ChromeOptions()
     # 初始化浏览器驱动
    driver = webdriver.Chrome(options=options)
     # 打开网页
    driver.get('https://www.ceshiren.com')
    time.sleep(2)
    driver.refresh()
    time.sleep(1)
    #关闭浏览器
    driver.quit()


if __name__=='__main__':
    window_start()
  
