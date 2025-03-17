import allure
import pytest
import logging
import os
import time
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from week9_day2.util.log_util import logger  # 从 log_util 导入 logger

class LiteMall:
    def __init__(self,driver: WebDriver = None):
        if driver:
            self._driver = driver
        else:
            # 设置ChromeDriver路径
            service = Service(executable_path=r'D:\chrome\chrome-driver\chromedriver-win64\chromedriver.exe')
            # 设置option选项
            option = Options()
            # 禁用沙盒模式
            option.add_argument("--no-sandbox")
            # 保持浏览器打开
            option.add_experimental_option("detach",True)
            # 实例化浏览器驱动对象
            self._driver = webdriver.Chrome(options=option,service=service)
            self._driver.maximize_window()
            # 添加隐式等待
            self._driver.implicitly_wait(5)
    #登录按钮
    _CLICK_LOGIN = (By.XPATH, '//*[@class="el-button el-button--primary el-button--mini"]')
    # 商品管理按钮
    _GOOD_MANAGE =(By.XPATH,'//*[text()="商品管理"]/..')
    #商品列表按钮
    _GOOD_LIST =(By.XPATH,'//*[text()="商品列表"]/../../..')
    # 添加按钮
    _ADD_GOOD =(By.XPATH,'//*[text()="添加"]/..')
    # 商品添加页面显示等待
    _WAIT_ADD_PAGE = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/div')
    # 商品编号、
    _GOOD_ID =(By.XPATH,'//*[text()="商品编号"]/../div/div/input')
    # 商品名称
    _GOOD_NAME =(By.XPATH,'//*[text()="商品名称"]/../div/div/input')

    # 设置商品库存
    #设置按钮
    _SETTING =(By.XPATH,'//*[text()="设置"]/..')
    #货品售价
    _GOOD_PRICE =(By.XPATH,'//label[text()="货品售价"]/..//*[@class="el-input__inner"]')
    #货品数量
    _GOOD_QUANTITY =(By.XPATH,'//*[text()="货品数量"]/../div/div/input')
    #货品图片
    _GOOD_PICTURE =(By.XPATH,'//label[text()="货品图片"]/../div/div/div/input')
    # 确定
    _YES =(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[2]/div/div[3]/div/button[2]')
    # 上架按钮
    _LISTING =(By.XPATH,'//*[text()="上架"]/..')

    # 商品列表页面显示等待
    _WAIT_GOOD_LIST_PAGE = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/input')

    #查找商品
    #输入商品编号
    _ID =(By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[1]/div[2]/input')
    #输入商品名称
    _NANE =(By.XPATH, '//input[@placeholder="请输入商品名称"]')
    #点击查找按钮
    _FIND = (By.XPATH,'//span[text()="查找"]/..')
    #点击删除按钮
    _DELETE = (By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[12]/div/button[2]')

    # 重新查询已删除的商品
    _REFIND = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/div/span')

    # 删除成功
    _DELETE_TEXT = (By.XPATH,'/html/body/div[2]')


    # 查找页面元素
    def find(self,by,path):
        return self._driver.find_element(by,path)

    # 点击按钮
    def find_click(self,by,path):

        self.get_picture_source()
        return self.find(by,path).click()
    # 文本输入框输入文本或上传文件
    def find_send_keys(self,by,path,texts):

        self.get_picture_source()
        return self.find(by,path).send_keys(texts)

    # 清空输入框
    def find_clear(self,by,path):

        self.get_picture_source()
        return self.find(by,path).clear()
    # 显示等待元素可见
    # def web_wait(self,by,path):
    #     return WebDriverWait(self._driver,10).until(EC.visibility_of_element_located(by,path))
    def web_wait(self, by, path):
        return WebDriverWait(self._driver, 20).until(EC.visibility_of_element_located((by, path)))
    # 获取toast显示等待文本信息
    def get_toast_text(self,by,path):

        self.get_picture_source()
        text = self.web_wait(by,path).text
        return text

    # 配置日志
    def action_log(self):
        log_folder = "../data/logs"
        # 如果日志文件夹不存在，则创建
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        # 设置日志文件的路径
        log_file = os.path.join(log_folder, "action_log.log")

        # 配置日志
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler(log_file),  # 输出到文件
                logging.StreamHandler()  # 输出到控制台
            ]
        )



    def screen(self):
        # 获取当前时间，并将其格式化为YYYYMMDDHHMMSS的字符串格式
        now_time = time.strftime('%Y%m%d%H%M%S')
        # 将当前时间作为文件名，生成一个PNG格式的文件
        image_name = f'{now_time}.png'
        # 拼接路径前提要有上一层目录
        filepath = f"../data/img/{image_name}"
        # 当前屏幕截图保存到指定的文件路径
        self._driver.get_screenshot_as_file(filepath)
        allure.attach.file(filepath,
        # 这里需改成自己想要的图片的路径,
        name = "log截图",
        attachment_type = allure.attachment_type.PNG,
        extension = "png")
    #
    # def get_page_source(self):
    #     # 获取当前时间，并将其格式化为YYYYMMDDHHMMSS的字符串格式
    #     now_time =time.strftime('%Y°%m%d°%H%M%S')
    #     #将当前时间作为文件名，生成一个html格式的文件
    #     page_source_name =f'{now_time}.html'
    #     filepath = f"../data/img/{page_source_name}"
    #     # 当前屏幕截图保存到指定的文件路径
    #     self._driver.get_page_source_as_file(filepath)
    def get_page_source(self):
        # 获取当前时间，并将其格式化为YYYYMMDDHHMMSS的字符串格式
        now_time = time.strftime('%Y%m%d_%H%M%S')  # 使用下划线作为分隔符
        # 将当前时间作为文件名，生成一个html格式的文件
        page_source_name = f'{now_time}.html'

        # 使用os.path.join构建文件路径，确保跨平台兼容性
        filepath = os.path.join("..", "data", "html", page_source_name)

        # 如果目录不存在，则创建
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        # 获取页面源码
        page_source = self._driver.page_source

        # 将页面源码写入文件
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(page_source)
        allure.attach(page_source,
                      '附件是HTML类型',
                      allure.attachment_type.HTML,
                      extension = "html")
    def get_picture_source(self):
        self.screen()
        self.get_page_source()


