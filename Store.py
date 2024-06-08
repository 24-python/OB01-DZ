# Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики, такие как адрес, название и ассортимент товаров. Ваша задача — создать класс `Store`, который можно будет использовать для создания различных магазинов.
# # Шаги:
# 1. Создай класс `Store`:
# -Атрибуты класса:
# - `name`: название магазина.
# - `address`: адрес магазина.
# - `items`: словарь, где ключ - название товара, а значение - его цена. Например, `{'apples': 0.5, 'bananas': 0.75}`.
# - Методы класса:
# - `__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для `items`.
# -  метод для добавления товара в ассортимент.
# - метод для удаления товара из ассортимента.
# - метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.
# - метод для обновления цены товара.


class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f'Товар {item_name} добавлен в ассортимент {self.name}')

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f'Товар {item_name} удален из ассортимента {self.name}')

    def get_price(self, item_name):
        if item_name in self.items:
            return self.items[item_name]
        return None

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f'Цена {item_name} обновлена в ассортименте {self.name}')
        else:
            print(f'Товар {item_name} отсутствует в ассортименте {self.name}')

store1 = Store('Командор', 'ул. Пушкина, 1')
store2 = Store('Красный яр', 'ул. Ленина, 2')
store3 = Store('Калина-малина', 'ул. Гоголя, 3')

store1.add_item('яблоки', 150)
store1.add_item('бананы', 124)
store1.add_item('молоко', 100)

store1.remove_item('яблоки')
store1.remove_item('бананы')

print(store1.get_price('молоко'))

store1.update_price('яблоки', 145)
store1.update_price('бананы', 125)
store1.update_price('молоко', 120)