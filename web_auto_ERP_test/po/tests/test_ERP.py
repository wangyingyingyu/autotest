from web_auto_ERP_test.po.page.login import Login

class TestERP:
    def setup_class(self):
        self.log_in = Login()
        self.wait_send_page = self.log_in.login().main_page().order_create()
        self.wait_send_page.wait_sent()
    def test_text(self):
        texts = self.wait_send_page.get_text()
        assert texts == '共更新1条记录，全部成功'


