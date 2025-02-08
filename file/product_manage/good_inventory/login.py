from file_operations import InventoryFileManager
from inventory_operations import InventoryManager


def login():
    # 预定义的用户名和密码
    manage_name = "aaa"
    password = "123"

    # 最大尝试次数
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        # 用户输入用户名和密码
        username = input("请输入用户名: ")
        password = input("请输入密码: ")
        # 验证用户名和密码
        if username == manage_name and password == password:
            print("登录成功")
            break
        else:
            attempts += 1
            print(f"登录失败! 你还有 {max_attempts - attempts} 次机会。")
    if attempts == max_attempts:
        print("登录失败，已超出最大尝试次数。")




def main():
    # 初始化文件名
    filename = "inventory.txt"
    # 创建文件管理器并读取库存
    file_manager = InventoryFileManager(filename)
    inventory = file_manager.read_inventory()

    # 创建库存管理器
    inventory_manager = InventoryManager(inventory)

    while True:
        print("\n请选择操作：")
        print("1. 登录：")
        print("2. 查询库存")
        print("3. 修改库存")
        print("4. 添加新商品")
        print("5. 退出系统")
        choice = input("请输入操作编号：")

        if choice == "2":
            inventory_manager.query_inventory()
        elif choice == "1":
            login()
        elif choice == "3":
            product_name = input("请输入商品名称：")
            try:
                new_stock = int(input("请输入新的库存数量："))
                inventory_manager.update_stock(product_name, new_stock)
            except ValueError:
                print("输入无效！库存数量必须是整数。")
        elif choice == "4":
            product_name = input("请输入新商品名称：")
            try:
                stock = int(input("请输入库存数量："))
                inventory_manager.add_product(product_name, stock)
            except ValueError:
                print("输入无效！库存数量必须是整数。")
        elif choice == "5":
            file_manager.write_inventory(inventory_manager.inventory)
            print("退出系统，再见！")
            break
        else:
            print("无效输入，请重新选择！")
