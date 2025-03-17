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

# 测试人社区搜索 添加 allure 数据
class TestDefaultSuite:

    def setup_method(self, method):
        # 设置 ChromeDriver 路径
        service = Service(executable_path=r'D:\chrome\chrome-driver\chromedriver-win64\chromedriver.exe')
        # 复用浏览器
        option = Options()
        option.add_argument("--no-sandbox")  # 禁用沙盒模式
        option.add_experimental_option("detach", True)  # 保持浏览器打开
        # option.address_debugger="localhost:9222"
        self.driver = webdriver.Chrome(options=option,service=service)

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # 隐式等待 10 秒
        self.vars = {}

    # def teardown_method(self):
    #     self.driver.quit()

    def test_get_cookies(self):
        # 1. 访问企业微信主页/登录页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 2. 等待20s，人工扫码操作
        time.sleep(10)
        # 3. 等成功登陆之后，再去获取cookie信息
        cookie = self.driver.get_cookies()
        # 4. 将cookie存入一个可持久存储的地方，文件
        # 打开文件的时候添加写入权限
        with open("./data/cookie.yaml", "w") as f:
            # 第一个参数是要写入的数据
            yaml.safe_dump(cookie, f)
    def test_add_weixin(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        time.sleep(1)
        # 2. 定义cookie，cookie信息从已经写入的cookie文件中获取
        cookie = yaml.safe_load(open("./data/cookie.yaml"))
        # 3. 植入cookie
        for c in cookie:
            self.driver.add_cookie(c)
        time.sleep(2)
        # # 4.再次访问企业微信页面，发现无需扫码自动登录，而且可以多次使用
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        #点击通讯录
        self.driver.find_element(By.XPATH,'//*[@id="menu_contacts"]/span').click()
        # 点击添加成员
        self.driver.find_element(By.XPATH,
        '/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[3]/div[10]/a[1]').click()
        # 添加成员名称
        self.driver.find_element(By.XPATH,'//*[@id="username"]').send_keys("Tom")
        # 添加账号
        self.driver.find_element(By.XPATH,'//*[@id="memberAdd_acctid"]').send_keys("123456")
        # 添加成员手机号
        self.driver.find_element(By.XPATH,'//*[@id="memberAdd_phone"]').send_keys("12345678901")

        # # 2. 滚动到特定元素
        # element = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div/div/div[2]/div/div[4]/div/form/div[3]')
        # self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # time.sleep(2)

        # 点击保存
        #self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/main/div/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()
        # # 获取弹窗文本
        # texts = self.driver.switch_to.alert.text
        # assert texts == "保存成功"
        # success_message = self.driver.find_element(By.XPATH,'./html/body/div[3]')
        # 使用 WebDriverWait 等待消息元素出现
        # success_message = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located((By.CSS_SELECTOR, './html/body/div[3]'))  # 替换为实际的成功提示元素的 CSS 选择器
        # )
        # assert "保存成功" in success_message.text  # 替换为实际提示的部分文本
        # print("添加成功的提示信息验证通过:", success_message.text)

        # 点击取消按钮
        self.driver.find_element(By.XPATH,'//*[@class="qui_btn ww_btn js_btn_cancel"]').click()

        # self.driver.switch_to.alert.dismiss()
        # 点击离开此页按钮//*[@id="__dialog__9324__"]/div/div[3]/a[2]
        # WebDriverWait(self.driver,5).until()
        # self.driver.find_element(By.XPATH,'//*[@class="qui_btn ww_btn"]').click()
        fail_text = self.driver.find_element(By.XPATH, '//*[@class="msgDlg_right_text"]')
        if fail_text.get_attribute('innerText') == '成员的资料尚未保存，确定要离开吗？':
            self.driver.find_element(By.XPATH, '//*[text()="离开此页"]').click()


        # # 删除成员,点击复选框
        # self.driver.find_element(By.XPATH,'//*[@id="member_list"]/tr[1]/td[1]/input').click()
        # # 点击删除按钮
        # self.driver.find_element(By.XPATH,'//*[@id="js_contacts70"]/div/div[2]/div/div[2]/div[3]/div[10]/a[3]').click()
        #
        # # 获取弹窗，点击删除
        # self.driver.switch_to.alert.accept()
        # text2=self.driver.switch_to.alert.text
        # print(text2)
        # assert text2 == "正在删除"


