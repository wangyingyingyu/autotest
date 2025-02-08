class SaveOrder:
    def __init__(self, filename, customer_name, order_content, order_amount):
        self.filename = filename

    def save_order_to_file(self, customer_name, order_content, order_amount):
        with open(self.filename, 'a') as file:
            file.write(f"客户姓名: {customer_name}, 订单内容: {order_content}, 订单金额: {order_amount}\n")
