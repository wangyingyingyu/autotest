# 模块级别（优先最高）
def setup_module():
    print("资源准备：setup module")

def teardown_module():
    print("资源准备：teardown module")

# 函数级别
def setup_function():
    print("资源准备：setup function")

def teardown_function():
    print("资源销毁：teardown function")

def test_func1():
    assert True

class TestDemo:
    # 执行测试类前后分别执行 setup_class teardown_class
    def setup_class(self):
        print("TestDemo setup_class")

    def teardown_class(self):
        print("TestDemo teardown_class")

    # 每个类里面的测试方法前后分别执行 setup teardown
    def setup_method(self):
        print("TestDemo setup")

    def teardown_method(self):
        print("TestDemo teardown")

    def test_method1(self):
        assert True

    def test_method2(self):
        assert False
