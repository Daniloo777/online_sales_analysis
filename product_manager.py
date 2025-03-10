from product import Product

class ProductManager:
    
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        if not self.products:
            return "Nema dostupnih proizvoda."
        return "\n".join(product.display_info() for product in self.products)

    def total_value(self):
        return sum(product.price * product.quantity for product in self.products)
