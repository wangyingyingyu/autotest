"""
课堂练习：模拟登录系统
设置一个预定义的用户名和密码，用户最多输入 3 次。如果用户名和密码正确，输出 "登录成功"；如果失败 3 次，输出 "登录失败"。
"""
def log_in():
    n = 1
    while n < 4:
        user = input('请输入用户名：')
        password = input('请输入密码：')
        if user == 'hog' and password == '123':
            print('登录成功')
            return

        else:
            print('密码或用户名输入错误')
            n += 1

    print('登陆错误')
log_in()