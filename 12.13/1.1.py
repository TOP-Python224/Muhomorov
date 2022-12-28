from typing import Self


class ClassBuilder:
    """Класс Строитель для формирования текста кода класса с конструктором или без."""
    indent: int = 4*' '
    constructor: str = 'def __init__(self):'
    default_plug: str = 'pass'
    field: str = ''

    def __init__(self, class_name: str):
        self.result = f"class {class_name}:\n" \
                      f"{self.indent}{self.default_plug}\n"

    def add_field(self,
                  name: str,
                  value: str = '""') -> Self:
        """Добавляет поле в шаблон класса и возвращает текущий строитель."""
        self.result = self.result.replace(self.default_plug, self.constructor)
        # ДОБАВИТЬ: строковые литералы должны отображаться в кавычках (см. вывод ниже)
        self.field = f"{self.indent*2}{name} = {value}\n"
        self.result += self.field
        return self

    def __str__(self):
        return self.result


mc = ClassBuilder('MyClass')
mc.add_field('x', '10').add_field('y', 'тестовая строка').add_field('z', '30')
print(mc)


# stdout:
# class MyClass:
#     def __init__(self):
#         x = 10
#         y = тестовая строка
#         z = 30


# ИТОГ: хорошо — 4/5
