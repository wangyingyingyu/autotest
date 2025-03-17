# 导入Selenium的webdriver模块
from selenium import webdriver
# 初始化Chrome浏览器驱动
driver = webdriver.Chrome()
# 初始化FireFox浏览器驱动
# driver = webdriver.FireFox()
# 打开网页
driver.get('https://www.ceshiren.com')
# 关闭浏览器
driver.quit()
