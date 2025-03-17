import pytest
import yaml

from exam_2_15.src.inventory_system import Inventory,Product
"""
测试目标：

编写 Pytest 测试用例，测试库存管理、订单管理和物流管理模块。
使用 Pytest 标记测试用例，组织测试顺序。
测试异常处理，包括库存不足和无效订单等情况。
使用 fixture 管理测试资源，模拟系统初始化。
使用 Pytest 配置文件配置全局选项。
使用 pytest.mark.parametrize 实现数据驱动，测试不同商品信息查询的场景。"""
def setup_module():
    print('信息管理打开')
def teardown_module():
    print('管理系统关闭')

def get_product():
    with open('../data/product_data.yaml', 'r',encoding='utf-8') as file:
        return yaml.safe_load(file)



class TestInventory:
    def setup_class(self):
        print("类测试开始")
    def teardown_class(self):
        print('类测试结束')
    def setup_method(self):
        self.product = Product()
        self.inventory = Inventory()
        print("方法测试开始")
    def teardown_method(self):
        print("方法测试结束")
    @pytest.mark.add_product
    @pytest.mark.parametrize('name,price,num,expected',get_product(),ids=['a','b','c'])
    def test_add_product(self,name,price,num,expected):
        assert self.product.add_product(name,price,num) == expected


    #@pytest.mark.run(order = 1)
    @pytest.mark.check_ptoduct
    @pytest.mark.parametrize('name,expected',[("a","商品存在"),("b","商品存在"),("c","商品存在")],ids=['a','b','c'])
    def test_check_product(self,get_add_data,name,expected):
        assert get_add_data.check_product(name) == expected

    @pytest.mark.add_order
    @pytest.mark.parametrize('name,num,expected',[("a",1,"订单成功"),("b",6,"按库存数量发货"),("d",2,"订单失败:库存中没有该商品")],
                             ids=['a','b','c'])
    def test_add_order(self,get_add_data,name,num,expected):
        assert self.inventory.add_order(name,num) == expected

    @pytest.mark.flow
    @pytest.mark.parametrize("id_name,expected",[('000','查询成功'),('001','查询成功')],
                             ids=['a','b'])
    def test_flow(self,get_add_data,get_add_order,id_name,expected):
        print("订单的ID:", [i[0][0] for i in get_add_order.inventory])  # 打印生成的订单ID
        assert get_add_order.check_flow(id_name) == expected