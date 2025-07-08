import pytest
import time
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestERP:
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

    def test_add_order(self):
        # 1、访问八爪云主页/登录页面
        self.driver.get('http://wxorder.taover.com/login?redirect=%2Fdashboard')
        # 2、定义cookie,cookie信息从已经写入的cookie文件中获取
        cookie = yaml.safe_load(open("./data/cookie.yaml"))
        # 3、植入cookie
        for c in cookie:
            self.driver.add_cookie(c)
        time.sleep(3)
        self.driver.get('http://wxorder.taover.com/login?redirect=%2Fdashboard')

        # 点击订单管理
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[1]/div/ul/div[9]').click()

        # 点击订单列表,进入待发货页面
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[1]/div[1]/div/div[1]/div/ul/div[9]/li/ul/div[1]').click()

        # 显示等待，输入订单编号
        ele03 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="请输入手机号"]')))
        ele03.send_keys('15560064465')

        # 显示等待点击查询按钮
        els01 = WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.XPATH,
                                 '//div[@class="el-col el-col-16"]//button[@class="el-button el-button--primary el-button--small"]')))
        els01.click()
        # 点击查询的第一个订单
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                                 '//div[@class="flex items-center justify-start"]//span[@class="el-checkbox__input"]').click()
        # 点击上传物流
        self.driver.find_element(By.XPATH,
                                 '//div[@style="display: flex; justify-content: space-between;"]//div[@class="el-dropdown"][2]').click()

        # 点击填写物流按钮 /html/body/ul[2]/li[1] (//li[text()="填写物流"])
        ele = self.driver.find_element(By.XPATH, "(//*[text()='填写物流'])[2]")

        # script = f"document.querySelector('{ele}').style.display='block';"
        # self.driver.execute_script(script)
        # 使用 JavaScript 点击：
        # 如果尝试使用常规的 `click()` 方法无效，可以使用 JavaScript 来强制点击.
        self.driver.execute_script("arguments[0].click();", ele)
        time.sleep(3)

        # 点击物流公司请选择按钮
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[1]/div[2]/section/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div[7]/div/div[2]/div[2]/div[3]/div/div[2]').click()

        # 点击圆通快递 //ul[@class="el-scrollbar__view el-select-dropdown__list"]/li[@class="el-select-dropdown__item hover"]
        # /html/body/div[3]/div[1]/div[1]/ul/li[1]
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
        # 点击编辑按钮
        self.driver.find_element(By.XPATH, '//*[@id="pane-0"]/div[7]/div/div[2]/div[2]/div[3]/div/div[3]').click()
        # 输入物流单号
        self.driver.find_element(By.XPATH, '//input[@placeholder="请输入物流"]').send_keys('00001')
        # 点击保存
        self.driver.find_element(By.XPATH, '//span[text()="保存"]').click()
        # 通知渠道点击通知
        self.driver.find_element(By.XPATH, '//span[text()="通知"]').click()
        # 点击提交并发货
        self.driver.find_element(By.XPATH, '//span[text()="提交并发货"]').click()
        # 点击操作提示的确定 /html/body/div[3]/div/div[3]/button[2]
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button[2]').click()

        # 共更新1条记录，全部成功
        els = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//div[@role="alert" and @class="el-message el-message--success"]')))
        texts = els.text

        print(texts)
