class InventoryFileManager:
    def __init__(self, filename):
        self.filename = filename

    def read_inventory(self):
        '''
        读取库存文件并返回字典
        :return: 库存信息（字典）
        '''
        try:
            with open(self.filename, "r") as file:
                file_lines = file.readlines()
                inventory = {}
                for line in file_lines:
                    name, stock = line.strip().split(",")
                    inventory[name] = int(stock)
                return inventory
        except FileNotFoundError:
            print("库存文件不存在，系统将自动创建一个新文件。")
            with open(self.filename, "w") as file:
                pass
            return {}
        except ValueError:
            print("文件内容格式错误，请检查！")
            return {}

    def write_inventory(self, inventory):
        '''
        将库存数据写入文件
        :param inventory: 库存信息（字典）
        '''
        try:
            with open(self.filename, "w") as file:
                for name, stock in inventory.items():
                    file.write(f"{name},{stock}\n")
        except Exception as e:
            print(f"写入文件时发生错误：{e}")