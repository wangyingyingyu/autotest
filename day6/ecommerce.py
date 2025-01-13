"""
实战：电商平台的折扣计算
创建一个 Ecommerce 类，包含一个静态方法 calculate_discount。
静态方法接收商品的原价和折扣百分比，返回折扣后的价格。
实现如下功能：
使用静态方法计算不同商品的折扣价格。
在主程序中展示多个商品的折扣计算结果
"""
class Ecommerce:
    @staticmethod
    def calculate_discount(original_price, discount_percentage):
        '''
        计算折扣后的价格
        '''
        if 0 <= discount_percentage <= 100:
            discount_amount = original_price * (discount_percentage / 100)
            discounted_price = original_price - discount_amount
            return discounted_price
        else:
            discounted_price = original_price
            return  discounted_price
if __name__ == "__main__":
    # 定义多个商品的原价和折扣百分比
    products = [
        {"name": "手机", "original_price": 5000, "discount_percentage": 10},
        {"name": "笔记本电脑", "original_price": 8000, "discount_percentage": 15},

    ]

    # 每个商品的折扣价格
    print("商品折扣价格计算结果：")
    for product in products:
        discounted_price = Ecommerce.calculate_discount(
            product["original_price"],
            product["discount_percentage"]
        )
        print(f"{product['name']} - 原价: {product['original_price']}元, "
              f"折扣: {product['discount_percentage']}%, "
              f"折扣后价格: {discounted_price:.2f}元")















