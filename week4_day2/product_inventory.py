import yaml
"""实战：商品库存管理系统
开发一个简单的商品库存管理系统，管理员可以查询商品的库存数量，修改库存值，并添加新的商品记录。
为了确保系统的稳定性，需要对输入异常、文件操作异常等进行处理，避免因用户输入错误或文件丢失导致系统崩溃。
查询商品库存：从文件中读取商品库存数据并展示。
修改商品库存：根据商品名称修改库存数量。
添加新商品：向文件中添加新的商品记录。
捕获用户输入错误（如输入非数字时的类型异常）。
捕获文件读写错误。
捕获商品名称不存在的自定义异常。"""
import os
# 读取库存文件 文件异常处理
def read_inventory(file_name):
    try:
        if not os.path.exists(file_name):
            with open(file_name,'w',encoding='utf-8'):
                pass
            return f'文件不存在，创建库存文件{file_name}'
        else:
            with open(file_name,'r',encoding='utf-8') as file:
                return yaml.safe_load(file) or {}
    except Exception as e:
        print("文件不能读取",{e})

def write_inventory(file_name, data):
    try:
        with open(file_name, "w", encoding='utf-8') as file:
            yaml.safe_dump(data, file, allow_unicode=True)
    except Exception as e:
        print("文件不能写入", e)

def query_inventory(file_name):
    name = input("输入查询的商品名称:")
    datas = read_inventory(file_name)
    if name in datas:
        print(f"商品{name}的库存信息为{datas[name]}")
    else:
        print('库存中没有该商品')


# 添加新商品
def  add_product(file_name):

    product_name = input("输入商品名称")

    try:
        product_num = int(input("输入商品库存数量："))
        inventory_data = read_inventory(file_name)
        if product_name in read_inventory(file_name):
            print("商品在库存中已存在")
        else:
            inventory_data[product_name] = product_num
            write_inventory(file_name, inventory_data)
            print(f"商品{product_name}已添加到库存")
    except ValueError:
        print(f'库存数量为整数')

# 修改库存
def update_stock(file_name):
    inventory_data = read_inventory(file_name)
    product_name = input("输入要修改的商品名称：")
    if product_name in inventory_data:
        try:
            product_num = int(input("输入商品库存数量："))
            inventory_data[product_name] = product_num
            write_inventory(file_name, inventory_data)
            print(f'{product_name}库存信息已更新')
        except ValueError as error:
            print("商品库存为整数",error)
    else:
        try:
            product_num = int(input("输入商品库存数量："))
            inventory_data[product_name] = product_num
            write_inventory(file_name, inventory_data)
            print(f'{product_name}没有库存信息，重新添加')
        except Exception as error:
            print("商品库存为整数", error)


def inventory_management_system():

    filename = "inventory.yaml"

    while True:
        read_inventory(filename)
        print("\n请选择操作：")
        print("1. 读取库存文件")
        print("2. 查询库存")
        print("3. 修改库存")
        print("4. 添加新商品")
        print("5. 退出系统")
        choice = input("请输入操作编号：")
        if choice == "1":
            print(read_inventory(filename))

        elif choice == "2":
            query_inventory(filename)

        elif choice == "3":
            update_stock(filename)

        elif choice == "4":
            add_product(filename)
        elif choice == "5":
            print("退出系统，再见！")
            break
        else:
            print("无效输入，请重新选择！")


# 主程序入口
if __name__ == "__main__":
    inventory_management_system()







