# import logging
#
# import allure
# import pytest
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# # 测试人社区搜索 添加allure数据
# class TestDefaultSuite:
#
#     def setup_method(self, method):
#         # 设置 ChromeDriver 路径
#         service = Service(r'D:\chrome\chrome-driver\chromedriver-win64\chromedriver.exe')
#         self.driver = webdriver.Chrome(service=service)
#         self.driver.implicitly_wait(10)  # 隐式等待 10 秒
#         self.vars = {}
#
#     def teardown_method(self, method):
#         self.driver.quit()
#
#     def test_testdemo(self):
#         # 访问 Flask 服务器的 URL
#         self.driver.get("https://ceshiren.com/")
#         logging.info("打开测试人社区")
#         self.driver.maximize_window()
#         logging.info("页面最大化")
#
#         # 显式等待页面加载完成
#         WebDriverWait(self.driver, 10).until(
#             EC.presence_of_element_located((By.CLASS_NAME, "information"))
#         )
#
#         # 点击搜索，点击搜索
#         self.driver.find_element(By.CSS_SELECTOR,'#search-button > svg').click()
#         logging.info("点击搜索icon")
#         # .send_keys("allure")
#         #查找搜索框，输入搜索内容，
#         self.driver.find_element(By.CSS_SELECTOR,"#search-term").send_keys("allure")
#         logging.info("点击搜索框，输入搜索内容")
#         #点击高级搜索
#         self.driver.find_element(By.XPATH,'//*[@id="ember6"]/header/div/div/div[2]/div/div/div/div/div[1]/div/a/svg')
#         logging.info("打开高级搜索")
#         # 附加截屏到 Allure 报告
#         allure.attach(self.driver.get_screenshot_as_file(f"./log_data/1.png"), name="截屏", attachment_type=allure.attachment_type.PNG)

import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from week9_day2.util.log_util import logger  # 从 log_util 导入 logger

# 测试人社区搜索 添加 allure 数据
class TestDefaultSuite:

    def setup_method(self, method):
        # 设置 ChromeDriver 路径
        service = Service(r'D:\chrome\chrome-driver\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(10)  # 隐式等待 10 秒
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    @allure.title("测试搜索功能")  # 为测试用例添加标题
    @allure.description("测试在测试人社区中搜索 allure 的功能")  # 为测试用例添加描述
    def test_testdemo(self):
        # 访问 Flask 服务器的 URL
        self.driver.get("https://ceshiren.com")
        time.sleep(20)
        logger.info("打开测试人社区")
        self.driver.maximize_window()
        logger.info("页面最大化")

        # # 显式等待页面加载完成
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.CLASS_NAME, "information"))
        # )

        # 点击搜索ICON
        self.driver.find_element(By.CSS_SELECTOR, '#search-button > svg').click()
        logger.info("点击搜索icon")

        # 查找搜索框，输入搜索内容
        self.driver.find_element(By.CSS_SELECTOR, "#search-term").send_keys("allure")
        logger.info("点击搜索框，输入搜索内容")

        # 点击高级搜索
        self.driver.find_element(By.CSS_SELECTOR, '#ember6 > header > div > div > div.panel.clearfix > div > div > div > div > div.search-input > div > a > svg').click()
        logger.info("打开高级搜索")

        # 附加截屏到 Allure 报告
        screenshot_path = f"./log_data/1.png"  # 将截图保存到 logs 目录

        self.driver.get_screenshot_as_file(screenshot_path)  # 保存截图
        allure.attach.file(screenshot_path, name="截屏", attachment_type=allure.attachment_type.PNG)

        logger.info("附加截屏到 Allure 报告")


def test_ceshiren(self):
    image_path = Path(__file__).parent / 'image_path'
    image_path.mkdir(exist_ok=True, parents=True)
    self.driver.get("https://ceshiren.com/")
    logger.info("打开首页")
    png_path = str(image_path / f'{time.time()}.png')
    self.driver.save_screenshot(png_path)
    allure.attach.file(source=png_path, name="图片", attachment_type=allure.attachment_type.PNG, extension="png")
    allure.attach(self.driver.page_source, '附件是HTML类型', allure.attachment_type.HTML)

    self.driver.find_element(By.CSS_SELECTOR, '[title="搜索"]').click()
    logger.info("点击搜索")
    png_path = str(image_path / f'{time.time()}.png')
    self.driver.save_screenshot(png_path)
    allure.attach.file(source=png_path, name="图片", attachment_type=allure.attachment_type.PNG, extension="png")
    allure.attach(self.driver.page_source, '附件是HTML类型', allure.attachment_type.HTML)

    self.driver.find_element(By.CSS_SELECTOR, '[title="打开高级搜索"]').click()
    logger.info("点击高级搜索")
    png_path = str(image_path / f'{time.time()}.png')
    self.driver.save_screenshot(png_path)
    allure.attach.file(source=png_path, name="图片", attachment_type=allure.attachment_type.PNG, extension="png")
    allure.attach(self.driver.page_source, '附件是HTML类型', allure.attachment_type.HTML)

    self.driver.find_element(By.CSS_SELECTOR, '[placeholder="搜索"]').send_keys("selenium")
    logger.info("输入selenium")
    png_path = str(image_path / f'{time.time()}.png')
    self.driver.save_screenshot(png_path)
    allure.attach.file(source=png_path, name="图片", attachment_type=allure.attachment_type.PNG, extension="png")
    allure.attach(self.driver.page_source, '附件是HTML类型', allure.attachment_type.HTML)

    self.driver.find_element(By.CSS_SELECTOR, '[aria-label="搜索"]').click()
    logger.info("点击搜索按钮")
    png_path = str(image_path / f'{time.time()}.png')
    self.driver.save_screenshot(png_path)
    allure.attach.file(source=png_path, name="图片", attachment_type=allure.attachment_type.PNG, extension="png")
    allure.attach(self.driver.page_source, '附件是HTML类型', allure.attachment_type.HTML)
