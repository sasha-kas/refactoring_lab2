class DogStore:

    def __init__(self):
        self.products = []
        self.total_money = 0

    def add_food(self, name, price, weight):
        # дублювання перевірок
        if price > 0:
            if weight > 0:
                product = {
                    "type": "food",
                    "name": name,
                    "price": price,
                    "weight": weight
                }
                self.products.append(product)

    def add_toy(self, name, price, size):
        # дублювання перевірок
        if price > 0:
            if size == "S" or size == "M" or size == "L":
                product = {
                    "type": "toy",
                    "name": name,
                    "price": price,
                    "size": size
                }
                self.products.append(product)

    def checkout(self, age):
        # ДОВГИЙ МЕТОД (все в одному місці)
        total = 0

        # підрахунок суми
        for product in self.products:
            total += product["price"]

        # розрахунок знижки
        if age < 1:
            discount = 0.2
        elif age > 10:
            discount = 0.15
        else:
            discount = 0

        total = total - (total * discount)

        # бонус (магічні числа)
        if total > 1000:
            total = total - 100

        # оновлення грошей магазину
        self.total_money = self.total_money + total

        # очищення кошика
        self.products = []

        return total

    def get_dog_category(self, age):
        if age < 1:
            return "puppy"
        if age >= 1 and age <= 7:
            return "adult"
        if age > 7:
            return "senior"