from typing import Self


# ИСПОЛЬЗОВАТЬ: объявления исключений обычно размещают над использующими их классами (или в отдельном модуле)
class Matrix1Error(Exception):
    pass

class Matrix1ElemSizeError(Matrix1Error):
    def __init__(self, *bad_args):
        self.bad_args = bad_args
        super().__init__(f"Количество элементов матрицы '{self.bad_args[0]}' "
                         f"не соответствует ее размеру '{self.bad_args[1]}'!")

class Matrix1BadNumberError(Matrix1Error):
    def __init__(self, bad_arg):
        self.bad_arg = bad_arg
        super().__init__(f"Введено не целое число '{self.bad_arg}'!")

class Matrix1BadSizeError(Matrix1Error):
    def __init__(self, *matrix):
        self.matrix = matrix
        super().__init__(f"Матрицы разного размера: '{self.matrix[0].rows}*{self.matrix[0].cols}' "
                         f"и '{self.matrix[1].rows}*{self.matrix[1].cols}'!")

class Matrix1BadInstanceError(Matrix1Error):
    def __init__(self, *matrix):
        self.matrix = matrix
        super().__init__(f"Аргумент - экземпляр класса '{matrix[1].__class__.__name__}', "
                         f"должен быть '{matrix[0].__class__.__name__}'!")


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
                    raise Matrix1ElemSizeError(rows * cols, len(matrix))

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
            raise Matrix1BadNumberError(number)

    @staticmethod
    def __check_matrix(matrix1, matrix2) -> bool:
        """Проверяет, является ли матрица экземпляром класса, проверяет равенство размеров 2-х матриц."""
        if isinstance(matrix2, Matrix1):
            if matrix1.rows == matrix2.rows and matrix1.cols == matrix2.cols:
                return True
            else:
                raise Matrix1BadSizeError(matrix1, matrix2)
        else:
            raise Matrix1BadInstanceError(matrix1, matrix2)

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
            result += f"{''.join(centered_matrix[i * self.cols:(i + 1) * self.cols])}\n"
        return result



class Matrix2Error(Exception):
    pass

class Matrix2BadNumberError(Matrix2Error):
    def __init__(self, bad_arg):
        self.bad_arg = bad_arg
        super().__init__(f"Введено не целое число '{self.bad_arg}'!")

class Matrix2NotTupleError(Matrix2Error):
    def __init__(self, bad_arg):
        self.bad_arg = bad_arg
        super().__init__(f"Введенный аргумент - '{self.bad_arg.__class__.__name__}', должен быть 'tuple'!")

class Matrix2BadTupleError(Matrix2Error):
    def __init__(self, bad_arg):
        self.bad_args = [elem for elem in bad_arg if not isinstance(elem, tuple)]
        super().__init__(f"Кортеж содержит элементы, не являющиеся кортежами '{self.bad_args}'!")

class Matrix2TupleSizeError(Matrix2Error):
    def __init__(self, bad_arg):
        self.bad_args = [len(elem) for elem in bad_arg]
        super().__init__(f"Кортеж содержит кортежи не одинакового размера '{self.bad_args}'!")

class Matrix2BadSizeError(Matrix2Error):
    def __init__(self, *matrix):
        self.matrix = matrix
        super().__init__(f"Матрицы разного размера: '{self.matrix[0].rows}*{self.matrix[0].cols}' "
                         f"и '{self.matrix[1].rows}*{self.matrix[1].cols}'!")

class Matrix2BadInstanceError(Matrix2Error):
    def __init__(self, *matrix):
        self.matrix = matrix
        super().__init__(f"Аргумент - экземпляр класса '{matrix[1].__class__.__name__}', "
                         f"должен быть '{matrix[0].__class__.__name__}'!")


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
            raise Matrix2BadNumberError(number)

    @staticmethod
    def __check_matrix(matrix: tuple) -> bool:
        """Проверяет, является ли введенный аргумент кортежем кортежей правильного размера."""
        if not isinstance(matrix, tuple):
            raise Matrix2NotTupleError(matrix)
        elif not all([True if isinstance(elem, tuple) else False for elem in matrix]):
            raise Matrix2BadTupleError(matrix)
        elif not all([True if len(elem) == len(matrix[0]) else False for elem in matrix]):
            raise Matrix2TupleSizeError(matrix)
        else:
            return True

    @staticmethod
    def __compare_matrix(matrix1, matrix2) -> bool:
        """Проверяет, является ли матрица экземпляром класса, проверяет равенство размеров 2-х матриц."""
        if isinstance(matrix2, Matrix2):
            if matrix1.rows == matrix2.rows and matrix1.cols == matrix2.cols:
                return True
            else:
                raise Matrix2BadSizeError(matrix1, matrix2)
        else:
            raise Matrix2BadInstanceError(matrix1, matrix2)

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



