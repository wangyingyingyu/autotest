import backports.tarfile
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

class TestLitemall:
    def setup_method(self):
        # 设置ChromeDriver路径
        service = Service(executable_path=r'D:\chrome\chrome-driver\chromedriver-win64\chromedriver.exe')
        # 设置option选项
        option = Options()
        # 禁用沙盒模式
        option.add_argument("--no-sandbox")
        # 保持浏览器打开
        option.add_experimental_option("detach",True)
        # 实例化浏览器驱动对象
        self.driver = webdriver.Chrome(options=option,service=service)
        self.driver.maximize_window()
        # 添加隐式等待
        self.driver.implicitly_wait(5)
    def test_add_good(self):
        self.driver.get("https://litemall.hogwarts.ceshiren.com/")

        # 点击登录按钮
        self.driver.find_element(By.XPATH,'//*[@class="el-button el-button--primary el-button--mini"]').click()
        #  点击商品管理
        self.driver.find_element(By.XPATH,'//*[text()="商品管理"]/..').click()
        # 点击商品列表
        self.driver.find_element(By.XPATH,'//*[text()="商品列表"]/../../..').click()
        # 点击添加按钮 //*[@id="app"]/div/div[2]/section/div/div[1]/button[2]
        self.driver.find_element(By.XPATH,'//*[text()="添加"]/..').click()

        # 设置显示等待
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/div'))
        )

        # 填写商品编号
        self.driver.find_element(By.XPATH,'//*[text()="商品编号"]/../div/div/input').send_keys('001')
        # 填写商品名称
        self.driver.find_element(By.XPATH,'//*[text()="商品名称"]/../div/div/input').send_keys('菠萝蜜')
        # 设置商品库存
        # 点击设置按钮
        self.driver.find_element(By.XPATH,'//*[text()="设置"]/..').click()
        # 填写货品售价
        self.driver.find_element(By.XPATH,'//label[text()="货品售价"]/..//*[@class="el-input__inner"]').send_keys('30')
        # 填写货品数量
        self.driver.find_element(By.XPATH,'//*[text()="货品数量"]/../div/div/input').send_keys('20')
        # 上传货品图片  //*[@id="app"]/div/div[2]/section/div/div[1]/div/form/div[7]/div/div/div/input
        # //*[text()="货品图片"]/../div/div/div/input
        #self.driver.find_element(By.XPATH,'//label[text()="货品图片"]/../div/div/div/input').send_keys('./utils/boluomi.jpg')
        # 点击确定按钮
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[2]/div/div[3]/div/button[2]').click()
        # 点击上架按钮
        self.driver.find_element(By.XPATH,'//*[text()="上架"]/..').click()

        # 设置显示等待
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/input'))
        )

        # 查询商品
        # 输入商品编号 //*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/input //input[@placeholder="请输入商品编号"]
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/input').send_keys("001")
        #  输入商品名称
        self.driver.find_element(By.XPATH, '//input[@placeholder="请输入商品名称"]').send_keys("菠萝蜜")
        # 点击查找
        self.driver.find_element(By.XPATH,'//span[text()="查找"]/..').click()

    # 删除商品
        # 点击删除
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[12]/div/button[2]').click()
        # 点击清空输入框
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/input').clear()
        self.driver.find_element(By.XPATH, '//input[@placeholder="请输入商品名称"]').clear()
        # 输入商品编号 //*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/input //input[@placeholder="请输入商品编号"]
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/input').send_keys("001")
        #  输入商品名称
        self.driver.find_element(By.XPATH, '//input[@placeholder="请输入商品名称"]').send_keys("菠萝蜜")
        # 点击查找
        self.driver.find_element(By.XPATH, '//span[text()="查找"]/..').click()

        # 点击删除
        # self.driver.find_element(backports.tarfile.XGLTYPE,'//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[12]/div/button[2]').click()

        result_element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/div/span'))
        )
        # 获取 Toast 文本
        texts = result_element.text
        print("Toast 文本信息:", texts)


        # 使用显示等待，确保 Toast 可见
        # toast_element = WebDriverWait(self.driver, 5).until(
        #     EC.visibility_of_element_located((By.XPATH, '/div/div'))
        # )
        # # 获取 Toast 文本
        # toast_text = toast_element.text
        # print("Toast 文本信息:", toast_text)


