from abc import ABC, abstractmethod


class Carrier(ABC):
    """
    Абстрактный базовый класс для типов назначения перевозки.
    """
    @abstractmethod
    def carry_military(self, items):
        pass

    @abstractmethod
    def carry_commercial(self, items):
        pass


# ИСПРАВИТЬ: типы назначения — это пассажирский (Passenger) и грузовой (Cargo)

class MilitaryCarrier(Carrier):
    """
    Класс для военного назначения перевозки.
    """
    def carry_military(self, items: str) -> str:
        return f"везет груз: {items} военного назначения."

    # КОММЕНТАРИЙ: у вас же эти два метода ничем кроме имени метода не отличаются — должно было насторожить, потому что методы очевидно должны отличаться, иначе зачем всё это
    def carry_commercial(self, items: str) -> str:
        return f"везет груз: {items} военного назначения."


class CommercialCarrier(Carrier):
    """
    Класс для коммерческого назначения перевозки.
    """
    def carry_military(self, items: str) -> str:
        return f"везет груз: {items} коммерческого назначения."

    def carry_commercial(self, items: str) -> str:
        return f"везет груз: {items} коммерческого назначения."


class Plane(ABC):
    """
    Абстрактный базовый класс для самолетов разного назначения.
    """
    def __init__(self, carrier: Carrier):
        self.carrier = carrier
        self.objects: list = []

    @abstractmethod
    def display_description(self):
        pass

    @abstractmethod
    def add_objects(self, new_objects):
        pass


# КОММЕНТАРИЙ: в шаблоне Мост классы не дублируют, а дополняют друг друга по назначению — у вас же получилось, что в одной цепочке наследования Военные и Коммерческие самолёты, и в другой цепочке также Военные и Коммерческие


class MilitaryPlane(Plane):
    """
    Класс для военных самолетов.
    """
    def __init__(self, carrier: Carrier):
        super().__init__(carrier)
        self.description = 'Военный самолет'

    def display_description(self):
        return f"{self.description}, {self.carrier.carry_military(self.objects)}"

    def add_objects(self, new_objects: str):
        self.objects += [new_objects]


class CommercialPlane(Plane):
    """
    Класс для коммерческих самолетов.
    """
    def __init__(self, carrier: Carrier):
        super().__init__(carrier)
        self.description = 'Коммерческий самолет'

    # КОММЕНТАРИЙ: для пассажиров и груза выводятся различные описания в зависимости от того, к какому классу проброшен мост
    def display_description(self):
        return f"{self.description}, {self.carrier.carry_commercial(self.objects)}"

    def add_objects(self, new_objects: str):
        self.objects += [new_objects]


military_carrier = MilitaryCarrier()
commercial_carrier = CommercialCarrier()

# КОММЕНТАРИЙ: здесь должен использоваться грузовой носитель
m1 = MilitaryPlane(military_carrier)
m1.add_objects('Бомбы')
m1.add_objects('Патроны')

m2 = MilitaryPlane(commercial_carrier)
m2.add_objects('Приборы')
m2.add_objects('Запчасти')

# КОММЕНТАРИЙ: а здесь должен использоваться пассажирский носитель
c1 = CommercialPlane(commercial_carrier)
c1.add_objects('Пассажиры')

c2 = CommercialPlane(military_carrier)
c2.add_objects('Продукты')

print(m1.display_description())
print(m2.display_description())
print(c1.display_description())
print(c2.display_description())


# stdout:
# Военный самолет, везет груз: ['Бомбы', 'Патроны'] военного назначения.
# Военный самолет, везет груз: ['Приборы', 'Запчасти'] коммерческого назначения.
# Коммерческий самолет, везет груз: ['Пассажиры'] коммерческого назначения.
# Коммерческий самолет, везет груз: ['Продукты'] военного назначения.


# ИТОГ: подумайте ещё о смысле моста и перепишите задачу — 3/6
