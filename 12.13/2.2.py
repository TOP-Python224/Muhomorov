from abc import ABC
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Dish(ABC):
    """Определяет абстрактный класс с набором атрибутов."""
    name: str
    description: str
    ingredients: list
    price: Decimal
    how_to_consume: str


class Soup(Dish):
    """Определяет класс супов."""
    pass


class Snack(Dish):
    """Определяет класс закусок."""
    pass


class Drink(Dish):
    """Определяет класс закусок."""
    pass


class Soup1(Soup):
    """Определяет класс супа окрошка."""
    def __init__(self):
        self.name = 'Окрошка'
        self.description = 'Холодный летний суп'
        self.ingredients = ['Овощи', 'Колбаса', 'Квас']
        self.price = Decimal(125)
        self.how_to_consume = 'в холодном виде'


class Soup2(Soup):
    """Определяет класс супа мисо-суп."""
    def __init__(self):
        self.name = 'Мисо-суп'
        self.description = 'Традиционный японский суп'
        self.ingredients = ['Мисо', 'Овощи', 'Мясо']
        self.price = Decimal(220)
        self.how_to_consume = 'в горячем виде'


class Snack1(Snack):
    """Определяет класс закусок блины."""
    def __init__(self):
        self.name = 'Блины'
        self.description = 'Блины с икрой'
        self.ingredients = ['Блины', 'Масло', 'Красная икра']
        self.price = Decimal(550)
        self.how_to_consume = 'в теплом виде'


class Snack2(Snack):
    """Определяет класс закусок роллы."""
    def __init__(self):
        self.name = 'Роллы'
        self.description = 'Рулет с морепродуктами'
        self.ingredients = ['Рис', 'Сыр', 'Рыба', 'Водоросли']
        self.price = Decimal(330)
        self.how_to_consume = 'палочками с соевым соусом'


class Drink1(Drink):
    """Определяет класс напитка водка."""
    def __init__(self):
        self.name = 'Водка'
        self.description = 'Русская водка'
        self.ingredients = ['Альфа-спирт', 'Вода']
        self.price = Decimal(350)
        self.how_to_consume = 'в охлажденном виде'


class Drink2(Drink):
    """Определяет класс напитка сакэ."""
    def __init__(self):
        self.name = 'Сакэ'
        self.description = 'Японская водка'
        self.ingredients = ['Рисовый спирт', 'Вода']
        self.price = Decimal(450)
        self.how_to_consume = 'в подогретом виде'


@dataclass
class Factory(ABC):
    """Определяет абстрактную фабрику для разных наборов блюд."""
    def create_set(self) -> None:
        pass


class FactoryRussianSet(Factory):
    """Определяет фабрику для набора блюд русской кухни."""
    russian_kitchen = [Soup1, Snack1, Drink1]

    def create_set(self) -> None:
        """Передает блюда из набора на приготовление."""
        for dish in self.russian_kitchen:
            FactoryMakeDish.create_dish(dish())


class FactoryJapanSet(Factory):
    """Определяет фабрику для набора блюд японской кухни."""
    japan_kitchen = [Soup2, Snack2, Drink2]

    def create_set(self) -> None:
        """Передает блюда из набора на приготовление."""
        for dish in self.japan_kitchen:
            FactoryMakeDish.create_dish(dish())


class FactoryMakeDish(Factory):

    @staticmethod
    def create_dish(dish) -> Dish:
        """Создает отдельные блюда из набора."""
        print(f"Блюдо {dish.name} подано.")
        return dish


rk = FactoryRussianSet()
jk = FactoryJapanSet()

set_kitchen = input('Введите тип кухни: ')
match set_kitchen:
    case 'russian':
        rk.create_set()
    case 'japan':
        jk.create_set()
    case _:
        raise ValueError('неверный тип кухни')

# Stdout:
# Введите тип кухни: russian
# Блюдо Окрошка подано.
# Блюдо Блины подано.
# Блюдо Водка подано.

# Введите тип кухни: japan
# Блюдо Мисо-суп подано.
# Блюдо Роллы подано.
# Блюдо Сакэ подано.
