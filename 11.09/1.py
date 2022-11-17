from typing import Self


class Matrix1:
    """
    Описывает матрицу.
    Элементы матрицы хранятся в атрибутах.
    """
    def __init__(self,
                 rows: int,
                 cols: int,
                 # ИСПРАВИТЬ: неудачный выбор параметра для конструктора (см. комментарий на строке)
                 matrix: tuple[int]) -> None:
        """
        :param rows: количество строк матрицы,
        :param cols: количество столбцов матрицы,
        :param matrix: кортеж элементов матрицы, их количество должно быть равно произведению количества строк на количество столбцов матрицы.
        """
        for elem in (rows, cols) + matrix:
            # ИСПРАВИТЬ здесь и далее: явного употребления имени класса лучше избегать: из-за этого начнутся проблемы в сложных моделях, использующих наследование — а статические методы можно вызывать и от self, при условии, что метод декорирован как статический
            if self.__check_input(elem):
                if len(matrix) == rows * cols:
                    self.__rows = rows
                    self.__cols = cols
                    # ИСПРАВИТЬ: насколько я вижу, вы не изменяете элементы этого атрибута — значит, список избыточен
                    self.__data = matrix
                else:
                    raise TypeError('Количество элементов матрицы не соответствует ее размеру!')

    # КОММЕНТАРИЙ: вот это хорошо
    @property
    def rows(self) -> int:
        return self.__rows

    @property
    def cols(self) -> int:
        return self.__cols

    @property
    def data(self) -> tuple:
        return self.__data

    # ИСПРАВИТЬ: здесь вы написали статический метод, следовательно нужно добавить соответствующий декоратор
    @staticmethod
    def __check_input(number: int) -> bool:
        """Проверяет, является ли введенное число целым."""
        if isinstance(number, int):
            return True
        else:
            raise TypeError('Введено не целое число!')

    # ИСПРАВИТЬ здесь и далее: зря исправили на self, в данном методе речь о сравнении атрибутов двух матриц, а значит удобно именовать первый параметр именно matrix1 — возвращайте всё взад =)
    @staticmethod
    def __check_matrix(matrix1, matrix2) -> bool:
        """Проверяет, является ли матрица экземпляром класса, проверяет равенство размеров 2-х матриц."""
        if isinstance(matrix2, Matrix1):
            if matrix1.rows == matrix2.rows and matrix1.cols == matrix2.cols:
                return True
            else:
                raise TypeError('Матрицы разного размера!')
        else:
            raise TypeError('Аргумент не является экземпляром класса!')

    # Непонятно, как аннотировать вывод функции как объект класса?
    # ИСПОЛЬЗОВАТЬ: в 3.10 для такой аннотации мы пишем имя класса и берём его в кавычки — также, как для ещё необъявленного класса (например, для такого, который объявляется позже в коде); в 3.11 для аннотации возврата экземпляра собственного класса введён специальный объект Self
    def __add__(self, matrix2) -> Self:
        """Производит поэлементное сложение 2-х матриц."""
        if self.__check_matrix(self, matrix2):
            result = tuple(map(
                lambda e1, e2: e1 + e2,
                self.data,
                matrix2.data
            ))
            return Matrix1(self.rows, self.cols, result)

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
                 matrix: tuple) -> None:
        """
        :param matrix: кортеж содержит одинаковые по длине кортежи элементов матрицы.
        """
        if self.__check_matrix(matrix):
            max_len = 0
            for row in matrix:
                max_row = len(str(max(row)))
                if max_len < max_row: max_len = max_row
                for elem in row:
                    if self.__check_input(elem):
                        self.__rows = len(matrix)
                        self.__cols = len(matrix[0])
            self.__max_len = max_len
        for i in range(len(matrix)):
            setattr(self, '_Hidden__row_' + str(i), matrix[i])

    @property
    def rows(self) -> int:
        return self.__rows

    @property
    def cols(self) -> int:
        return self.__cols

    @property
    def max_len(self) -> int:
        return self.__max_len

    @staticmethod
    def __check_input(number: int) -> bool:
        """Проверяет, является ли введенное число целым."""
        if isinstance(number, int):
            return True
        else:
            raise TypeError('Введено не целое число!')

    @staticmethod
    def __check_matrix(matrix: tuple) -> bool:
        """Проверяет, является ли введенный аргумент кортежем кортежей правильного размера."""
        if not isinstance(matrix, tuple):
            raise TypeError('Введенный аргумент не является кортежем!')
        elif not all([True if isinstance(elem, tuple) else False for elem in matrix]):
            raise TypeError('Кортеж содержит элементы, не являющиеся кортежами!')
        elif not all([True if len(elem) == len(matrix[0]) else False for elem in matrix]):
            raise TypeError('Кортеж содержит кортежи не одинакового размера!')
        else:
            return True

    @staticmethod
    def __compare_matrix(matrix1, matrix2) -> bool:
        """Проверяет, является ли матрица экземпляром класса, проверяет равенство размеров 2-х матриц."""
        if isinstance(matrix2, Matrix2):
            if matrix1.rows == matrix2.rows and matrix1.cols == matrix2.cols:
                return True
            else:
                raise TypeError('Матрицы разного размера!')
        else:
            raise TypeError('Аргумент не является экземпляром класса!')

    @staticmethod
    def __get_rows(self):
        """Возвращает пару ключ/значение для каждой строки матрицы."""
        for key, value in self.__dict__.items():
            if key.startswith('_Hidden__row_'):
                yield key, value

    def __getitem__(self, item):
        return getattr(self, item)

    def __getattr__(self, attr):
        if attr.startswith('row_'):
            attr = '_Hidden__' + attr
            return self[attr]
        else:
            return None

    def __str__(self) -> str:
        result = ''
        for key, value in self.__get_rows(self):
            centered_row = [
                            str(elem).rjust(self.max_len + 1)
                            for elem in value
            ]
            result += f"{''.join(centered_row)}\n"
        return result

    def __add__(self, matrix2) -> Self:
        """Производит поэлементное сложение 2-х матриц."""
        result = ()
        if self.__compare_matrix(self, matrix2):
            for key, value in self.__get_rows(self):
                row1 = value
                row2 = matrix2.__dict__[key]
                result += tuple(map(lambda a, b: a + b, row1, row2)),
            return Matrix2(result)

    def __sub__(self, matrix2) -> Self:
        """Производит поэлементное вычитание 2-х матриц."""
        result = ()
        if self.__compare_matrix(self, matrix2):
            for key, value in self.__get_rows(self):
                row1 = value
                row2 = matrix2.__dict__[key]
                result += tuple(map(lambda a, b: a - b, row1, row2)),
            return Matrix2(result)

    def __mul__(self, number) -> Self:
        """Производит умножение элементов матрицы на число."""
        result = ()
        if self.__check_input(number):
            for key, value in self.__get_rows(self):
                result += tuple(elem * number for elem in value),
            return Matrix2(result)

