from hogwarts_function_utils.order_manager.controller.order_controller import OrderController

import sys
import os

from hogwarts_function_utils.order_manager.view.order_manager_ui import OrderManagerUI


def main():
    ui = OrderManagerUI()
    ui.main_ui()


if __name__ == '__main__':
    main()
