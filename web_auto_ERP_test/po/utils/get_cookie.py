import time

import yaml


def get_cookie(self):
    # 1、访问八爪云主页/登录页面
    self.driver.get('http://wxorder.taover.com/login?redirect=%2Fdashboard')
    # 2、等待20秒输入账号名与账号密码
    time.sleep(20)
    # 3、等成功登陆后，再去获取cookie信息,将cookie信息赋值给一个变量保存
    cookie = self.driver.get_cookies()
    # 4、将cookie信息存入一个可持久存储的地方，文件
    with open("../data/cookie.yaml", "w") as f:
        yaml.safe_dump(cookie, f)