# m1 = Matrix2(((1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)))
# m2 = Matrix2(((2, 3, 4), (5, 6, 7), (8, 9, 10), (11, 12, 13)))
# print(m1)
# print(m1 + m2)
# print(m1 - m2)
# print(m2 - m1)
# print(m1 * 11)
# stdout:

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

# КОММЕНТАРИЙ: здесь же неотличимы аргументы, являющиеся размерами матрицы, от аргументов, являющихся элементами матрицы; мы так упорно изучали параметризацию функций как раз для того, чтобы не допускать таких вызовов
# m1 = Matrix1(3, 4, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
# m2 = Matrix1(3, 4, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
# m2 = Matrix1(3, 4, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
# КОММЕНТАРИЙ: не лень было ещё сорок чисел набирать?))
# m3 = Matrix2(4, 5, *range(1, 21))
# m4 = Matrix2(4, 5, *range(2, 22))
# print(m1)
# print(m1 + m2)
# print(m1 - m2)
# print(m1 * 10)
# print(m3 + m4)
# print(m3 - m4)
# print(m3 * 7)


# stdout:
#   1  2  3  4
#   5  6  7  8
#   9 10 11 12

#   3  5  7  9
#  11 13 15 17
#  19 21 23 25

#  -1 -1 -1 -1
#  -1 -1 -1 -1
#  -1 -1 -1 -1

#   10  20  30  40
#   50  60  70  80
#   90 100 110 120

#   3  5  7  9 11
#  13 15 17 19 21
#  23 25 27 29 31
#  33 35 37 39 41

#  -1 -1 -1 -1 -1
#  -1 -1 -1 -1 -1
#  -1 -1 -1 -1 -1
#  -1 -1 -1 -1 -1

#    7  14  21  28  35
#   42  49  56  63  70
#   77  84  91  98 105
#  112 119 126 133 140


# КОММЕНТАРИЙ: первый вариант засчитываю, второй нет — его необходимо переписать; не лишним будет также ещё подумать над способами хранения элементов матрицы в различных структурах атрибутов

# ИТОГ: проработать указанные моменты — 7/12
