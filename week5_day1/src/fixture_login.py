# 用户认证类
class UserAuth:

    def __init__(self):
        # 用户使用字典管理
        self.users = {}

    def register(self, username, password, email):
        '''
        注册
        :param username: 用户名
        :param password: 密码
        :param email: 邮箱
        :return:
        '''
        if not username or not password or not email:
            raise ValueError("用户名或者密码或者邮箱不能为空！")
        if len(password) < 6:
            raise ValueError("密码必须大于等于6位！")
        self.users[username] = {"password": password, "email": email}

    def login(self, username, password):
        '''
        登录
        :param username: 用户名
        :param password: 密码
        :return:
        '''
        if username not in self.users:
            raise ValueError("用户没有找到！")
        if self.users[username]["password"] != password:
            raise ValueError("密码错误！")
        return "Login successful"

    def change_password(self, username, old_password, new_password):
        '''
        修改密码
        :param username: 用户名
        :param old_password: 旧密码
        :param new_password: 新密码
        :return:
        '''
        if username not in self.users:
            raise ValueError("用户没有找到！")
        if self.users[username]["password"] != old_password:
            raise ValueError("原始密码错误！")
        if len(new_password) < 6:
            raise ValueError("新密码必须大于等于6位！")
        self.users[username]["password"] = new_password






