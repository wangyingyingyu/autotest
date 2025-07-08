import time

from selenium.webdriver.common.by import By

from web_auto_ERP_test.po.page.base_page import BasePage

_ORDER_MANAGE=(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[1]/div/ul/div[9]')
_ORDER_LIST =(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div[1]/div/ul/div[9]/li/ul/div[1]')
_RECIPIENT_PHONE =(By.XPATH, '//input[@placeholder="请输入手机号"]')
_SEARCH = (By.XPATH,'//div[@class="el-col el-col-16"]//button[@class="el-button el-button--primary el-button--small"]')
_FIRST_ORDER =(By.XPATH,'//div[@class="flex items-center justify-start"]//span[@class="el-checkbox__input"]')
_UPLOAD_FLOW =(By.XPATH,'//div[@style="display: flex; justify-content: space-between;"]//div[@class="el-dropdown"][2]')

_WRITE_FLOW = (By.XPATH, "(//*[text()='填写物流'])[2]")
_SELECT = (By.XPATH,'/html/body/div[1]/div[1]/div[2]/section/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div[7]/div/div[2]/div[2]/div[3]/div/div[2]').click()
_ZHONG_TONG = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[2]')
_BAINJI = (By.XPATH, '//*[@id="pane-0"]/div[7]/div/div[2]/div[2]/div[3]/div/div[3]')
_WULIUDANHAO = (By.XPATH, '//input[@placeholder="请输入物流"]')
_SAVE = (By.XPATH, '//span[text()="保存"]')
_CHANNEL = (By.XPATH, '//span[text()="通知"]')
_SUBMIT = (By.XPATH, '//span[text()="提交并发货"]')
_OK = (By.XPATH, '/html/body/div[3]/div/div[3]/button[2]')
_GET_TEXT = (By.XPATH,'//div[@role="alert" and @class="el-message el-message--success"]')





class WaitingSent(BasePage):
    def wait_sent(self):
        """
        1、按收件人电话搜索商品
        2、上传物流：搜索的第一个商品填写物流
        3、选择中通快递 搜索渠道为通知
        :return:
        """
        # 点击订单管理
        self.find_click(*_ORDER_MANAGE)

        # 点击订单列表,进入待发货页面
        self.find_click(*_ORDER_LIST)

        # 显示等待，输入收件人手机号
        self.wait_visibility_sendkeys(*_RECIPIENT_PHONE,wait_time=10,text='15560064465')

        # 点击查询按钮
        self.find_click(*_SEARCH)
        # 点击查询的第一个订单
        self.find_click(*_FIRST_ORDER)
        # 点击上传物流
        self.find_click(*_UPLOAD_FLOW)

        # 点击填写物流按钮 /html/body/ul[2]/li[1] (//li[text()="填写物流"])
        # 使用 JavaScript 点击：
        # 如果尝试使用常规的 `click()` 方法无效，可以使用 JavaScript 来强制点击.
        self.js_click(*_WRITE_FLOW)
        # script = f"document.querySelector('{ele}').style.display='block';"
        # self.driver.execute_script(script)
        time.sleep(3)

        # 点击物流公司请选择按钮
        self.find_click(*_SELECT)
        # 点击中通快递
        self.find_click(*_ZHONG_TONG)
        # 点击编辑按钮
        self.find_click(*_BAINJI)
        # 输入物流单号
        self.find_click(*_WULIUDANHAO)
        # 点击保存
        self.find_click(*_SAVE)
        # 通知渠道点击通知
        self.find_click(*_CHANNEL)
        # 点击提交并发货
        self.find_click(*_SUBMIT)
        # 点击操作提示的确定 /html/body/div[3]/div/div[3]/button[2]
        self.find_click(*_OK)
    def get_text(self):
        # self.find_click()

        # 共更新1条记录，全部成功
        els = self.wait_present(*_GET_TEXT,wait_time=10)
        texts = els.text

        return texts