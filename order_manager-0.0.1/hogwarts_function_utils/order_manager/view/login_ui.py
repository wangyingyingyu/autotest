from hogwarts_function_utils.order_manager.controller.user_controller import UserController
from hogwarts_function_utils.order_manager.model.user import User


class LoginUI:
    def __init__(self):
        self.user_controller = UserController()

    def login_ui(self):
        username = input('请输入用户名：')
        password = input('请输入密码：')
        user = User(username=username, password=password)
        state = self.user_controller.login(user)

        if state:
            print("登录成功")
        else:
            print("登录失败")
