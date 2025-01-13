"""实战：房子家具管理系统
编写一个 Python 程序：
房子有户型，总面积和家具名称列表，新房子没有任何的家具。
家具有名字和占地面积，其中
床：占 4 平米
衣柜：占 2 平米
餐桌：占 1.5 平米
将以上三件家具添加到房子中
打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
"""


#定义房子类
class Home:
    def __init__(self,type,space):

        self.type = type
        self.space = space
        self.furniture_list = []
        self.useful_space = space  # 剩余面积初始化为总面积
    #将 三件家具 添加到房子中
    def add_furniture(self,furniture):
        if self.useful_space >= furniture.area:  # 判断剩余面积是否足够
            self.furniture_list.append(furniture)  # 添加家具到家具列表
            self.useful_space -= furniture.area  # 更新剩余面积
            print(f"{furniture.name}已添加到房子中")
        else:
            print(f"房子剩余面积不足，无法添加{furniture.name}")
    def display_info(self):

        print("户型:", self.type)

        print("总面积:", self.space, "平米")

        print("剩余面积:", self.useful_space, "平米")

        print("家具名称列表:")
        for furniture in self.furniture_list:# 循环遍历家具列表my_house = House("两室一厅", 100)
            print(furniture.name)

class Furniture:
    def __init__(self,name,area):
        self.name = name
        self.area = area
    # def __str__(self):
    #     return f'Furniture{self.name},area{self.area}'


# 创建房子对象 实例化home类
my_house = Home("两室一厅", 100)

# 创建家具对象
bed = Furniture("床", 4)
wardrobe = Furniture("衣柜", 2)
table = Furniture("餐桌", 1.5)

# 添加家具到房子中
my_house.add_furniture(bed)
my_house.add_furniture(wardrobe)
my_house.add_furniture(table)

# 打印房子信息
my_house.display_info()














