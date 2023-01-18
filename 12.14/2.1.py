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

# class MilitaryCarrier(Carrier):
class PassengerCarrier(Carrier):
    """
    Класс для пассажирского перевозчика.
    """
    def carry_military(self, items: str) -> str:
        return f"везет пассажиров: {items} военного назначения."

    # КОММЕНТАРИЙ: у вас же эти два метода ничем кроме имени метода не отличаются — должно было насторожить, потому что методы очевидно должны отличаться, иначе зачем всё это
    def carry_commercial(self, items: str) -> str:
        return f"везет пассажиров: {items} коммерческого назначения."


# class CommercialCarrier(Carrier):
class CargoCarrier(Carrier):
    """
    Класс для грузового перевозчика.
    """
    def carry_military(self, items: str) -> str:
        return f"везет груз: {items} военного назначения."

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
        self.objects += [new_objects]


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
        super().add_objects(new_objects)


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
        super().add_objects(new_objects)


passenger_carrier = PassengerCarrier()
cargo_carrier = CargoCarrier()

# КОММЕНТАРИЙ: здесь должен использоваться грузовой носитель
m1 = MilitaryPlane(cargo_carrier)
m1.add_objects('Бомбы')
m1.add_objects('Патроны')

m2 = MilitaryPlane(passenger_carrier)
m2.add_objects('Солдаты')

# КОММЕНТАРИЙ: а здесь должен использоваться пассажирский носитель
c1 = CommercialPlane(passenger_carrier)
c1.add_objects('Туристы')

c2 = CommercialPlane(cargo_carrier)
c2.add_objects('Запчасти')
c2.add_objects('Электроника')

print(m1.display_description())
print(m2.display_description())
print(c1.display_description())
print(c2.display_description())


# Stdout:
# Военный самолет, везет груз: ['Бомбы', 'Патроны'] военного назначения.
# Военный самолет, везет пассажиров: ['Солдаты'] военного назначения.
# Коммерческий самолет, везет пассажиров: ['Туристы'] коммерческого назначения.
# Коммерческий самолет, везет груз: ['Запчасти', 'Электроника'] коммерческого назначения.


# ИТОГ: подумайте ещё о смысле моста и перепишите задачу — 3/6
