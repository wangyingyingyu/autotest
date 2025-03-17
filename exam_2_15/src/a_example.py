class Product:
    products = []

    # 添加商品，如果商品存在，增加库存，单价不同，修改单价、库存

    def add_product(self,name,price,num):
        product_dict = {}
        for i in Product.products:
            if i['name'] == name:
                if i['price'] != price:
                    i['price'] = price
                    i['num'] = num
                    print('修改库存数量')
                    return '修改单价和库存数量'
                else:
                    i['num'] += num
                    print('修改库存数量')
                    return '修改库存数量'
        else:
            product_dict['name'] = name
            product_dict['price'] = price
            product_dict['num'] = num
            Product.products.append(product_dict)

            print('添加商品')
            return '添加商品'


import yaml
data = [('a',1,3,'添加商品'),('b',2,4,'添加商品'),('c',3,5,'添加商品')]
with open('../data/product_data.yaml', 'w',encoding='utf-8') as file:
    yaml.safe_dump(data, file)


def get_product():
    with open('../data/product_data.yaml', 'r',encoding='utf-8') as file:
        return yaml.safe_load(file)
print(get_product())








