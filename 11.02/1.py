from numbers import Real


class Tetrahedron:
    """
    Описывает правильный тетраэдр с ребром размером edge.
    """
    # ИСПРАВИТЬ: метод __init__() всегда возвращает None
    def __init__(self, edge: Real) -> Real:
        if isinstance(edge, Real):
            self.edge = edge
        else:
            raise TypeError('Должно быть число!')

    @property
    def area(self) -> Real:
        """Возвращает площадь тетраэдра."""
        # ИСПРАВИТЬ: в аннотации возвращаемого значения заявлен числовой тип, а возвращаете строку
        return f"{3**0.5 * self.edge**2:.2f}"

    @property
    def volume(self) -> Real:
        """Возвращает объем тетраэдра."""
        # ИСПРАВИТЬ: в аннотации возвращаемого значения заявлен числовой тип, а возвращаете строку
        return f"{2**0.5 / 12 * self.edge**3:.2f}"

    def __str__(self):
        return f"Тетраэдр: ребро = {self.edge}, площадь = {self.area}, объем = {self.volume}"


t1 = Tetrahedron(5)
t2 = Tetrahedron(3.3)
print(t1.area)
print(t1.volume)
print(t2.area)
print(t2.volume)
print(t1)
print(t2)


# stdout:
# 43.30
# 14.73
# 18.86
# 4.24
# Тэтраэдр: ребро = 5, площадь = 43.30, объем = 14.73
# Тэтраэдр: ребро = 3.3, площадь = 18.86, объем = 4.24


# ИТОГ: хорошо — 5/6
