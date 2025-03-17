import time

import yaml
from selenium.webdriver.common.by import By
from web_auto_test.po1.page.base_page import BasePage


class ContactsPage(BasePage):

    def add_contacts_save(self):

        # 点击添加成员
        self.driver.find_element(By.XPATH,
        '/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[3]/div[10]/a[1]').click()
        # 添加成员名称
        self.driver.find_element(By.XPATH,'//*[@id="username"]').send_keys("Tom")
        # 添加账号
        self.driver.find_element(By.XPATH,'//*[@id="memberAdd_acctid"]').send_keys("123456")
        # 添加成员手机号
        self.driver.find_element(By.XPATH,'//*[@id="memberAdd_phone"]').send_keys("12345678901")

        # 2. 滚动到特定元素
        element = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div/div/div[2]/div/div[4]/div/form/div[3]')
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)

        # 点击保存
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/main/div/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()
        # 获取弹窗文本
        texts = self.driver.switch_to.alert.text
        # assert texts == "保存成功"
        return texts
        # success_message = self.driver.find_element(By.XPATH,'./html/body/div[3]')
        # 使用 WebDriverWait 等待消息元素出现
        # success_message = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located((By.CSS_SELECTOR, './html/body/div[3]'))  # 替换为实际的成功提示元素的 CSS 选择器
        # )
        # assert "保存成功" in success_message.text  # 替换为实际提示的部分文本
        # print("添加成功的提示信息验证通过:", success_message.text)

        # 点击取消按钮
    def add_contacts_not_save(self):
        # 点击添加成员
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[3]/div[10]/a[1]').click()
        # 添加成员名称
        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("Tom")
        # 添加账号
        self.driver.find_element(By.XPATH, '//*[@id="memberAdd_acctid"]').send_keys("123456")
        # 添加成员手机号
        self.driver.find_element(By.XPATH, '//*[@id="memberAdd_phone"]').send_keys("12345678901")

        self.driver.find_element(By.XPATH,'//*[@class="qui_btn ww_btn js_btn_cancel"]').click()

        # self.driver.switch_to.alert.dismiss()
        # 点击离开此页按钮//*[@id="__dialog__9324__"]/div/div[3]/a[2]
        # WebDriverWait(self.driver,5).until()
        # self.driver.find_element(By.XPATH,'//*[@class="qui_btn ww_btn"]').click()
        fail_text = self.driver.find_element(By.XPATH, '//*[@class="msgDlg_right_text"]')
        if fail_text.get_attribute('innerText') == '成员的资料尚未保存，确定要离开吗？':
            self.driver.find_element(By.XPATH, '//*[text()="离开此页"]').click()
        return fail_text
