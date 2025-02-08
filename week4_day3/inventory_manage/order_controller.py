class ReadController:
    def __init__(self, filename):
        self.filename = filename

    def read_orders_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                orders = file.readlines()
                if orders:
                    print("\n历史订单：")
                    for order in orders:
                        print(order.strip())
                else:
                    print("没有历史订单。")
        except FileNotFoundError:
            print("文件未找到，请先添加一个订单。")
