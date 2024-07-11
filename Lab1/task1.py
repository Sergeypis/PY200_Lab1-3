# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from datetime import date


class Bicycle:
    """
    Класс, описывающий объект велосипед.
    """
    categories = ['road', 'bmx', 'trial']

    def __init__(self, color: str, category: str, gears: int):
        """
        Создание и подготовка к работе объекта "Велосипед".

        :param color: Цвет велосипеда
        :param category: Категория велосипеда
        :param gears: Количество скоростей трансмиссии
        :raise ValueError: Если количество скоростей трансмиссии не в диапазоне 1-10, возвращается ошибка.

        >>> bicycle = Bicycle('red', 'road', 10)
        """
        if not isinstance(color, str):
            raise TypeError("Цвет велосипеда должен быть строкового типа: 'str'")
        self.color = color

        self.category = None
        self.check_category(category, Bicycle.categories)

        if not isinstance(gears, int):
            raise TypeError("Количество скоростей трансмиссии должно быть типа: 'int'")
        if not 1 <= gears <= 10:
            raise ValueError("Количество скоростей трансмиссии не может быть меньше одной")
        self.gears = gears

    def check_category(self, category: str, categories: list) -> None:
        """
        Проверяет принадлежит ли экземпляр к категории из списка разрешенных.

        :param category: Категория велосипеда
        :param categories: Список возможных категорий
        :raise ValueError: Если категории велосипеда нет в спике допустимых, возвращается ошибка.

        :return: Валидная категория велосипеда, либо ошибка ValueError, TypeError

        >>> bicycle = Bicycle('red', 'road', 10)
        >>> bicycle.category == 'road'
        True
        """
        if not isinstance(category, str):
            raise TypeError("Категория велосипеда должна быть строкового типа: 'str'")
        if category not in categories:
            raise ValueError("Ошибка. Задана несуществущая категория")
        self.category = category

    def change_speed_up(self, current_gear: int) -> int:
        """
        Функция повышает передачу велосипеда на одну ступень.

        :param current_gear: Текущщая передача велосипеда
        :raise ValueError: Если текущая скорость трансмиссии не в диапазоне 1-10, возвращается ошибка.

        :return: Повышенная на одну ступень передача велосипеда

        >>> bicycle = Bicycle('red', 'road', 10)
        >>> bicycle.change_speed_up(9)
        10
        """
        if not isinstance(current_gear, int):
            raise TypeError("Текущая скорость трансмиссии должна быть типа: 'int'")
        if not 1 <= current_gear <= 10:
            raise ValueError("Текущая скорость трансмиссии должна быть от 1 до 10")
        if current_gear != self.gears:
            current_gear += 1
        return current_gear

    @staticmethod
    def state_move_or_stay(speed: float) -> bool:
        """
        Функция определяет состояние велосипеда: движется или стоит.

        :param speed: Текущая скорость велосипеда
        :raise ValueError: Если текущая скорость велосипеда меньше 0, возвращается ошибка.

        :return: True, если движется, False, если стоит.
        >>> Bicycle.state_move_or_stay(0)
        False
        >>> bicycle2 = Bicycle('blue', 'bmx', 10)
        >>> bicycle2.state_move_or_stay(5)
        True
        """
        if not isinstance(speed, (float | int)):
            raise TypeError("Текущая скорость трансмиссии должна быть типа: 'float' или 'int'")
        if speed < 0:
            raise ValueError("Скорость не может быть отрицательной")
        return False if speed == 0 else True


class User:
    """
    Класс описывает пользователя из БД.
    """
    def __init__(self, name: str, age: int):
        """
        Создание и подготовка к работе объекта "Пользователь".

        :param name: Имя пользователя
        :param age: Возраст пользователя
        :raise ValueError: Если возраст меньше 0, возвращается ошибка.

        >>> user = User('Сергей', 42)
        """
        if not isinstance(name, str):
            raise TypeError("Имя пользователя должно быть строкового типа: 'str'")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст пользователя должен быть типа: 'int'")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self.age = age

    def change_age(self, new_age: int) -> None:
        """
        Метод изменяет возраст пользователя

        :param new_age: Новый возраст пользователя
        :return: Новый возраст пользователя

        >>> user = User('Сергей', 42)
        >>> user.change_age(39)
        >>> user.age == 39
        True
        """
        if not isinstance(new_age, int):
            raise TypeError("Возраст пользователя должен быть типа: 'int'")
        if new_age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self.age = new_age

    def check_age(self) -> bool:
        """
        Метод проверяет возраст пользователя, должен быть больше 18.

        :return: True - если больше 18 лет, False - если меньше.

        >>> user = User('Сергей', 42)
        >>> user.check_age()
        True
        """
        age_limit = 18
        return False if self.age < age_limit else True


class Vegetable:
    """
    Класс описывает объект овощей.
    """
    def __init__(self, type_of: str, weight: float | int, expiration_date: int):
        """
        Создание и подготовка к работе объекта "Овощ".

        :param type_of: Тип или сорт овоща.
        :param weight: Вес.
        :param expiration_date: Срок годности.
        :raise ValueError: Если вес меньше 0 или срок годности меньше или равен 0, возвращается ошибка.

        >>> tomato = Vegetable('Помидоры', 1.5, 10)
        """
        if not isinstance(type_of, str):
            raise TypeError("Наименование овоща должно быть типа: 'str'")
        self.type_of = type_of

        if not isinstance(weight, (float, int)):
            raise TypeError("Вес овоща должен быть типа: 'float' или 'int'")
        if weight < 0:
            raise ValueError("Вес не может быть отрицательным")
        self.weight = weight

        if not isinstance(expiration_date, int):
            raise TypeError("Срок годности овоща должен быть типа: 'int'")
        if expiration_date < 0:
            raise ValueError("Срок годности не может быть отрицательным или равен 0")
        self.expiration_date = expiration_date

    def change_weight(self, weight_difference: float | int, direction: bool) -> None:
        """
        Метод изменяет вес овоща в зависимости от входных данных, увеличивает или уменьшает.

        :param weight_difference: Вес который нужно прибавить, отнять.
        :param direction: Если True-прибавить вес, если False-отнять.
        :raise ValueError: Если вес меньше 0 или неверные исходные данные, возвращается ошибка.

        >>> tomato = Vegetable('Помидоры', 1.5, 10)
        >>> tomato.change_weight(1.5, False)
        >>> tomato.weight == 0
        True
        """
        if not isinstance(weight_difference, (float, int)):
            raise TypeError("Вес овоща должен быть типа: 'float' или 'int'")
        if weight_difference < 0:
            raise ValueError("Вес не может быть отрицательным")

        if not isinstance(direction, bool):
            raise TypeError("Параметр изменения веса должен быть типа: 'bool'")
        if weight_difference > self.weight and direction is False:
            raise ValueError("Ошибка. Неверные исходные данные")

        if direction:
            self.weight = self.weight + weight_difference
        else:
            self.weight = self.weight - weight_difference

    def check_expiration(self, purchase_date: str) -> bool:
        """
        Метод проверяет годность продукта по дате покупке и сроку годности.

        :param purchase_date: Дата покупки продукта.
        :return: True - если срок годности не вышел, False- если срок годности закончился.

        >>> tomato = Vegetable('Помидоры', 1.5, 10)
        >>> tomato.check_expiration('2024-06-10')
        """


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
