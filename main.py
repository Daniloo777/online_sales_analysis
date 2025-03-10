from product import Product
from product_manager import ProductManager

# Kreiranje ProductManager instance
manager = ProductManager()

# Dodavanje proizvoda
product1 = Product("Telefon", 50000, 5)
product2 = Product("Laptop", 120000, 3)
product3 = Product("Miš", 3000, 10)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

# Prikaz proizvoda i ukupne vrednosti
print(manager.display_products())
print(f"Ukupna vrednost inventara: {manager.total_value()} RSD")