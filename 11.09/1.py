# КОММЕНТАРИЙ: для переключения между версиями 3.10 и 3.11 без переписывания кода
# from __future__ import annotations
from typing import Self

# переменные типов для аннотаций
# ИСПОЛЬЗОВАТЬ: аннотация tuple[int] означает кортеж с одним элементом int, а когда мы хотим обозначить кортеж с неопределённым количеством элементов, то добавляем многоточие
Row = list[int] | tuple[int, ...]
Matrix = list[Row] | tuple[Row, ...]


class Matrix1:
    """
    Описывает матрицу.
    Элементы матрицы хранятся в одном атрибуте в плоской структуре.
    """
    def __init__(self,
                 rows: int,
                 cols: int,
                 # ИСПОЛЬЗОВАТЬ: составные типы лучше аннотировать отдельно объявленной переменной
                 matrix: Row) -> None:
        """
        :param rows: количество строк матрицы,
        :param cols: количество столбцов матрицы,
        :param matrix: кортеж элементов матрицы, их количество должно быть равно произведению количества строк на количество столбцов матрицы.
        """
        # КОММЕНТАРИЙ: вообще, не уверен, что принудительная проверка типа действительно здесь необходима:
        #  1) типы параметров конструктора аннотированы, далее начинается ответственность пользователя;
        #  2) неверно переданный аргумент точно также приводит к исключению, которое не сильно уточняет ситуацию;
        #  3) такие проверки актуальны в гибких методах, которые могут принимать на вход разные типы;
        #  4) мы можем захотеть работать с матрицей, элементами которой являются строки, а не числа (например, поле крестиков-ноликов)
        for elem in (rows, cols) + matrix:
            if self.__check_input(elem):
                if len(matrix) == rows * cols:
                    self.__rows = rows
                    self.__cols = cols
                    self.__data = tuple(matrix)
                else:
                    # ИСПРАВИТЬ здесь и далее: сообщение, передаваемое в конструктор классов исключений, выводится после двоеточия, поэтому пишется в нижнем регистре и без знаков препинания в конце
                    raise TypeError('количество элементов матрицы не соответствует ее размеру')

    @property
    def rows(self) -> int:
        return self.__rows

    @property
    def cols(self) -> int:
        return self.__cols

    @property
    def data(self) -> tuple:
        return self.__data

    @staticmethod
    def __check_input(number: int) -> bool:
        """Проверяет, является ли введенное число целым."""
        if isinstance(number, int):
            return True
        else:
            # ИСПРАВИТЬ: не введено, а передано в конструктор
            raise TypeError('в конструктор передано не целое число')

    @staticmethod
    def __check_matrix(matrix1, matrix2) -> bool:
        """Проверяет, является ли матрица экземпляром класса, проверяет равенство размеров 2-х матриц."""
        if isinstance(matrix2, Matrix1):
            if matrix1.rows == matrix2.rows and matrix1.cols == matrix2.cols:
                return True
            else:
                raise TypeError('матрицы разного размера')
        else:
            # ИСПРАВИТЬ в сообщении: какой именно аргумент? какого именно класса?
            #  моделируйте ситуацию:
            #      >>> m1 + 'abc'
            #      TypeError: Аргумент не является экземпляром класса!
            #  ничего не понятно
            raise TypeError('второй аргумент не является экземпляром класса Matrix1')

    def __add__(self, matrix2) -> Self:
        """Производит поэлементное сложение 2-х матриц."""
        if self.__check_matrix(self, matrix2):
            result = tuple(map(
                lambda e1, e2: e1 + e2,
                self.data,
                matrix2.data
            ))
            # КОММЕНТАРИЙ: а если здесь тоже вместо явного имени Matrix1 использовать self.__class__, то код получится более гибким, и его можно будет удобно наследовать
            return self.__class__(self.rows, self.cols, result)

    def __sub__(self, matrix2) -> Self:
        """Производит поэлементное вычитание 2-х матриц."""
        if self.__check_matrix(self, matrix2):
            result = tuple(map(
                lambda e1, e2: e1 - e2,
                self.data,
                matrix2.data
            ))
            return Matrix1(self.rows, self.cols, result)

    def __mul__(self, number) -> Self:
        """Производит умножение элементов матрицы на число."""
        if self.__check_input(number):
            result = tuple(
                elem * number
                for elem in self.__data
            )
            return Matrix1(self.rows, self.cols, result)
    
    def __str__(self) -> str:
        max_width = len(str(max(self.data)))
        centered_matrix = [
            str(elem).rjust(max_width + 1)
            for elem in self.data
        ]
        result = ''
        for i in range(self.rows):
            result += f"{''.join(centered_matrix[i*self.cols:(i+1)*self.cols])}\n"
        return result


