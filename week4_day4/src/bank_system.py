"""实战：银行账户系统
设计一个银行账户系统 BankAccount 类，支持以下基本功能
存款 (deposit)：向账户中存入指定金额。
取款 (withdraw)：从账户中提取指定金额，且取款金额不能超过账户余额。
获取余额 (get_balance)：获取当前账户的余额。
转账 (transfer)：从当前账户向另一个账户转账，转账金额不能超过账户余额。
使用 Pytest 测试框架进行单元测试
测试存款、取款、获取余额、转账方法的正确性。
配置测试环境的初始化和清理。"""
"""
class BankAccount:
    def __init__(self):
        self.bank= 0
        self.bank2 = 0


    def deposit(self,crash):
        self.bank +=crash
        print(f"存储了{crash}元")


    def withdraw(self,crash):
        if crash > self.bank:
            print("取款金额超过了账户余额")
        else:
            self.bank -= crash
            print(f"提取了{crash}元")

    def get_balance(self):
        print(f"当前账户余额为{self.bank}")

    def transfer(self,crash):
        if crash > self.bank:
            print("取款金额超过了账户余额")
        else:
            self.bank -= crash
            self.bank2 += crash
            print(f"账户a向账户b转账了{crash}元")

c = BankAccount()
c.deposit(30)
c.get_balance()
c.withdraw(10)
c.transfer(15)
"""

class BankAccount:
    def __init__(self):
        self.bank = 0
        self.bank2 = 0

    def deposit(self, amount):
        self.bank += amount
        print(f"存储了{amount}元")
        return self.bank  # 返回当前余额

    def withdraw(self, amount):
        if amount > self.bank:
            print("取款金额超过了账户余额")
            return None
        else:
            self.bank -= amount
            print(f"提取了{amount}元")
            return self.bank  # 返回当前余额

    def get_balance(self):
        print(f"当前账户余额为{self.bank}")
        return self.bank  # 返回当前余额

    def transfer(self, amount):
        if amount > self.bank:
            print("取款金额超过了账户余额")
            return None
        else:
            self.bank -= amount
            self.bank2 += amount
            print(f"账户a向账户b转账了{amount}元")
            return self.bank  # 返回当前余额