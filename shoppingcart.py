class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)

    def show(self):
        print(f" you have {self.items} in your cart.")


cart = ShoppingCart()

cart.add("big ahh car")
cart.add("small ahh tractor")
cart.add("milk")

cart.show()

cart.remove("big ahh car")
cart.remove("milk")

cart.show()