class Matrix2:
    """
    Описывает матрицу.
    Отдельные строки матрицы хранятся в отдельных атрибутах.
    """
    def __init__(self,
                 matrix: Matrix) -> None:
        """
        :param matrix: кортеж содержит одинаковые по длине кортежи элементов матрицы.
        """
        if self.__check_matrix(matrix):
            # ИСПОЛЬЗОВАТЬ: неудачный выбор имени max_len, мне, например, представляется количество элементов самой матрицы
            max_elem_width = 0
            for row in matrix:
                max_row = len(str(max(row)))
                if max_elem_width < max_row:
                    max_elem_width = max_row
                for elem in row:
                    if self.__check_input(elem):
                        pass
                        # ИСПРАВИТЬ: перезаписывать два одинаковых атрибута столько раз, сколько элементов в матрице — не лучшая идея
                    self.__rows = len(matrix)
                    self.__cols = len(matrix[0])
            self.__max_elem_width = max_elem_width
        # ИСПРАВИТЬ: вы только что записали результат вызова len(matrix) в атрибут, незачем повторно вызывать функцию
        for i in range(self.__rows):
            # КОММЕНТАРИЙ: здесь вы добавили только частный атрибут, а если хотите добавить защищённый атрибут со включенным механизмом искажения имён, то имя атрибута должно включать имя класса '_Matrix2__row_0' — в объявлении класса к такому атрибуту можно будет обращаться self.__row_0
            setattr(self, '_Hidden__row_' + str(i), matrix[i])
            # setattr(self, '_Hidden__row_' + str(i), matrix[i])

    @property
    def rows(self) -> int:
        return self.__rows

    @property
    def cols(self) -> int:
        return self.__cols

    @property
    def max_elem_width(self) -> int:
        return self.__max_elem_width

    @staticmethod
    def __check_input(number: int) -> bool:
        """Проверяет, является ли введенное число целым."""
        if isinstance(number, int):
            return True
        else:
            raise TypeError('введено не целое число')

    @staticmethod
    def __check_matrix(matrix: tuple) -> bool:
        """Проверяет, является ли введенный аргумент кортежем кортежей правильного размера."""
        if not isinstance(matrix, tuple):
            raise TypeError('введенный аргумент не является кортежем')
        elif not all([True if isinstance(elem, tuple) else False for elem in matrix]):
            raise TypeError('кортеж содержит элементы, не являющиеся кортежами')
        elif not all([True if len(elem) == len(matrix[0]) else False for elem in matrix]):
            raise TypeError('кортеж содержит кортежи не одинакового размера')
        else:
            return True

    @staticmethod
    def __compare_matrix(matrix1, matrix2) -> bool:
        """Проверяет, является ли матрица экземпляром класса, проверяет равенство размеров 2-х матриц."""
        if isinstance(matrix2, Matrix2):
            if matrix1.rows == matrix2.rows and matrix1.cols == matrix2.cols:
                return True
            else:
                raise TypeError('матрицы разного размера')
        else:
            raise TypeError('второй аргумент не является экземпляром класса Matrix2')

    # ИСПРАВИТЬ: зачем писать статический метод, который затем вызывать от экземпляра, вручную передавая объект экземпляра?
    def __get_rows(self):
        """Возвращает пару ключ/значение для каждой строки матрицы."""
        # КОММЕНТАРИЙ: любопытный подход
        for key, value in self.__dict__.items():
            # КОММЕНТАРИЙ: но если так, то я бы ранее дал этим атрибутам имена, начинающиеся на '___row', а здесь итерировался бы по отсортированному словарю — чтобы меньше атрибутов перебирать в этом цикле
            if key.startswith('_Hidden__row_'):
                yield key, value

    # УДАЛИТЬ: так и не понял, зачем реализовали эти два метода — они нигде не использованы
    # def __getitem__(self, item):
    #     return getattr(self, item)
    #
    # def __getattr__(self, attr):
    #     if attr.startswith('row_'):
    #         attr = '_Hidden__' + attr
    #         return self[attr]
    #     else:
    #         return None

    def __str__(self) -> str:
        result = ''
        for key, value in self.__get_rows():
            centered_row = [
                str(elem).rjust(self.max_elem_width + 1)
                for elem in value
            ]
            result += f"{''.join(centered_row)}\n"
        return result

    def __add__(self, matrix2) -> Self:
        """Производит поэлементное сложение 2-х матриц."""
        result = ()
        if self.__compare_matrix(self, matrix2):
            for key, value in self.__get_rows():
                row1 = value
                row2 = matrix2.__dict__[key]
                result += tuple(map(lambda a, b: a + b, row1, row2)),
            return Matrix2(result)

    def __sub__(self, matrix2) -> Self:
        """Производит поэлементное вычитание 2-х матриц."""
        result = ()
        if self.__compare_matrix(self, matrix2):
            for key, value in self.__get_rows():
                row1 = value
                row2 = matrix2.__dict__[key]
                result += tuple(map(lambda a, b: a - b, row1, row2)),
            return Matrix2(result)

    def __mul__(self, number) -> Self:
        """Производит умножение элементов матрицы на число."""
        result = ()
        if self.__check_input(number):
            for key, value in self.__get_rows():
                result += tuple(elem * number for elem in value),
            return Matrix2(result)



# ИСПОЛЬЗОВАТЬ: перенос со второй строки (для небольшого количества строк)
m1 = Matrix2(((1, 2, 3),
              (4, 5, 6),
              (7, 8, 9),
              (10, 11, 12)))
# ИСПОЛЬЗОВАТЬ: или перенос с первой строки
m2 = Matrix2(
    ((2, 3, 4),
     (5, 6, 7),
     (8, 9, 10),
     (11, 12, 13))
)
print(m1)
print(m1 + m2)
print(m1 - m2)
print(m2 - m1)
print(m1 * 11)

# stdout:
#
#   1  2  3
#   4  5  6
#   7  8  9
#  10 11 12
#
#   3  5  7
#   9 11 13
#  15 17 19
#  21 23 25
#
#  -1 -1 -1
#  -1 -1 -1
#  -1 -1 -1
#  -1 -1 -1
#
#  1 1 1
#  1 1 1
#  1 1 1
#  1 1 1
#
#   11  22  33
#   44  55  66
#   77  88  99
#  110 121 132


# КОММЕНТАРИЙ: дополнительно проработать механику вызова методов от объектов экземпляров -> функций от объектов классов, и разобраться в различиях между обычными и статическими (и, вероятно, классовыми) методами


# ИТОГ: так уже лучше — 10/12