# m1_1 = Matrix1(3, 4, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
# m1_2 = Matrix1(3, 3, (1, 2, 3, 4, 5, 6, 7, 8, 9))
# m2_1 = Matrix2(((1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)))
# m2_2 = Matrix2(((2, 3, 4), (5, 6, 7), (8, 9, 10)))

# stdout:
# m1_bad = Matrix1(3, 3, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
# Traceback (most recent call last):
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 308, in <module>
#     m1_bad = Matrix1(3, 3, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
#              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 26, in __init__
#     raise MatrixElemSizeError1(rows * cols, len(matrix))
# MatrixElemSizeError1: Количество элементов матрицы '9' не соответствует ее размеру '12'!

# print(m1_1 * 1.2)
# Traceback (most recent call last):
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 308, in <module>
#     print(m1_1 * 1.2)
#           ~~~~~^~~~~
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 85, in __mul__
#     if self.__check_input(number):
#        ^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 47, in __check_input
#     raise MatrixBadNumberError1(number)
# MatrixBadNumberError1: Введено не целое число '1.2'!

# print(m1_1 + m1_2)
# raceback (most recent call last):
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 308, in <module>
#     print(m1_1 + m1_2)
#           ~~~~~^~~~~~
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 65, in __add__
#     if self.__check_matrix(self, matrix2):
#        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 57, in __check_matrix
#     raise MatrixBadSizeError1(matrix1, matrix2)
# MatrixBadSizeError1: Матрицы разного размера: '3*4' и '3*3'!

# print(m1_1 + m2_1)
# Traceback (most recent call last):
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 310, in <module>
#     print(m1_1 + m2_1)
#           ~~~~~^~~~~~
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 65, in __add__
#     if self.__check_matrix(self, matrix2):
#        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 60, in __check_matrix
#     raise MatrixBadInstanceError1(matrix1, matrix2)
# MatrixBadInstanceError1: Аргумент - экземпляр класса 'Matrix2', должен быть 'Matrix1'!

# print(m2_1 * 1.2)
# Traceback (most recent call last):
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 310, in <module>
#     print(m2_1 * 1.2)
#           ~~~~~^~~~~
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 258, in __mul__
#     if self.__check_input(number):
#        ^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 177, in __check_input
#     raise MatrixBadNumberError2(number)
# MatrixBadNumberError2: Введено не целое число '1.2'!

# m2_bad1 = Matrix2(7)
# Traceback (most recent call last):
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 314, in <module>
#     m2_bad1 = Matrix2(7)
#               ^^^^^^^^^^
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 146, in __init__
#     if self.__check_matrix(matrix):
#        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 184, in __check_matrix
#     raise MatrixNotTupleError2(matrix)
# MatrixNotTupleError2: Введенный аргумент - 'int', должен быть 'tuple'!

# m2_bad2 = Matrix2(((2, 3, 4), (5, 6, 7), (8, 9, 10), (11, 12, 13), 8, 'a'))
# Traceback (most recent call last):
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 313, in <module>
#     m2_bad2 = Matrix2(((2, 3, 4), (5, 6, 7), (8, 9, 10), (11, 12, 13), 8, 'a'))
#               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 146, in __init__
#     if self.__check_matrix(matrix):
#        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 187, in __check_matrix
#     raise MatrixBadTupleError2(matrix)
# MatrixBadTupleError2: Кортеж содержит элементы, не являющиеся кортежами '[8, 'a']'!

# m2_bad3 = Matrix2(((2, 3, 4), (5, 6, 7), (8, 9, 10), (11, 12, 13, 14)))
# Traceback (most recent call last):
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 314, in <module>
#     m2_bad3 = Matrix2(((2, 3, 4), (5, 6, 7), (8, 9, 10), (11, 12, 13, 14)))
#               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 146, in __init__
#     if self.__check_matrix(matrix):
#        ^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 190, in __check_matrix
#     raise MatrixTupleSizeError2(matrix)
# MatrixTupleSizeError2: Кортеж содержит кортежи не одинакового размера '[3, 3, 3, 4]'!

# print(m2_1 + m2_2)
# Traceback (most recent call last):
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 310, in <module>
#     print(m2_1 + m2_2)
#           ~~~~~^~~~~~
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 238, in __add__
#     if self.__compare_matrix(self, matrix2):
#        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 202, in __compare_matrix
#     raise MatrixBadSizeError2(matrix1, matrix2)
# MatrixBadSizeError2: Матрицы разного размера: '4*3' и '3*3'!

# print(m2_1 + m1_1)
# Traceback (most recent call last):
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 310, in <module>
#     print(m2_1 + m1_1)
#           ~~~~~^~~~~~
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 238, in __add__
#     if self.__compare_matrix(self, matrix2):
#        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "D:\Step\python\rep\Muhomorov\11.16\1.py", line 205, in __compare_matrix
#     raise MatrixBadInstanceError2(matrix1, matrix2)
# MatrixBadInstanceError2: Аргумент - экземпляр класса 'Matrix1', должен быть 'Matrix2'!
