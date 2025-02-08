from log_in import Login   # 主程序入口

if __name__ == "__main__":
    # 创建 Login 实例并传入文件名
    login = Login("orders.txt")
    login.order_management_system()