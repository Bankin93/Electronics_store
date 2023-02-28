import csv


class Product:
    """Базовый класс товара"""
    discount = 0.85
    product_list = []

    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

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

    def __add__(self, other):
        """Сложение по количеству товара в магазине"""
        if isinstance(other, Product):
            return self.quantity + other.quantity
        else:
            raise ValueError('С объектами других классов сложение запрещено')

    @staticmethod
    def is_integer(num) -> bool:
        """Проверяет, является ли число целым"""
        if isinstance(num, int) or (isinstance(num, float) and num % 1 == 0):
            return True
        else:
            return False

    @classmethod
    def instantiate_from_csv(cls, path: str) -> None:
        """Считывает данные из csv файла и создает экземпляры класса"""
        with open(path, "r") as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                item = cls(
                    name=row['name'],
                    price=float(row['price']),
                    quantity=int(row['quantity'])
                )
                cls.product_list.append(item)


class Phone(Product):
    """Класс Phone, наследуемый от базового Product"""
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{super().__repr__().replace(')', ',')} {self.number_of_sim})"

    def __str__(self):
        return super().__str__()

    @property
    def number_of_sim(self) -> int:
        """Возвращаем кол-во сим-карт"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim: int) -> None:
        """Обновляет количество сим-карт и выбрасывает исключение"""
        if number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        else:
            raise Exception('Количество физических SIM-карт должно быть целым числом больше нуля.')
