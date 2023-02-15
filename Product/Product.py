class Product:
    """Базовый класс товара"""
    discount = 0.85
    product_list = []

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.product_list.append(self)

    def calculate_total_price(self):
        """Получаем общую стоимость конкретного товара в магазине"""
        total_cost = self.price * self.quantity
        return total_cost

    def apply_discount(self):
        """Применяем установленную скидку для конкретного товара"""
        self.price = self.price * self.discount
        return self.price

# item1 = Product("Смартфон", 10000, 20)
# item2 = Product("Ноутбук", 20000, 5)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())
# 200000  # общая стоимость смартфонов
# 100000  # общая стоимость ноутбуков

# Product.discount = 0.8  # устанавливаем новый уровень цен
# item1.apply_discount()
# print(item1.price)
# print(item2.price)
# 8000.0  # к цене смартфона применена скидка
# 20000  # к цене ноутбука скидка не была применена

# print(Product.product_list)
# #[<__main__.Item object at 0x000001EC6250C690>, <__main__.Item object at 0x000001EC6250C6D0>]
