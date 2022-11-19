class Point:
    """Описывает точку плоскости в декартовой системе координат."""
    def __init__(self,
                 x: float,
                 y: float):
        self.x = x
        self.y = y

    # Этого нет в ТЗ, но так красивее.
    def __ne__(self, other):
        return self.x != other.x or self.y != other.y


class Line:
    """Описывает отрезок, задаваемый двумя точками на плоскости в декартовой системе координат. """
    def __init__(self,
                 start: Point,
                 end: Point):
        self.start_point = start
        self.end_point = end

    @property
    def length(self) -> float:
        """Вычисляет и возвращает длину отрезка как расстояние между двумя точками."""
        return ((self.start_point.x - self.end_point.x)**2
                + (self.start_point.y - self.end_point.y)**2)**0.5


class Polygon(list):
    """Описывает многоугольник, задаваемый отрезками на плоскости в декартовой системе координат."""
    def __init__(self,
                 side1: Line,
                 side2: Line,
                 side3: Line,
                 *sides: Line):
        super().__init__((side1, side2, side3, *sides))

    def _is_closed(self) -> bool:
        """Проверяет, замкнут ли многоугольник."""
        if self[0].start_point != self[-1].end_point:
            return False
        for i in range(len(self) - 1):
            if self[i].end_point != self[i + 1].start_point:
                return False
        return True

    @property
    def perimeter(self) -> float:
        """Вычисляет и возвращает периметр многоугольника как сумму длин отрезков его составляющих, если многоугольник замкнут."""
        sides_length = 0
        if self._is_closed():
            for line in self:
                sides_length += line.length
        return sides_length


# p1 = Point(1, 2)
# p2 = Point(7, 5)
# p3 = Point(11, 2)
# p4 = Point(6, -1)
# p5 = Point(4, 1)
# p6 = Point(0, 0)
#
# l1 = Line(p1, p2)
# l2 = Line(p2, p3)
# l3 = Line(p3, p4)
# l4 = Line(p4, p5)
# l5 = Line(p5, p1)
# l6 = Line(p5, p6)
#
# pol1 = Polygon(l1, l2, l3, l4, l5)
# pol2 = Polygon(l1, l2, l3, l4, l6)
# pol3 = Polygon(Line(p1, p5), Line(p5, p4), Line(p4, p1))
# pol4 = Polygon(Line(p2, p5), Line(p5, p4), Line(p4, p1))
#
# print(pol1.perimeter)
# print(pol2.perimeter)
# print(pol3.perimeter)
# print(pol4.perimeter)

# stdout:
# 23.52986061225924
# 0
# 11.82165667975987
# 0
