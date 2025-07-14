# Base class representing a generic shopping cart
class ShoppingCart:
    def _init_(self):
        self.items = []  # List to store (item_name, quantity, unit_price)

    def add_item(self, item_name: str, qty: int, unit_price: float):
        self.items.append((item_name, qty, unit_price))

    def remove_item(self, item_name: str):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def calculate_total(self) -> float:
        # Calculates total price without any discounts or taxes
        total = 0.0
        for name, qty, price in self.items:
            total += qty * price
        return total

    def cart_contents(self):
        # Prints the cart contents and subtotal
        print("Cart Contents:")
        for name, qty, price in self.items:
            print(f"  {name}:- {qty} @ Ksh {price:.2f} each")
        print(f"Total: Ksh {self.calculate_total():.2f}\n")


# Subclass that applies a discount
class DicountedCart(ShoppingCart):
    def _init_(self, discount_rate: float):
        super()._init_()
        self.discount_rate = discount_rate  # e.g., 0.15 for 15%

    def calculate_total(self) -> float:
        # Overrides base method to apply a discount
        initial_total = super().calculate_total()
        discount = initial_total * self.discount_rate
        return initial_total - discount


# Subclass that applies a tax
class TaxedCart(ShoppingCart):
    def _init_(self, tax_rate: float):
        super()._init_()
        self.tax_rate = tax_rate  # e.g., 0.12 for 12%

    def calculate_total(self) -> float:
        # Overrides base method to apply tax
        initial_total = super().calculate_total()
        tax = initial_total * self.tax_rate
        return initial_total + tax


# Polymorphic function: works with any ShoppingCart type
def checkout(cart: ShoppingCart):
    cart.cart_contents()
    print(f"Total amount: Ksh {cart.calculate_total():.3f}\n")


# Main execution block
if __name__ == "_main_":
    # Regular cart: no tax or discount
    obj_cart = ShoppingCart()
    obj_cart.add_item("Papaya", 76, 6.20)
    obj_cart.add_item("Orange", 96, 11.50)
    obj_cart.add_item("Kiwi", 85, 9.60)
    print(">>> Ordinary Cart Without Tax & Discount <<<")
    checkout(obj_cart)

    # Discounted cart: 15% discount applied
    disc_cart = DicountedCart(discount_rate=0.15)
    disc_cart.add_item("Papaya", 76, 6.20)
    disc_cart.add_item("Orange", 96, 11.50)
    disc_cart.add_item("Kiwi", 85, 9.60)
    print(">>> Applying a 15% Discount <<<")
    checkout(disc_cart)

    # Taxed cart: 12% tax applied
    taxed_cart = TaxedCart(tax_rate=0.12)
    taxed_cart.add_item("Papaya", 5, 2.00)
    taxed_cart.add_item("Orange", 96, 11.50)
    taxed_cart.add_item("Kiwi", 3, 1.50)
    print(">>> Applying a 12% Tax <<<")
    checkout(taxed_cart)