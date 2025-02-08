from order_controller import ReadController
from save_order import SaveOrder

class Login(SaveOrder, ReadController):
    def __init__(self, filename):
        # 只需要传递文件名，其他参数由订单管理系统处理
        super().__init__(filename, '', '', 0)

    def login(self):
        # 预定义的用户名和密码
        manage_name = "aaa"
        password = "123"

        # 最大尝试次数
        max_attempts = 3
        attempts = 0

        while attempts < max_attempts:
            # 用户输入用户名和密码
            username = input("请输入用户名: ")
            password = input("请输入密码: ")
            # 验证用户名和密码
            if username == manage_name and password == password:
                print("登录成功")
                break
            else:
                attempts += 1
                print(f"登录失败! 你还有 {max_attempts - attempts} 次机会。")
        if attempts == max_attempts:
            print("登录失败，已超出最大尝试次数。")

    def order_management_system(self):
        '''
        订单管理主程序
        :return:
        '''
        while True:
            print("\n请选择操作：\n"
                  "1. 输入用户名和密码：")
            print("2. 添加新订单")
            print("3. 查看历史订单")
            print("4. 退出系统")
            choice = input("请输入操作编号：")
            if choice == "1":
                self.login()
            elif choice == "2":
                customer_name = input("请输入客户姓名：")
                order_content = input("请输入订单内容：")
                order_amount = input("请输入订单金额（元）：")
                self.save_order_to_file(customer_name, order_content, order_amount)
            elif choice == "3":
                self.read_orders_from_file()
            elif choice == "4":
                print("退出系统，再见！")
                break
            else:
                print("无效输入，请重新选择！")