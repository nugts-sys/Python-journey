class ShoppingCart:
    def __init__ (self, items, prices):
        self.items = items
        self.prices = prices

    def total_price(self):
        total = 0

        for price in self.prices:
            total += price

        return total

cart = ShoppingCart(["milk","bread", "skyr" ], [5, 3, 2])

print(cart.total_price())