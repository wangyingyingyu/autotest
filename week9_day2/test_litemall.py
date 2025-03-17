"""针对 litemall 商品的增删改查编写测试用例，要求添加关键数据。"""
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCss:
    def setup_method(self):
        service = Service(r'D:\chrome\chrome-driver\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(10)
        self.var = {}
    def teardown_method(self):
        self.driver.quit()
    def test_css(self):
        self.driver.get('https://litemall.hogwarts.ceshiren.com/#/goods/list')
        self.driver.maximize_window()
        #点击登录按钮
        self.driver.find_element(By.CSS_SELECTOR,'#app > div > form > button').click()
        # 点击商品管理下拉菜单
        self.driver.find_element(By.CSS_SELECTOR,
        '#app > div > div.sidebar-container.el-scrollbar > div.scrollbar-wrapper.el-scrollbar__wrap > div > ul > div:nth-child(3) > li > div > i').click()
        # 点击商品列表
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/div/ul/div[3]/li/ul/div[1]/a/li/span')
        # # 点击添加按钮
        # self.driver.find_element(By.CSS_SELECTOR,
        # "#app > div > div.main-container > section > div > div.filter-container > button:nth-child(5)").click()
        # # 点击添加页面的取消按钮
        #
        # self.driver.find_element(By.CSS_SELECTOR,
        # '#app > div > div.main-container > section > div > div.op-container > button.el-button.el-button--default.el-button--mini > span')
        #time.sleep(20)

        # 输入框输入商品ID
        self.driver.find_element(By.XPATH,
        '//*[@id="app"]/div/div[2]/section/div/div[1]/div[1]/input').send_keys('1468182')
        # 输入框输入商品名称
        self.driver.find_element(By.CSS_SELECTOR,
        '#app > div > div.main-container > section > div > div.filter-container > div:nth-child(3) > input').send_keys('粉苹果')
        # 点击查找按钮
        self.driver.find_element(By.CSS_SELECTOR,
        '#app > div > div.main-container > section > div > div.filter-container > button:nth-child(4) > span').click()
        time.sleep(3)
        #进入单个商品详情页，点击查看
        self.driver.find_element(By.XPATH,
        '//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[6]/div/button').click()

        # 点击取消弹窗
        # self.driver.switch_to.alert.dismiss()
        self.driver.find_element(By.XPATH,
        '//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[6]/div/div/div/div[1]/button/i').click()

        # 输入框输入商品ID
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[2]/section/div/div[1]/div[1]/input')

        # 点击清空商品ID输入框
        self.driver.find_element(By.XPATH,
        '/html/body/div/div/div[2]/section/div/div[1]/div[1]/span/span/i').click()

        # 输入框输入商品名称
        self.driver.find_element(By.CSS_SELECTOR,'#app > div > div.main-container > section > div > div.filter-container > div:nth-child(3) > input')

        # 点击清空商品名称输入框
        self.driver.find_element(By.XPATH,
        '//*[@id="app"]/div/div[2]/section/div/div[1]/div[3]/span/span/i').click()
         # 点击查找按钮返回全部商品列表
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[1]/button[1]/span').click()

        # 点击删除按钮
        self.driver.find_element(By.XPATH,
        '//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[2]/td[12]/div/button[2]/span').click()

        #


        # a2 = self.driver.window_handles
        # self.driver.switch_to.window(a2[1])