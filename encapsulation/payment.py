"""
实战代码
创建基础类 Payment，包含方法 pay(amount)。
创建 CreditCardPayment 子类，继承 Payment 并实现自己的支付逻辑。
创建 PayPalPayment 子类，继承 Payment 并实现自己的支付逻辑。
使用多态调用 pay() 方法，模拟支付过程
"""
class Payment:
    def pay(self,amount):
        pass
class CreditCardPayment(Payment):
    def pay(self,amount):
        return f'刷卡支付{amount}'
class PayPalPayment(Payment):
    def pay(self,amount):
        return f'电子支付{amount}'


class Payment:
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount):
        return f'刷卡支付 {amount}'


class PayPalPayment(Payment):
    def pay(self, amount):
        return f'电子支付 {amount}'




















if __name__ == '__main__':
    # 创建支付方式对象
    card1 = CreditCardPayment()
    card2 = PayPalPayment()

    # 准备金额
    amounts = ['50', '60']
    cards = [(card1, amounts[0]), (card2, amounts[1])]  # 使用元组将对象和金额关联

    # 使用多态调用 pay() 方法
    for card, amount in cards:
        print(f'{card.pay(amount)}')

# if __name__ == '__main__':
#     card1 = CreditCardPayment()
#     card2 = PayPalPayment()
#     amount1 = '50'
#     amount2 = '60'
#     cards = [card1, card2]
#
#     # 对每个支付方法调用 pay 方法，传递相应的金额
#     for card in cards:
#         if isinstance(card, CreditCardPayment):
#             print(card.pay(amount1))
#         elif isinstance(card, PayPalPayment):
#             print(card.pay(amount2))



















