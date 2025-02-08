from exceptions import ProductNotFoundError

class InventoryManager:
    def __init__(self, inventory):
        self.inventory = inventory

    def query_inventory(self):
        '''
        查询库存
        '''
        if not self.inventory:
            print("当前库存为空！")
        else:
            print("\n商品库存：")
            for name, stock in self.inventory.items():
                print(f"- {name}: {stock} 件")

    def update_stock(self, product_name, new_stock):
        '''
        更新库存
        :param product_name: 商品名称
        :param new_stock: 新库存数量
        '''
        try:
            if product_name not in self.inventory:
                raise ProductNotFoundError(f"商品 '{product_name}' 不存在！")
            self.inventory[product_name] = new_stock
            print(f"商品 '{product_name}' 的库存已更新为 {new_stock} 件。")
        except ProductNotFoundError as e:
            print(e)

    def add_product(self, product_name, stock):
        '''
        添加新商品
        :param product_name: 商品名称
        :param stock: 商品库存数量
        '''
        if product_name in self.inventory:
            print(f"商品 '{product_name}' 已存在！无法重复添加。")
        else:
            self.inventory[product_name] = stock
            print(f"已添加商品 '{product_name}'，库存为 {stock} 件。")