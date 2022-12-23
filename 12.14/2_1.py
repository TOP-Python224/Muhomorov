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


class MilitaryCarrier(Carrier):
    """
    Класс для военного назначения перевозки.
    """
    def carry_military(self, items: str) -> str:
        return f"везет груз: {items} военного назначения."

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


class MilitaryPlan(Plane):
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


class CommercialPlan(Plane):
    """
    Класс для коммерческих самолетов.
    """
    def __init__(self, carrier: Carrier):
        super().__init__(carrier)
        self.description = 'Коммерческий самолет'

    def display_description(self):
        return f"{self.description}, {self.carrier.carry_commercial(self.objects)}"

    def add_objects(self, new_objects: str):
        self.objects += [new_objects]


military_carrier = MilitaryCarrier()
commercial_carrier = CommercialCarrier()
m1 = MilitaryPlan(military_carrier)
m1.add_objects('Бомбы')
m1.add_objects('Патроны')

m2 = MilitaryPlan(commercial_carrier)
m2.add_objects('Приборы')
m2.add_objects('Запчасти')

c1 = CommercialPlan(commercial_carrier)
c1.add_objects('Пассажиры')

c2 = CommercialPlan(military_carrier)
c2.add_objects('Продукты')

print(m1.display_description())
print(m2.display_description())
print(c1.display_description())
print(c2.display_description())

# Stdout:
# Военный самолет, везет груз: ['Бомбы', 'Патроны'] военного назначения.
# Военный самолет, везет груз: ['Приборы', 'Запчасти'] коммерческого назначения.
# Коммерческий самолет, везет груз: ['Пассажиры'] коммерческого назначения.
# Коммерческий самолет, везет груз: ['Продукты'] военного назначения.
