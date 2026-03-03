import pytest
from lab2_first import DogStore


def test_add_food_valid():
    """Перевіряю, що якщо передати правильну ціну і вагу, то корм реально додається в список товарів"""
    # Підготовка: створюю магазин
    store = DogStore()

    # Дія: додаю корм
    store.add_food("Meat", 200, 1)

    # Перевірка: товар має з’явитися в списку
    assert len(store.products) == 1


def test_add_food_invalid_price():
    """Перевіряю, що корм з від’ємною ціною не додається """
    # Підготовка
    store = DogStore()

    # Дія: пробую додати корм з неправильною ціною
    store.add_food("Meat", -10, 1)

    # Перевірка: список має залишитися порожнім
    assert len(store.products) == 0


def test_add_toy_valid():
    """Перевіряю, що іграшка з допустимим розміром додається"""
    store = DogStore()

    store.add_toy("Ball", 100, "M")

    assert len(store.products) == 1


def test_add_toy_invalid_size():
    """Перевіряю, що іграшка з недопустимим розміром не додається """
    store = DogStore()

    store.add_toy("Ball", 100, "XL")

    assert len(store.products) == 0


def test_puppy_discount():
    """Перевіряю, що для цуценяти (малютка менше 1 року)застосовується знижка 20%"""
    store = DogStore()
    store.add_food("Meat", 1000, 1)

    total = store.checkout(0.5)

    assert total == 800


def test_senior_discount():
    """Перевіряю, що для старої собаки (більше 10 років)застосовується знижка 15%"""
    store = DogStore()
    store.add_food("Meat", 1000, 1)

    total = store.checkout(12)

    assert total == 850


def test_bonus_discount():
    """Перевіряю, що якщо сума більша за 1000,то додатково віднімається 100 грн"""
    store = DogStore()
    store.add_food("Meat", 1200, 1)

    total = store.checkout(5)

    assert total == 1100


def test_total_money_updates():
    """Перевіряю, що після покупки гроші додаються до загального прибутку магазину"""
    store = DogStore()
    store.add_food("Meat", 200, 1)

    store.checkout(5)

    assert store.total_money == 200


def test_products_cleared_after_checkout():
    """Перевіряю, що після оформлення покупки кошик очищується"""
    store = DogStore()
    store.add_food("Meat", 200, 1)

    store.checkout(5)

    assert len(store.products) == 0


def test_dog_category():
    """Перевіряю, що категорія собаки правильно визначається за віком"""
    store = DogStore()

    assert store.get_dog_category(0.5) == "puppy"
    assert store.get_dog_category(5) == "adult"
    assert store.get_dog_category(9) == "senior"