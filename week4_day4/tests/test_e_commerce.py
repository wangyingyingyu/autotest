"""测试要求：
使用 pytest 框架测试以下功能：添加商品到购物车。删除商品从购物车中。计算购物车总价是否正确。
使用 setup 和 teardown 来管理测试环境。
使用 pytest 参数化 来编写测试用例，测试不同商品的添加和删除操作。
每个测试用例都需要使用 断言 来验证结果。"""
import pytest
from week4_day4.src.E_commerce_shopping_cart import ShoppingCart,Goods

def setup_module():
    print("模块测试开始")

def teardown_module():
    print("模块测试开始")

class TestShoppingCart:
    def setup_class(self):
        print("类测试开始")
    def teardown_class(self):
        print("类测试结束")
    def setup_method(self):
        self.cart1 = ShoppingCart()
        self.good1 = Goods('iphone', 2, 8000)
        self.good2 = Goods('book', 8, 60)
        self.good3 = Goods('cosmetics', 5, 500)



        print("方法测试开始")
    def teardown_method(self):
        print("方法测试结束")

    @pytest.mark.parametrize("good, expected_message",
                             [(lambda self: self.good1, '商品iphone已添加'),
                              (lambda self: self.good2, '商品book已添加'),
                              (lambda self: self.good3, '商品cosmetics已添加')],
                             ids=['iphone', 'book','cosmetics'])
    def test_add_good(self, good, expected_message):
        # 添加商品并进行断言
        result = self.cart1.add_good(good(self))  # 调用 lambda 函数获取 good
        assert result == expected_message
    @pytest.mark.parametrize("good_name,excepted_message",
                             [('iphone','商品 iphone 信息为：数量：2 单价：8000 总价： 16000'),
                              ('book', '商品 book 信息为：数量：8 单价：60 总价： 480'),
                              ('cosmetics', '商品 cosmetics 信息为：数量：5 单价：500 总价： 2500')
                              ],ids=['iphone', 'book','cosmetics'])
    def test_goods_info(self,good_name,excepted_message):
        # 添加商品到购物车
        self.cart1.goods_list=[]
        self.cart1.add_good(self.good1)
        self.cart1.add_good(self.good2)
        self.cart1.add_good(self.good3)

        result = self.cart1.goods_info(good_name)
        assert result == excepted_message

    @pytest.mark.parametrize("good_name,excepted_message",
                             [('iphone', '商品iphone信息已从购物车删除'),
                              ('book', '商品book信息已从购物车删除'),
                              ('cosmetics', '商品cosmetics信息已从购物车删除')
                              ], ids=['iphone', 'book', 'cosmetics'])
    def test_del_good(self,good_name,excepted_message):
        # 添加商品到购物车
        self.cart1.goods_list = []
        self.cart1.add_good(self.good1)
        self.cart1.add_good(self.good2)
        self.cart1.add_good(self.good3)

        result = self.cart1.del_good(good_name)
        assert result == excepted_message
    def test_settle_account(self):
        # 添加商品到购物车
        self.cart1.goods_list = []
        self.cart1.add_good(self.good1)
        self.cart1.add_good(self.good2)
        self.cart1.add_good(self.good3)
        assert self.cart1.settle_accounts() == "购物车总账单为18980"






















