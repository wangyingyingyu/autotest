from hogwarts_function_utils.order_manager.view.login_ui import LoginUI


class OrderManagerUI:
    def __init__(self):
        self.user_ui = LoginUI()

    def main_ui(self):
        while True:
            menu = input("""
            1. login
            2. xxx
            3. fff
            4. xxx
            """)

            if menu == 1:
                self.user_ui.login_ui()
            elif menu == 2:
                ...
