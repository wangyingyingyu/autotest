import pytest

from week4_day4.src.bank_system import BankAccount
"""def setup_module():
    print("模块测试开始")
def teardown_module():
    print("模块测试结束")
class TestBankAccount:
    def setup_class(self):
        self.bank_account = BankAccount()

    def teardown_class(self):
        print("类测试结束")

    # 每个类里面的测试方法前后分别执行 setup teardown
    def setup_method(self):
        print("TestDemo setup")

    def teardown_method(self):
        print("TestDemo teardown")

    def test_deposit(self):
        assert self.bank_account.deposit(30)

    def test_withdraw(self):
        assert self.bank_account.withdraw(10)

    def test_get_balance(self):
        assert self.bank_account.get_balance()

    def test_transfer(self):
        assert self.bank_account.transfer(15)"""


def setup_module():
    print("模块测试开始")

def teardown_module():
    print("模块测试结束")

class TestBankAccount:
    def setup_class(self):

        print("类测试开始")

    def teardown_class(self):
        print("类测试结束")

    def setup_method(self):
        self.bank_account = BankAccount()
        print("方法测试开始")

    def teardown_method(self):
        print("方法测试结束")

    # def test_deposit(self):
    #     assert self.bank_account.deposit(30) == 30  # 余额为30
    #
    # def test_withdraw(self):
    #     #self.bank_account.deposit(30)  # 确保有余额
    #     assert self.bank_account.withdraw(10) == 20  # 余额应为20
    #
    # def test_get_balance(self):
    #     # self.bank_account.deposit(30)  # 确保有余额
    #     assert self.bank_account.get_balance() == 20  # 余额应为30
    #
    # def test_transfer(self):
    #     #self.bank_account.deposit(30)
    #     assert self.bank_account.transfer(15) == 5  # 余额应为15
    @pytest.mark.parametrize("amount, expected_balance", [(30, 30), (50, 50), (100, 100)],
                             ids=['first:30', 'second:50', 'third:100'])
    def test_deposit(self, amount, expected_balance):
        assert self.bank_account.deposit(amount) == expected_balance  # 验证存款后余额

    @pytest.mark.parametrize("deposit_amount, withdraw_amount, expected_balance",
                             [(30, 10, 20), (30, 30, 0), (50, 20, 30)],
                             ids=['first:30 to 10', 'second:30 to 30', 'third:50 to 20'])
    def test_withdraw(self, deposit_amount, withdraw_amount, expected_balance):
        self.bank_account.deposit(deposit_amount)  # 存款确保余额
        assert self.bank_account.withdraw(withdraw_amount) == expected_balance  # 检查余额

    def test_get_balance(self):
        self.bank_account.deposit(30)  # 确保有余额
        assert self.bank_account.get_balance() == 30  # 余额应为30

    @pytest.mark.parametrize("deposit_amount, transfer_amount, expected_balance_a, expected_balance_b", [
        (30, 10, 20, 10),
        (50, 50, 0, 50),
        (100, 100, 0, 100)
    ],
                             ids=['first:30 to 10', 'second:50 to 50', 'third:100 to 100'])
    def test_transfer(self, deposit_amount, transfer_amount, expected_balance_a, expected_balance_b):
        self.bank_account.deposit(deposit_amount)  # 存款确保余额
        assert self.bank_account.transfer(transfer_amount) == expected_balance_a  # 检查账户a余额
        assert self.bank_account.bank2 == expected_balance_b  # 检查账户b余额





