# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# class TestInteractions:
#     def setup_method(self):
#         # 初始化 WebDriver
#         self.driver = webdriver.Chrome()
#         # 设置隐式等待时间
#         self.driver.implicitly_wait(10)
#
#     def teardown_method(self):
#         # 退出浏览器
#         self.driver.quit()
#
#     def test_interaction_demo(self, driver):
#         driver.get("https://www.sogou.com/")
#         # 输入内容
#         search_box = driver.find_element(By.ID, "query")
#         search_box.send_keys("霍格沃兹测试开发")
#         # 清空输入框
#         search_box.clear()
#         # 点击搜索按钮
#         search_button = driver.find_element(By.ID, "stb")
#         search_button.click()

# 课堂练习三：定位交互练习
# id
# class name
# name
# link test
# partial link test
# tag name
# css selector（绝对定位）
# xpath（绝对定位）
# 练习网站：https://vip.ceshiren.com/#/ui_study/locate

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestInteractions:

    def setup_class(self):
        # 初始化WebDriver
        self.driver = webdriver.Chrome()
        # 设置隐式等待
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        # 退出WebDriver
        self.driver.quit()

    def test_interaction_demo2(self):
        # 打开ui练习网址
        self.driver.get("https://vip.ceshiren.com/#/ui_study")
        # 获取元素文本
        text = self.driver.find_element(By.ID, "frame").text
        # 获取这个元素的name属性的值
        text2 = self.driver.find_element(By.ID, "locate_id").get_attribute("name")
        print(text)
        print(text2)