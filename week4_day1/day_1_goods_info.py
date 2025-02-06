import copy

# 添加销售记录
# 商品列表


def get_goods_name(goods):
    goods_name = []
    for i in goods:
        goods_name.append(i["product"])
    return goods_name

def add_sale(goods):
    # 用户输入产品信息
    good = {}
    good["product"] = input('输入产品名称：')
    good["quantity"] = int(input('输入销售数量：'))
    good["price"] = int(input('输入单价：'))
    goods.append(good)
    print(f'已将{good["product"]}添加到商品列表中')
    print(goods)
# 更新销售记录
def update(goods):
    # goods_name = []
    # for i in goods:
    #     goods_name.append(i["product"])
    product_name = input('输入产品名称')
    goods_name = get_goods_name(goods)
    if product_name in goods_name:
        # 输入新销售数量
        for good in goods:
            if product_name == good["product"]:
                good["quantity"] = int(input(f'输入产品{product_name}新销售数量：'))
                good["price"] = int(input(f'输入产品{product_name}新单价：'))
        print(goods)
    else:
        print(f'产品{product_name}不在销售列表内')
# 删除销售记录
def delete(goods):
    product_name = input('输入产品名称')
    goods_name = get_goods_name(goods)
    if product_name in goods_name:
        # 输入新销售数量
        for good in goods:
            if product_name == good["product"]:
                goods.remove(good)
        print(goods)
    else:
        print(f'产品{product_name}不在销售列表内')

# 统计销售数据
def count(goods):
    for good in goods:
        total_price = good["quantity"]*good["price"]
        good["total_price"] = total_price
    print(goods)
# 备份销售数据 深拷贝
def copy_goods(goods):
    type = input("请选择备份类型（shallow 或 deep）：")
    if type == 'shallow':
        copy_goods = copy.copy(goods)
        print("完成浅拷贝备份！")
        return copy_goods
    elif type == 'deep':
        deep_goods = copy.deepcopy(goods)
        print("完成深拷贝备份！")
        return deep_goods
    else:
        print("无效的备份类型！")



# 恢复销售数据 输入深拷贝函数调用变量
def restore(deep_data):
    if deep_data is None:
        print("当前没有备份可用！")
    else:
        goods = deep_data
        return goods


# 修改备份数据
def fix_goods(copy_data):
    print(copy_data)
    good_name = input('请输入要修改的产品名称：')
    #goods_name1 = get_goods_name(copy_data)

    for i in copy_data:
        if good_name == i["product"]:
            new_quantity = int(input("请输入备份数据的新销售数量："))
            i["quantity"] = new_quantity
            i["total_price"] = i["quantity"]*i["price"]
            print(f"备份数据中产品 {good_name} 的销售记录已修改！")
            print(copy_data)
            return
    print(f"未找到备份数据中产品 {good_name} 的记录！")
# 销售数据管理系统
def sales_management_system():
    '''
    销售数据管理系统
    :return:
    '''
    # 初始化销售数据
    goods = []
    # 初始化备份数据

    while True:
        print("\n请选择操作：")
        print("1. 添加销售记录")
        print("2. 更新销售记录")
        print("3. 删除销售记录")
        print("4. 统计销售数据")
        print("5. 备份销售数据")
        print("6. 恢复销售数据")
        print("7. 修改备份数据（观察浅拷贝与深拷贝）")
        print("8. 退出系统")
        choice = input("请输入操作编号：")

        if choice == "1":
            # 调用添加销售记录
            add_sale(goods)
        elif choice == "2":
            # 调用更新销售记录
            update(goods)
        elif choice == "3":
            # 调用删除销售记录
            delete(goods)
        elif choice == "4":
            # 调用统计销售数据
            count(goods)
        elif choice == "5":
            # 接受用户输入备份类型

            # 获取备份
            copy_data = copy_goods(goods)
        elif choice == "6":
            # 从备份回复数据
            goods = restore(copy_data)
        elif choice == "7":
            # 修改备份数据中的值，执行完通过 4 选项观察结果
            fix_goods(copy_data)
        elif choice == "8":
            print("退出系统，再见！")
            break
        else:
            print("无效输入，请重新选择！")

# 主程序
if __name__ == "__main__":
    sales_management_system()
