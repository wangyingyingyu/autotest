import pytest
from exam_2_15.src.inventory_system import Product, Inventory

@pytest.fixture(scope='class')
def get_add_data():
    product1 = Product()
    product1.add_product('a', 1, 3)
    product1.add_product('b', 2, 4)
    product1.add_product('c', 3, 5)
    yield product1  # Yield 让夹具在测试之后进行清理（如果需要）

@pytest.fixture(scope='class')
def get_add_order():

    inventory1 = Inventory()
    inventory1.add_order('a', 3)
    inventory1.add_order('b', 3)
    yield inventory1  # Yield 使得也能在测试使用后分享实例



