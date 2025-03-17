"""实战练习
使用八大定位完成"百度搜索功能"自动化测试用例的编写，步骤如下：

打开百度搜索 https://www.baidu.com/
输入关键字："测试人社区"。
点击搜索按钮。
断言 “测试人社区” 在第一个标题中。"""

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBaidu:

    def setup_class(self):
        # 初始化WebDriver
        self.driver = webdriver.Chrome()
        # 设置隐式等待
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        # 退出WebDriver
        self.driver.quit()

    def test_baidu_demo2(self):
        # 打开ui练习网址
        self.driver.get("https://www.baidu.com/")
        # 获取元素文本
        text = self.driver.find_element(By.ID, "frame").text
        # 获取这个元素的name属性的值
        text2 = self.driver.find_element(By.ID, "locate_id").get_attribute("name")
        print(text)
        print(text2)


