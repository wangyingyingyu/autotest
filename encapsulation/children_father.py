"""
父类的私有属性和私有方法（以双下划线`__`开头）不能被子类直接访问，甚至使用`super()`函数也不行。
`super()`主要用于调用父类的公有和保护成员，但不能直接访问私有成员。
虽然不能直接使用`super()`访问父类的私有属性和方法，您仍然可以通过父类提供的公有方法来间接使用这些私有成员。
"""
# 示例：使用公有方法间接访问父类的私有属性和方法

class Parent:
    def __init__(self):
        self.__private_var = "这是私有变量"

    def __private_method(self):
        return "这是私有方法"

    def get_private_var(self):
        return self.__private_var

    def call_private_method(self):
        return self.__private_method()


class Child(Parent):
    def show_parent_private(self):
        # 使用 super() 调用父类的公有方法
        private_var = super().get_private_var()
        private_method_result = super().call_private_method()
        print(f"父类的私有变量: {private_var}")
        print(f"父类的私有方法结果: {private_method_result}")


# 测试代码
if __name__ == "__main__":
    child = Child()
    child.show_parent_private()
"""
### 代码解释
1. ** 父类`Parent` **：- 具有一个私有属性`__private_var`和一个私有方法`__private_method`。
- 提供公有方法`get_private_var`和`call_private_method`，使得子类可以访问私有成员的值和结果。

2. ** 子类`Child` **：- 在`show_parent_private`方法中，使用`super()`调用父类的公有方法`get_private_var`
和`call_private_method`。通过这些公有方法来间接访问父类的私有属性和方法。
"""