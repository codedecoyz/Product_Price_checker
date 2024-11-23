import pandas as pd

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        return f"{self.name} - ${self.price} ({self.category})"

products = []

def add_product(name, price, category):
    product = Product(name, price, category)
    products.append(product)
