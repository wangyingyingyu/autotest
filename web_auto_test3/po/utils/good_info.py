# 定义商品名称列表
# strings = [
#     "阳光玫瑰",
#     "阳光玫瑰",
#     "菠萝",
#     "郁金香",
#     "玫瑰",
#     "月季",
#     "菠萝蜜",
#     "杨桃",
#     "草莓",
#     "砂糖桔"
# ]
strings = ["阳光玫瑰"]
# 初始化全局索引
current_index = 0

def get_name():
    global current_index  # 声明使用全局变量

    # 获取当前索引的字符串
    name = strings[current_index]

    # 更新索引，若到达列表末尾则重置为0
    # current_index = (current_index + 1) % len(strings)

    return name
print(get_name())
print(get_name())
print(get_name())
#strings_ID = ['001','002','003','004','005','006','007','008','009','010']
strings_ID = ['001']
def get_ID():
    global current_index  # 声明使用全局变量

    # 获取当前索引的字符串
    id = strings_ID[current_index]

    # 更新索引，若到达列表末尾则重置为0
    # current_index = (current_index + 1) % len(strings_ID)

    return id
print(get_ID())
print(get_ID())
print(get_ID())
#strings_price = ['1','2','3','04','5','6','7','8','9','10']
strings_price = ['1']
def get_price():
    global current_index  # 声明使用全局变量

    # 获取当前索引的字符串
    price = strings_price[current_index]

    # 更新索引，若到达列表末尾则重置为0
    # current_index = (current_index + 1) % len(strings_price)

    return price
# strings_quantity = ['11','22','33','44','55','66','77','88','99','100']
strings_quantity = ['11']
def get_quantity():
    global current_index  # 声明使用全局变量

    # 获取当前索引的字符串
    quantity = strings_quantity[current_index]

    # 更新索引，若到达列表末尾则重置为0
    # current_index = (current_index + 1) % len(strings_quantity)

    return quantity











"""
class ProductSelector:
    def __init__(self, strings):
        self.strings = strings
        self.current_index = 0

    def get_name(self):
        # 获取当前索引的字符串
        name = self.strings[self.current_index]
        # 更新索引，若到达列表末尾则重置为0
        self.current_index = (self.current_index + 1) % len(self.strings)
        return name

# 定义商品名称列表
strings = [
    "香蕉",
    "苹果",
    "菠萝",
    "郁金香",
    "玫瑰",
    "月季",
    "菠萝蜜",
    "杨桃",
    "草莓",
    "砂糖桔"
]

# 创建ProductSelector对象
product_selector = ProductSelector(strings)"""