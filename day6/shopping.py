# 构造方法可以携带参数，根据类中属性的定义，
"""课堂练习
定义一个商品类，包含 商品名称 和 商品价格 两个属性，
实现商品类的对象描述方法和添加到购物车方法
定义一个购物车类，包含一个商品列表 属性，和 添加商品 及 显示所有商品 两个方法

class Goods:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'商品名称为{self.name},商品价格为{self.price}'

    def shopping_car(self):
        BuyCar.add_good(self)


class BuyCar:
    def __init__(self):
        self.goods_list = []

    def add_good(self,goods):
        self.goods_list.append(goods)

    def all_goods(self):
        for g in self.goods_list:
            print(g)


g1 = Goods('apple',10)
g2 = Goods('banana',15)
g3 = Goods('organge',14)
print(g1.shopping_car())
print(g2.shopping_car())
print(g3.shopping_car())


# c1 = BuyCar()
c1 = BuyCar()
print(c1.add_good(g1))
"""

class Goods:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'商品名称为{self.name}, 商品价格为{self.price}'

    def add_to_cart(self, cart):
        """将商品添加到购物车"""
        cart.add_good(self)


class BuyCar:
    def __init__(self):
        self.goods_list = []

    def add_good(self, goods):
        """将商品添加到购物车列表中"""
        self.goods_list.append(goods)

    def all_goods(self):
        """显示购物车中所有商品"""
        for g in self.goods_list:
            print(g)


# 创建商品对象
g1 = Goods('apple', 10)
g2 = Goods('banana', 15)
g3 = Goods('orange', 14)

# 创建购物车对象
c1 = BuyCar()

# 将商品添加到购物车
g1.add_to_cart(c1)
g2.add_to_cart(c1)
g3.add_to_cart(c1)

# 显示购物车中的所有商品
print("购物车中的商品：")
c1.all_goods()

















