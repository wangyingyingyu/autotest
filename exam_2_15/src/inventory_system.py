import pytest
import yaml

"""你正在测试一个智能仓库系统。该系统可以管理库存、订单和物流。你需要编写测试用例，确保系统功能正确，并能正确处理各种异常情况。

被测系统功能要求：

库存管理：每个商品有库存量，当商品库存为0时，用户无法下单。
订单管理：系统允许创建、查看、取消订单。
物流管理：每个订单会分配一个物流编号，物流状态可以是“待处理”、“运输中”、“已送达”。

"""
import random

current_number = 0  # 全局变量，初始化为 0
def product_id():
    global current_number  # 声明使用全局变量
    # 将当前数字格式化为五位，并填充前导零
    number_string = f"{current_number:0{3}}"
    current_number += 1  # 自增
    return number_string
def get_random_status():
    # 定义状态列表
    statuses = ["待处理", "运输中", "已送达"]
    # 随机选择一个状态
    return random.choice(statuses)

def add_flow():
    flow_status = []
    # digits = random.sample(range(10), 2)
    # id = ''.join(map(str, digits))
    flow_status.append(product_id())
    # 00 01 02 03

    flow_status.append(get_random_status())
    return flow_status

class Product:
    products = []

    # 添加商品，如果商品存在，增加库存，单价不同，修改单价、库存
    def add_product(self,name,price,num):
        product_dict = {}
        for i in Product.products:
            if i['name'] == name:
                if i['price'] != price:
                    i['price'] = price
                    i['num'] = num
                    print('修改库存数量')
                    return '修改单价和库存数量'
                else:
                    i['num'] += num
                    print('修改库存数量')
                    return '修改库存数量'
        else:
            product_dict['name'] = name
            product_dict['price'] = price
            product_dict['num'] = num
            Product.products.append(product_dict)

            print('添加商品')
            return '添加商品'
    def delete_product(self,name):
        for i in Product.products:
            if i['name'] == name:
                Product.products.remove(i)
                return '删除商品'
        return '商品不存在'

    # 商品信息查询：用户可以查询商品的名称、价格、库存等信息。
    # [{'name': ,'price': ,'num': }]
    def check_product(self,name):
        for i in Product.products:
            if name == i['name']:
                print(i)
                return '商品存在'
        return '商品不存在'

class Inventory:
    def __init__(self):
        self.inventory = []
        # 调用商品、物流实例对象
    def add_order(self,name,num):
        order_data = {}
        order_data_list = []
        for i in Product.products:
            if name == i['name']:
                if  i['num'] >= num:
                    order_data['name'] = name
                    order_data['price'] = i['price']
                    order_data['num']  = num
                    i['num'] -= num
                    order_data_list.append(add_flow())
                    order_data_list.append(order_data)
                    self.inventory.append(order_data_list)
                    #print(order_data_list)
                    print(self.inventory)

                    print('订单成功')

                    return '订单成功'
                elif 0 < i['num'] < num:
                    order_data['name'] = name
                    order_data['price'] = i['price']
                    order_data['num'] = i['num']
                    i['num'] -= num
                    order_data_list.append(add_flow())
                    order_data_list.append(order_data)
                    self.inventory.append(order_data_list)
                    print(f'库存不足只能发货{i["num"]}件')
                    return '按库存数量发货'
                else:
                    return '库存为0'
        print('库存中没有该商品')
        return '订单失败:库存中没有该商品'
# [[['00000', '待处理'],{'name': ,'price': ,'num':}]]
    def check_order(self,id_name:str):
        for i in self.inventory:
            if id_name == i[0][0]:
                print(i)
                return '订单存在'
        print('订单不存在')
        return '订单不存在'
    def delete_order(self,id_name):
        for i in self.inventory:
            if id_name == i[0][0]:
                self.inventory.remove(i)

                return '订单取消'
        return '订单不存在'
    # [[{'name': ,'price': , 'num': },[id,status]]
    def check_flow(self,id_name):
        for i in self.inventory:
            if id_name == i[0][0]:
                print(i[0][1])
                return '查询成功'
        print('查询失败')
        return "查询失败"


if __name__ == '__main__':
    product1 = Product()
    product1.add_product('a', 1, 3)
    product1.check_product('a')
    order1 = Inventory()
    order1.add_order('a', 2)
    product1.check_product('a')
    order1.check_flow('000')
    order1.check_order('000')



