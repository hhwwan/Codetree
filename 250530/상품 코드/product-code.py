product_name, product_code = input().split()
product_code = int(product_code)

class product:
    def __init__(self, name='codetree', code=50):
        self.n = name
        self.c = code

product1 = product()
print('product', product1.c, 'is', product1.n)

product2 = product(product_name, product_code)
print('product', product2.c, 'is', product2.n)