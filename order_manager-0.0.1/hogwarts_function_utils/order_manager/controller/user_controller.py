from hogwarts_function_utils.order_manager.model.user import User


class UserController:

    def __init__(self):
        self.users = [
            User(username='admin', password='123'),
            User(username='seveniruby', password='456')
        ]
        self.login_user: User = None

    def login(self, user: User) -> bool:
        if user in self.users:
            self.login_user = user
            return True
        else:
            self.login_user = None
            return False
