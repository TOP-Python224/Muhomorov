class Matrix1:
    """
    Описывает матрицу.
    Элементы матрицы хранятся в атрибутах.
    """
    def __init__(self,
                 rows: int,
                 cols: int,
                 # ИСПРАВИТЬ: неудачный выбор параметра для конструктора (см. комментарий на строке )
                 *args: int) -> None:
        """
        :param rows: количество строк матрицы,
        :param cols: количество столбцов матрицы,
        :param args: элементы матрицы через запятую, их количество должно быть равно произведению количества строк на количество столбцов матрицы.
        """
        for elem in (rows, cols) + args:
            # ИСПРАВИТЬ здесь и далее: явного употребления имени класса лучше избегать: из-за этого начнутся проблемы в сложных моделях, использующих наследование — а статические методы можно вызывать и от self, при условии, что метод декорирован как статический
            if Matrix1.__check_input(elem):
                if len(args) == rows * cols:
                    self.__rows = rows
                    self.__cols = cols
                    # ИСПРАВИТЬ: насколько я вижу, вы не изменяете элементы этого атрибута — значит, список избыточен
                    self.__data = list(args)
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
    def data(self) -> list:
        return self.__data

    # ИСПРАВИТЬ: здесь вы написали статический метод, следовательно нужно добавить соответствующий декоратор
    def __check_input(number: int) -> bool:
        """Проверяет, является ли введенное число целым."""
        if isinstance(number, int):
            return True
        else:
            raise TypeError('Введено не целое число!')

    # ИСПРАВИТЬ здесь и далее: зря исправили на self, в данном методе речь о сравнении атрибутов двух матриц, а значит удобно именовать первый параметр именно matrix1 — возвращайте всё взад =)
    def __check_matrix(self, matrix2) -> bool:
        """Проверяет, является ли матрица экземпляром класса, проверяет равенство размеров 2-х матриц."""
        if isinstance(matrix2, Matrix1):
            if self.rows == matrix2.rows and self.cols == matrix2.cols:
                return True
            else:
                raise TypeError('Матрицы разного размера!')
        else:
            raise TypeError('Аргумент не является экземпляром класса!')

    # Непонятно, как аннотировать вывод функции как объект класса?
    # ИСПОЛЬЗОВАТЬ: в 3.10 для такой аннотации мы пишем имя класса и берём его в кавычки — также, как для ещё необъявленного класса (например, для такого, который объявляется позже в коде); в 3.11 для аннотации возврата экземпляра собственного класса введён специальный объект Self
    def __add__(self, matrix2) -> str:
        """Производит поэлементное сложение 2-х матриц."""
        if Matrix1.__check_matrix(self, matrix2):
            result = list(map(
                lambda e1, e2: e1 + e2,
                self.data,
                matrix2.data
            ))
            return Matrix1(self.rows, self.cols, *result)

    def __sub__(self, matrix2) -> str:
        """Производит поэлементное вычитание 2-х матриц."""
        if Matrix1.__check_matrix(self, matrix2):
            result = list(map(
                lambda e1, e2: e1 - e2,
                self.data,
                matrix2.data
            ))
            return Matrix1(self.rows, self.cols, *result)

    def __mul__(self, number) -> str:
        """Производит умножение элементов матрицы на число."""
        if Matrix1.__check_input(number):                
            result = [
                elem * number
                for elem in self.__data
            ]
            return Matrix1(self.rows, self.cols, *result)
    
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


# ИСПРАВИТЬ: общая проблема с этим классом заключается в том, что вы, судя по всему, максимально подгоняли структуру атрибутов под написанные для предыдущего класса методы — а задача стояла ровно противоположная: придумать новую структуру атрибутов и для неё написать новые методы — после чего сравнить основные методы всех получившихся классов; и вариантов куда больше, чем два =)
class Matrix2:
    """
    Описывает матрицу.
    Элементы матрицы хранятся в словаре. Сильно надуманный вариант.
    """
    # КОММЕНТАРИЙ: конструкторы также могут заметно отличаться
    def __init__(self,
                 rows: int,
                 cols: int, 
                 *args: int) -> None:
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
    def data(self) -> list:
        return self.__v

    def __check_input(number: int) -> bool:
        """Проверяет, является ли введенное число целым."""
        if isinstance(number, int):
            return True
        else:
            raise TypeError('Введено не целое число!')
    
    def __check_matrix(self, matrix2) -> bool:
        """Проверяет, является ли матрица экземпляром класса, проверяет равенство размеров 2-х матриц."""
        if isinstance(matrix2, Matrix2):
            if self.rows == matrix2.rows and self.cols == matrix2.cols:
                return True
            else:
                raise TypeError('Матрицы разного размера!')
        else:
            raise TypeError('Аргумент не является экземпляром класса!')
    
    def __add__(self, matrix2) -> str:
        """Производит поэлементное сложение 2-х матриц."""
        if Matrix2.__check_matrix(self, matrix2):
            result = list(map(
                lambda e1, e2: e1 + e2,
                self.data,
                matrix2.data
            ))
            return Matrix2(self.rows, self.cols, *result)

    def __sub__(self, matrix2) -> str:
        """Производит поэлементное вычитание 2-х матриц."""
        if Matrix2.__check_matrix(self, matrix2):
            result = list(map(
                lambda e1, e2: e1 - e2,
                self.data,
                matrix2.data
            ))
            return Matrix2(self.rows, self.cols, *result)

    def __mul__(self, number) -> str:
        """Производит умножение элементов матрицы на число."""
        if Matrix2.__check_input(number):                
            result = [
                elem * number
                for elem in self.data
            ]
            return Matrix2(self.rows, self.cols, *result)
    
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


# КОММЕНТАРИЙ: здесь же неотличимы аргументы, являющиеся размерами матрицы, от аргументов, являющихся элементами матрицы; мы так упорно изучали параметризацию функций как раз для того, чтобы не допускать таких вызовов
m1 = Matrix1(3, 4, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
m2 = Matrix1(3, 4, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
# КОММЕНТАРИЙ: не лень было ещё сорок чисел набирать?))
m3 = Matrix2(4, 5, *range(1, 21))
m4 = Matrix2(4, 5, *range(2, 22))
print(m1)
print(m1 + m2)
print(m1 - m2)
print(m1 * 10)
print(m3 + m4)
print(m3 - m4)
print(m3 * 7)


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
