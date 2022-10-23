class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.price

    def set_price(self, value):
        if value < 0:
            raise ValueError('Price cannot be negative.')

product = Product(-50)