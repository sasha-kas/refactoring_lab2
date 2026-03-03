DISCOUNT_PUPPY = 0.2
DISCOUNT_SENIOR = 0.15
BONUS_THRESHOLD = 1000
BONUS_AMOUNT = 100
VALID_SIZES = ["S", "M", "L"]

class DogStore:
    def __init__(self):
        self.products = []
        self.total_money = 0
    def add_food(self, name, price, weight):
        if self._is_valid_price(price) and weight > 0:
            self._add_product("food", name, price, weight=weight)
    def add_toy(self, name, price, size):
        if self._is_valid_price(price) and size in VALID_SIZES:
            self._add_product("toy", name, price, size=size)

    def _add_product(self, product_type, name, price, **kwargs):
        product = {
            "type": product_type,
            "name": name,
            "price": price
        }
        product.update(kwargs)
        self.products.append(product)

    def _is_valid_price(self, price):
        return price > 0

    def checkout(self, age):
        total = self._calculate_total()
        total = self._apply_discount(total, age)
        total = self._apply_bonus(total)
        self.total_money += total
        self.products.clear()
        return total

    def _calculate_total(self):
        return sum(product["price"] for product in self.products)
    def _apply_discount(self, total, age):
        discount = self._calculate_discount(age)
        return total - (total * discount)
    def _calculate_discount(self, age):
        if age < 1:
            return DISCOUNT_PUPPY
        if age > 10:
            return DISCOUNT_SENIOR
        return 0
    def _apply_bonus(self, total):
        if total > BONUS_THRESHOLD:
            return total - BONUS_AMOUNT
        return total
    def get_dog_category(self, age):
        if age < 1:
            return "puppy"
        if age <= 7:
            return "adult"
        return "senior"