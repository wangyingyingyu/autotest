"""
Python编程实现：餐厅订单管理系统

基础功能：

创建一个基类 Restaurant，包含餐厅名称 name、菜单 menu（字典，{菜品名称: 价格}）和顾客订单 orders（列表，存储订单信息）。
提供方法 display_menu 展示餐厅菜单。
提供方法 add_dish，接收菜品名称 dish_name 和菜品价格 price 两个参数。
扩展功能：

"""
class Restaurant:
    def __init__(self,name):
        self.name = name
        # 字典 key值为菜品名称，value值为价格
        self.menu = {}
        # 顾客订单
        self.orders = []
    def display_menu(self):
        print(f'{self.name}菜单信息为：')
        for i in self.menu.keys():
            print(f'{i}价格为{self.menu[i]}')
        # for dish_name, dish_price in self.menu.keys():
        #     print(f'{dish_name}价格为{dish_price}')
# 添加菜单 菜名和价格
    def add_dish(self,dish_name,price):
        if dish_name in self.menu.keys():
            print(f'{dish_name}已经在餐厅菜单中')
        else:
            self.menu[dish_name] = price
            print(f'{dish_name}已添加到餐厅菜单中')
        #                   顾客名      菜品名称      菜品数量
    def add_order(self,customer_name,dish_name,quantity):

        self.person_order ={}
        # 查看菜名是否在菜单字典中：
        if dish_name in self.menu.keys():

            self.person_order['customer_name'] = [customer_name]
            self.person_order['order'] = [dish_name,quantity]
            self.person_order['total']  =[self.menu[dish_name]*quantity]
            self.orders.append(self.person_order)
            print(self.orders)

        else:
            print(f'该餐厅没有{dish_name}')
#[0]}*{order[1]  [{'customer_name': ['Tom'], 'order': ['西湖醋鱼', 1], 'total': [70]}]
#Restaurant 提供 display_orders 方法，展示所有顾客订单，格式为：顾客名: 菜品1 x 数量, 菜品2 x 数量 ---- 总金额.
    def display_orders(self):
        for i in self.orders:
            print(i,type(i))
            print(f'{i["customer_name"]}: {i["order"][0]*i["order"][1]} --- {i["total"]}')


"""
创建 FastFoodRestaurant 类，继承自 Restaurant。
新增打折功能 set_discount（可为某些菜品设置折扣）。接收菜品名称 dish_name 和菜品折扣后的价格 discount_price 两个参数。
打折菜品信息记录在实例变量 discounts 中（字典，{菜品名称: 折扣后价格}）
顾客操作：

Restaurant 提供 add_order 方法，接收顾客姓名 customer_name、菜品名称 dish_name、菜品数量 quantity 三个参数。
允许顾客根据菜品名称和数量下单，检查菜品是否存在，计算总金额并添加到订单列表中。
订单数据格式为：{"customer_name": "name", "order": {"dish": quantity}, "total": amount}
Restaurant 提供 display_orders 方法，展示所有顾客订单，格式为：顾客名: 菜品1 x 数量, 菜品2 x 数量 ---- 总金额.
高级功能：

使用多态设计一个方法 welcome_message，支持不同餐厅展示不同的欢迎语。
"""
class FastFoodRestaurant(Restaurant):
    def __init__(self):
        super().__init__(self)
        # 字典 菜品名：折扣后的价格
        self.discounts = {}

    def set_discount(self,dish_name,discount_price):
        if dish_name in self.menu:
            self.discounts[dish_name] = [discount_price]
            print(f'菜品{dish_name}打折后价格为{discount_price}')
        else:
            print(f'{dish_name}不在餐厅菜单中')


# 实例化餐厅对象
r1 = Restaurant('西湖饭店')
r2 = Restaurant('西湖饭店')
r3 = Restaurant('西湖饭店')


# 添加菜单
r1.add_dish('西湖醋鱼',70)
r2.add_dish('麻辣小龙虾',66)
r3.add_dish('麻婆豆腐',50)
# 展示订单信息
r1.display_menu()
r2.display_menu()
r3.display_menu()

# 顾客点单
r1.add_order('Tom','西湖醋鱼',1)
r2.add_order('张三','麻辣小龙虾',2)
r3.add_order('李四','麻婆豆腐',3)

# 展示所有顾客订单
r1.display_orders()
r2.display_orders()
r3.display_orders()

# 实例化FastFoodRestaurant对象
p1  = FastFoodRestaurant()

# 给餐厅菜打折
p1.set_discount('西湖醋鱼', 60)


# 展示订单信息
r1.display_menu()
r2.display_menu()
r3.display_menu()












