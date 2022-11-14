# Элементы матрицы хранятся в атрибутах.
class Matrix1:
    """Описывает матрицу."""
    def __init__(self, rows: int, 
                 cols: int, 
                 *args: tuple[int]) -> None:
        """
        :param rows: количество строк матрицы,
        :param cols: количество столбцов матрицы,
        :param args: элементы матрицы через запятую, их количество должно быть равно произведению количества строк на количество столбцов матрицы.
        """
        for elem in (rows, cols) + args:
            if Matrix1.__check_input(elem):
                if len(args) == rows * cols:
                    self.__rows = rows
                    self.__cols = cols
                    self.__data = list(args)
                else:
                    raise TypeError('Количество элементов матрицы не соответствует ее размеру!')
        
    @property
    def rows(self) -> int:
        return self.__rows

    @property
    def cols(self) -> int:
        return self.__cols

    @property
    def data(self) -> int:
        return self.__data

    def __check_input(number: int) -> bool:
        """Проверяет является ли введенное число целым."""
        if isinstance(number, int):
            return True
        else:
            raise TypeError('Введено не целое число!')
    
    def __check_matrix(matrix1, matrix2) -> bool:
        """Проверяет является ли матрица экземпляром класса, проверяет равенство размеров 2-х матриц."""
        if isinstance(matrix2, Matrix1):
            if matrix1.rows == matrix2.rows and matrix1.cols == matrix2.cols:
                return True
            else:
                raise TypeError('Матрицы разного размера!')
        else:
            raise TypeError('Аргумент не является экземпляром класса!')
    
    def __add__(matrix1, matrix2) -> str:
        """Производит поэлементное сложение 2-х матриц."""
        if Matrix1.__check_matrix(matrix1, matrix2):
            result = list(map(lambda e1, e2: e1 + e2, matrix1.data, matrix2.data))
            return Matrix1(matrix1.rows, matrix1.cols, *result)

    def __sub__(matrix1, matrix2) -> str:
        """Производит поэлементное вычитание 2-х матриц."""
        if Matrix1.__check_matrix(matrix1, matrix2):
            result = list(map(lambda e1, e2: e1 - e2, matrix1.data, matrix2.data))
            return Matrix1(matrix1.rows, matrix1.cols, *result)

    def __mul__(matrix, number) -> str:
        """Производит умножение элементов матрицы на число."""
        if Matrix1.__check_input(number):                
            result = [elem * number for elem in matrix.__data]
            return Matrix1(matrix.rows, matrix.cols, *result)
    
    def __str__(self) -> str:
        max_width = len(str(max(self.data)))
        centered_matrix = [
        str(elem).rjust(max_width + 1)
        for elem in self.data
        ]
        result = ''
        for i in range(self.rows):
            result += f"{''.join(centered_matrix[i*self.cols: (i+1)*self.cols])}\n"
        return result

# Элементы матрицы храняться в словаре. Сильно надуманный вариант.
class Matrix2:
    """Описывает матрицу."""
    def __init__(self, rows: int, 
                 cols: int, 
                 *args: tuple[int]) -> None:
        """
        :param rows: количество строк матрицы,
        :param cols: количество столбцов матрицы,
        :param args: элементы матрицы через запятую, их количество должно быть равно произведению количества строк на количество столбцов матрицы.
        """
        for elem in (rows, cols) + args:
            if isinstance(elem, int):
                if len(args) == rows * cols:
                    self.__data = {(rows, cols): list(args)}
                else:
                    raise TypeError('Количество элементов матрицы не соответствует ее размеру!')
            else:
                raise TypeError('Введено не целое число!')

        for elem in self.__data.items():
            self.__k, self.__v = elem

    @property
    def rows(self) -> int:
        return self.__k[0]

    @property
    def cols(self) -> int:
        return self.__k[1]

    @property
    def data(self) -> int:
        return self.__v

    def __check_input(number: int) -> bool:
        """Проверяет является ли введенное число целым."""
        if isinstance(number, int):
            return True
        else:
            raise TypeError('Введено не целое число!')
    
    def __check_matrix(matrix1, matrix2) -> bool:
        """Проверяет является ли матрица экземпляром класса, проверяет равенство размеров 2-х матриц."""
        if isinstance(matrix2, Matrix2):
            if matrix1.rows == matrix2.rows and matrix1.cols == matrix2.cols:
                return True
            else:
                raise TypeError('Матрицы разного размера!')
        else:
            raise TypeError('Аргумент не является экземпляром класса!')
    
    def __add__(matrix1, matrix2) -> str:
        """Производит поэлементное сложение 2-х матриц."""
        if Matrix2.__check_matrix(matrix1, matrix2):
            result = list(map(lambda e1, e2: e1 + e2, matrix1.data, matrix2.data))
            return Matrix2(matrix1.rows, matrix1.cols, *result)

    def __sub__(matrix1, matrix2) -> str:
        """Производит поэлементное вычитание 2-х матриц."""
        if Matrix2.__check_matrix(matrix1, matrix2):
            result = list(map(lambda e1, e2: e1 - e2, matrix1.data, matrix2.data))
            return Matrix2(matrix1.rows, matrix1.cols, *result)

    def __mul__(matrix, number) -> str:
        """Производит умножение элементов матрицы на число."""
        if Matrix2.__check_input(number):                
            result = [elem * number for elem in matrix.data]
            return Matrix2(matrix.rows, matrix.cols, *result)
    
    def __str__(self) -> str:
        max_width = len(str(max(self.data)))
        centered_matrix = [
        str(elem).rjust(max_width + 1)
        for elem in self.data
        ]
        result = ''
        for i in range(self.rows):
            result += f"{''.join(centered_matrix[i*self.cols: (i+1)*self.cols])}\n"
        return result


# m1 = Matrix1(3, 4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
# m2 = Matrix1(3, 4, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
# m3 = Matrix2(4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
# m4 = Matrix2(4, 5, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21)
# print(m1)
# print(m1 + m2)
# print(m1 - m2)
# print(m1 * 10)
# print(m3 + m4)
# print(m3 - m4)
# print(m3 * 7)

#stdout:
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