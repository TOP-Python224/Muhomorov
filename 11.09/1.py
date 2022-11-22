from typing import Self


class Matrix1:
    """
    Описывает матрицу.
    Элементы матрицы хранятся в атрибутах.
    """
    def __init__(self,
                 rows: int,
                 cols: int,
                 matrix: tuple[int]) -> None:
        """
        :param rows: количество строк матрицы,
        :param cols: количество столбцов матрицы,
        :param matrix: кортеж элементов матрицы, их количество должно быть равно произведению количества строк на количество столбцов матрицы.
        """
        for elem in (rows, cols) + matrix:
            if self.__check_input(elem):
                if len(matrix) == rows * cols:
                    self.__rows = rows
                    self.__cols = cols
                    self.__data = matrix
                else:
                    raise TypeError('Количество элементов матрицы не соответствует ее размеру!')

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
            raise TypeError('Введено не целое число!')

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
                if max_len < max_row:
                    max_len = max_row
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


# ИТОГ: проработать указанные моменты — 7/12
