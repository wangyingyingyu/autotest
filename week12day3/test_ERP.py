import pytest
import time
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_data():
    with open('./data/recipients.yaml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    """
    `send_keys()` 只接受字符串参数，因此需要将列表格式化为字符串
    [
    ['赫敏', '15560064465', '霍格沃兹学院格兰芬多'],
    ['哈利', '15560064466', '霍格沃兹学院格兰芬多'],
    ['罗恩', '15560064467', '霍格沃兹学院格兰芬多']
]
通过 `join` 进行合并, 并用换行符连接names = "\n".join([user[0] for user in user_data])
    """
    datas = "\n".join([str(d) for d in data])

    return datas


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

    def test_get_cookies(self):
        # 1、访问八爪云主页/登录页面
        self.driver.get('http://wxorder.taover.com/login?redirect=%2Fdashboard')
        # 2、等待20秒输入账号名与账号密码
        time.sleep(20)
        # 3、等成功登陆后，再去获取cookie信息,将cookie信息赋值给一个变量保存
        cookie = self.driver.get_cookies()
        # 4、将cookie信息存入一个可持久存储的地方，文件
        with open("./data/cookie.yaml","w") as f:
            yaml.safe_dump(cookie,f)
    # def test_add_cookies(self):
    #     # 1、访问八爪云主页/登录页面
    #     self.driver.get('http://wxorder.taover.com/login?redirect=%2Fdashboard')
    #     # 2、定义cookie,cookie信息从已经写入的cookie文件中获取
    #     cookie = yaml.safe_load(open("./data/cookie.yaml"))
    #     # 3、植入cookie
    #     for c in cookie:
    #         self.driver.add_cookie(c)
    #     time.sleep(3)
    #     self.driver.get('http://wxorder.taover.com/login?redirect=%2Fdashboard')


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
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div[1]/div/ul/div[9]').click()
        # 点击订单录入
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/div/div[1]/div/ul/div[9]/li/ul/div[4]').click()
        # 关闭弹窗
        # ele01 = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div/div[10]/div/div/div[1]/button')))
        # ele01.click()
        # 点击手动创建,跳转到文本信息页面
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div/div[2]/div/p[1]').click()
        # 点击请选择所属渠道,展示系统中存在的渠道列表
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[1]/div[1]/div/input').click()
        # 点击所选渠道
        time.sleep(1)
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/ul/li[1]').click()
        # 文本框输入收件人、收件人电话、收件人地址

        self.driver.find_element(By.XPATH, "//*[@autocomplete='off' and @rows='9']").send_keys(get_data())

        # 点击识别文本信息按钮
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[1]/button').click()
        # 双击商品下拉框，展示系统中已存在商品
        els = WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,'(//*[@placeholder="请选择"])[1]')))
        els.click()
        els7 = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '(//*[@placeholder="请选择"])[1]')))
        els7.click()
        time.sleep(1)
        # 等待列表的第一行元素出现，点击第一行商品
        ele6 = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div/div/span/span'))
        )
        ele6.click()
        time.sleep(1)
        # 点击商品 /html/body/div[4]/div[1]/div[2]
        ele9 = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div[1]/span'))
        )
        ele9.click()
        # 点击是一起修改
        self.driver.find_element(By.XPATH,'//*[@class="el-button el-button--default el-button--small el-button--primary "]').click()
        # # 输入供货价格
        # ele02 = self.driver.find_element(By.XPATH,'//*[@role="spinbutton"]')
        # ele02.clear()
        # ele02.send_keys('20')
        # # 点击提交按钮
        # self.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div/div/div/div[2]/div/div[3]/div/button[2]').click()

        # 定位到需要滚动的元素
        element = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div[1]/div[3]')

        # 向右滑动
        self.driver.execute_script("arguments[0].scrollLeft += arguments[0].clientWidth;", element)

        # 或者使用 scrollTo 方法来滚动特定的距离
        # driver.execute_script("arguments[0].scrollTo(arguments[0].scrollLeft + 100, 0);", element)
        time.sleep(2)
        # 点击数量输入框
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div/div').click()
        ele1 = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,
                                                                                   '//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div/div/div/input')))

        ele1.send_keys('100')

        # 点击第二个数量框
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[6]').click()
        # 点击一起修改商品数量按钮
        ele5 = WebDriverWait(self.driver,60).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div/div[3]/button[2]')))
        ele5.click()

        self.driver.find_element(By.XPATH,'//*[text()="全部提交"]').click()

        # 点击订单管理
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[1]/div/ul/div[9]').click()

        # 点击订单列表,进入待发货页面
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div[1]/div/ul/div[9]/li/ul/div[1]').click()

        # 显示等待，输入订单编号
        ele03 = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//input[@placeholder="请输入手机号"]')))
        ele03.send_keys('15560064465')

        # 点击查询按钮
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//div[@class="el-col el-col-16"]//button[@class="el-button el-button--primary el-button--small"]').click()
        # 点击查询的第一个订单
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//div[@class="flex items-center justify-start"]//span[@class="el-checkbox__input"]').click()
        # 点击上传物流
        self.driver.find_element(By.XPATH,'//div[@style="display: flex; justify-content: space-between;"]//div[@class="el-dropdown"][2]').click()

        # 填写物流按钮 /html/body/ul[2]/li[1] (//li[text()="填写物流"])
        ele=self.driver.find_element(By.XPATH, "(//*[text()='填写物流'])[2]")

        # script = f"document.querySelector('{ele}').style.display='block';"
        # self.driver.execute_script(script)
        self.driver.execute_script("arguments[0].click();", ele)
        time.sleep(3)
        ele.click()

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




