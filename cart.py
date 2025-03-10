class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        """Dodaje proizvod u korpu."""
        self.cart_items.append(product)
        print(f"Proizvod {product.name} dodat u korpu.")

    def total_price(self):
        """Izračunava ukupnu vrednost proizvoda u korpi."""
        return sum(product.price for product in self.cart_items)

    def show_cart(self):
        """Prikazuje sadržaj korpe."""
        if not self.cart_items:
            print("Korpa je prazna.")
        else:
            print("Sadržaj korpe:")
            for product in self.cart_items:
                print(f"- {product.name} ({product.price} RSD)")
            print(f"Ukupna cena: {self.total_price()} RSD")