from product import Product
from product_manager import ProductManager
from cart import Cart

# Kreiranje ProductManager instance
manager = ProductManager()

# Dodavanje proizvoda
product1 = Product("Telefon", 50000, 5)
product2 = Product("Laptop", 120000, 3)
product3 = Product("Miš", 3000, 10)
product4 = Product("Tastatura", 5000, 20)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

# Prikaz proizvoda i ukupne vrednosti
print(manager.display_products())
print(f"Ukupna vrednost inventara: {manager.total_value()} RSD")

# Prikaz dostupnih proizvoda
manager.display_products()

# Kreiranje instance korpe
cart = Cart()

# Dodavanje nasumičnih proizvoda u korpu
cart.add_to_cart(manager.products[0])
cart.add_to_cart(manager.products[2])
cart.add_to_cart(manager.products[1])

# Prikaz korpe
cart.show_cart()