"""
实战：电商购物车系统的测试
电商平台的购物车是用户在购物过程中临时存放商品的地方，用户可以在购物车中查看商品、添加商品、删除商品，并计算商品的总价，最后可以进行结算。
"""
import yaml

class Goods:
    def __init__(self,name,count,price):
        self.name = name
        self.count = count
        self.price = price
        self.total = count*price
class ShoppingCart:
    def __init__(self):
        self.goods_list = []
        # 传入一个商品名称字符串
    def goods_info(self,good_name):
        found = False
        for i in self.goods_list:
            if good_name == i["name"]:
                return f"商品 {good_name} 信息为：数量：{i['count']} 单价：{i['price']} 总价： {i['total']}"
                # print( f"商品 {good_name} 信息为："
                #        f"数量： {i['count']} "
                #        f"单价： {i['price']} "
                #        f"总价： {i['total']}")
                found = True
                # break # 找到商品后，直接退出循环

        if not found:
            print(f"商品 {good_name} 不存在")  # 如果遍历完成后还没找到，输出不存在

        # 传入一个商品类实例对象
    def add_good(self,good):
        # 标志变量，表示是否找到了已有商品
        found = False

        # 遍历现有商品列表
        for item in self.goods_list:
            if good.name == item["name"]:
                # 如果商品已经存在，更新数量和总价
                item["count"] += good.count
                item["total"] += good.count * good.price
                return f'商品{good.name}已更新'
                found = True
                break  # 找到后可以提前退出循环

        # 如果商品不存在，添加新商品
        if not found:
            good_data = {}
            good_data["name"] = good.name
            good_data["count"] = good.count
            good_data["price"] = good.price
            good_data["total"] = good.count * good.price
            self.goods_list.append(good_data)
            return f'商品{good.name}已添加'
            # 传入一个商品名称字符串
    def del_good(self,good_name):
        for i in self.goods_list:
            if good_name == i["name"]:
                self.goods_list.remove(i)
                return f"商品{good_name}信息已从购物车删除"

        return f"商品{good_name}不存在"

    def settle_accounts(self):
        total_crash = 0
        for i in self.goods_list:
            total_crash += i["total"]
        return f"购物车总账单为{total_crash}"
    # 将数据储存为.yaml文件
    def write_json(self):
        with open('shopping_cart.yaml','w') as file:
            yaml.safe_dump(self.goods_list,file)
        with open('shopping_cart.yaml','r') as f:
            data = yaml.safe_load(f)
            print(f'购物车商品信息展示：{data}')




# 实例化商品对象
good1 = Goods('iphone',2,8000)
good2 = Goods('book',8,60)
good3 = Goods('cosmetics',5,500)
#查看商品、添加商品、删除商品，并计算商品的总价，最后可以进行结算。
# 实例化购物车对象
cart1 = ShoppingCart()
cart1.add_good(good1)
cart1.add_good(good2)
cart1.add_good(good3)
cart1.goods_info('iphone')
cart1.del_good('iphone')

cart1.settle_accounts()
cart1.write_json()


































