"""
实战：在线订餐系统
开发一个简单的在线订餐系统，允许餐厅添加菜品、顾客浏览菜品、选择菜品下单，并生成订单。

创建 Dish 类：
- 实例属性：菜品名称、价格、库存数量。 - 实例方法：展示菜品信息。

创建 Customer 类：
- 实例属性：顾客姓名、订单（字典：菜品 -> 数量）。 - 实例方法：展示顾客订单信息。

创建 OrderManager 类：
- 添加菜品、删除菜品、查看所有菜品。 - 顾客下单（检查菜品库存）。 - 计算订单总金额。 - 展示所有订单。

"""
# 使用构造方法添加实例属性
class Dish:
    def __init__(self, name, price, repertory):
        # 菜单名称、价格、仓库数量
        self.name = name
        self.price = price
        self.repertory = repertory

    # 展示菜品信息
    def show_menu(self):
        print(f'菜品名称为：{self.name}')
        print(f'菜品价格为：{self.price}')
        print(f'库存数量为：{self.repertory}')


class Customer:
    def __init__(self,name):
        #顾客姓名、订单
        self.name = name
        self.order = {}
        # 菜品信息实例对象作为键key值，菜品数量作为value值

    # 展示顾客的订单信息
    def show_order(self):
        if not self.order:
            print('当前顾客订单为空')
        else:
            crush =0
            for dish, num in self.order.items():
                crush += dish.price*num
                print(f'顾客{self.name}的订单信息：菜名：{dish.name}-数量{num}')
            print(f'订单总金额为{crush}')

        # 顾客下单，检查菜品库存 传入菜品实例对象      - 计算订单总金额。 - 展示所有订单。
    def order_new(self, food,num):
        # 判断库存是否大于下单的数量，判断客户订单中是否已有该菜品
        if food.repertory >= num:
            if food in self.order.keys():
                print(f'{food.name}已经点过{self.order[food]}份')
                self.order[food]+=num #将顾客订单中该菜品的数量加num份
                food.repertory -= num # 该菜品库存减num份
                print(f'这次{food.name}点了{num}份')
            else: #如果菜品不在订单中（第一次点），将菜品添加到订单字典
                self.order[food] = num
                food.repertory -= num  # 该菜品库存减num份
                print(f'{food.name}第一次点了{num}份')
        else:
            print(f'{food}库存仅为{food.repertory}份')
# 创建 OrderManager 类：
# - 添加菜品、删除菜品、查看所有菜品。 - 顾客下单（检查菜品库存）。 - 计算订单总金额。 - 展示所有订单。
class OrderManage:
    # 添加菜品 给一个菜品信息列表
    def __init__(self):
        self.menu_list = []

    # 添加菜品,传入菜品实例对象
    def add_menu(self, food):


        self.menu_list.append(food)
        print(f"添加菜品：{food.name}")

    # 删除菜品
    def del_menu(self,food):
        if food in self.menu_list:
            self.menu_list.remove(food)
            print(f'已删除{food.name}')
        else:
            print(f'{food.name}不存在')

    # 查看所有菜品
    def display_all_menu(self):
        for food in self.menu_list:
            food.show_menu()


    # 查看所有订单,传入客户实例对象
    def display_order(self,customer):
        customer.show_order()

# 创建菜品
dish1 = Dish("宫保鸡丁", 30, 100)
dish2 = Dish("麻辣香锅", 50, 50)
dish3 = Dish("红烧排骨", 40, 80)

# 创建订单管理系统
order_manager = OrderManage()
# 添加菜品
order_manager.add_menu(dish1)
order_manager.add_menu(dish2)
order_manager.add_menu(dish3)

# 创建顾客
customer1 = Customer("张三")
customer2 = Customer("李四")

# 顾客下单
customer1.order_new(dish1, 2)
customer2.order_new(dish2, 3)

# 查看顾客订单
order_manager.display_order(customer1)
order_manager.display_order(customer2)

# 删除菜品
order_manager.del_menu(dish3)

# 查看所有菜品
order_manager.display_all_menu()




























