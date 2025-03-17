from web_auto_test.po1.page.main_page import MainPage


class TestContacts:

    def setup_class(self):
        main_page = MainPage()
        self.contacts_page = main_page.goto_contacts()

    def test_add_save(self):
        res = self.contacts_page.add_contacts_save()
        assert res == '保存成功'

    def test_add_not_save(self):
        res = self.contacts_page.add_contacts_not_save()
        assert res == '成员的资料尚未保存，确定要离开吗？'