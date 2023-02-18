import csv


class Product:
    """Базовый класс товара"""
    discount = 0.85
    product_list = []

    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.product_list.append(self)

    @property
    def name(self) -> str:
        """Возвращает наименование товара"""
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """Обновляет наименование товара и выбрасывает исключение"""
        if len(name) > 10:
            raise Exception('Длина наименования товара превышает 10 символов.')
        self.__name = name

    def calculate_total_price(self):
        """Получаем общую стоимость конкретного товара в магазине"""
        total_cost = self.price * self.quantity
        return total_cost

    def apply_discount(self):
        """Применяем установленную скидку для конкретного товара"""
        self.price = self.price * self.discount
        return self.price

    @classmethod
    def instantiate_from_csv(cls, path: str) -> None:
        """Считывает данные из csv файло и создает экземпляры класса"""
        with open(path) as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                cls(
                    name=row['name'],
                    price=float(row['price']),
                    quantity=int(row['quantity'])
                )

    @staticmethod
    def is_integer(num) -> bool:
        """Проверяет, является ли число целым"""
        if isinstance(num, int) or (isinstance(num, float) and num % 1 == 0):
            return True
        else:
            return False
