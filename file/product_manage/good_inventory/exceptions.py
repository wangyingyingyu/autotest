class ProductNotFoundError(Exception):
    '''
    自定义异常：商品未找到
    '''
    def __init__(self, message="商品未找到！"):
        super().__init__(message)
        self.message = message



