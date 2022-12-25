"""Демонстратор строителя."""
from typing import Self

class HTMLTag:
    """
    Описывает HTML тег, который может содержать вложенные теги.
    Может быть инициализирован с помощью строителя.
    """
    default_indent_spaces: int = 2

    def __init__(self, name: str, value: str = ''):
        self.name = name
        self.value = value
        self.__nested: list[HTMLTag] = []

    @property
    def nested(self):
        """Возвращает неиндексируемый итератор по всем вложенным тегам."""
        return iter(self.__nested)

    @nested.setter
    def nested(self, value: 'HTMLTag'):
        """Добавляет вложенный тег к текущему."""
        self.__nested += [value]

    def __str(self, indent_level: int) -> str:
        """Рекурсивно формирует строку с текущим и всеми вложенными тегами."""
        margin = ' ' * indent_level * self.default_indent_spaces
        eol = ''
        result = f"{margin}<{self.name}>{self.value}"
        if self.__nested:
            for tag in self.__nested:
                result += '\n' + tag.__str(indent_level+1)
            eol = f'\n{margin}'
        result += f"{eol}</{self.name}>"
        return result

    def __str__(self):
        return self.__str(0)

    # в данной реализации нецелесообразно "прятать" класс HTMLBuilder
    @staticmethod
    def create(name: str, value: str = ''):
        return HTMLBuilder(name, value)


class HTMLBuilder:
    """
    Предоставляет методы для пошаговой инициализации экземпляра HTMLTag.
    """
    def __init__(self, root: HTMLTag | str, value: str = ''):
        if isinstance(root, HTMLTag):
            self.root = root
        elif isinstance(root, str):
            self.root = HTMLTag(root, value)
        else:
            raise TypeError('use HTMLTag or str instance for root parameter')

    def nested(self, name: str, value: str = '') -> 'HTMLBuilder':
        """Добавляет вложенный тег к текущему тегу и возвращает строитель для вложенного тега."""
        tag = HTMLTag(name, value)
        self.root.nested = tag
        return HTMLBuilder(tag)

    def sibling(self, name: str, value: str = '') -> 'HTMLBuilder':
        """Добавляет вложенный тег к текущему тегу и возвращает текущий строитель."""
        tag = HTMLTag(name, value)
        self.root.nested = tag
        return self

    def build(self) -> HTMLTag:
        return self.root


class CVBuilder:
    """Описывает HTML документ портфолио человека."""
    def __init__(self,
                 fio: str,
                 age: int,
                 profession: str,
                 email: str):
        self.fio = fio
        self.age = age
        self.profession = profession
        self.email = email
        self.education = ()
        self.projects = []
        self.contacts = {}

    def add_education(self, *args) -> Self:
        self.education = args
        return self

    def add_project(self, *args) -> Self:
        self.projects += args,
        return self

    def add_contact(self, **kwargs) -> Self:
        self.contacts.update(kwargs)
        return self

    def build(self) -> 'HTMLTag':
        root = HTMLTag.create('html')

        result = root.nested('head')\
                     .sibling('title', f"{self.fio}: портфолио")\
                     .nested('body')\
                     .nested('div')\
                     .sibling('h2', 'Обо мне') \
                     .sibling('p', f"Ф.И.О.:{self.fio}, "
                                   f"Возраст: {self.age}, "
                                   f"профессия: {self.profession}, "
                                   f"email: {self.email}")

        if self.education:
            result.sibling('h2', 'Образование') \
                  .sibling('p', f"Учебное заведение: {self.education[0]}, "
                                f"факультет: {self.education[1]}, "
                                f"год окончания: {self.education[2]}")

        if self.projects:
            project_items = ''
            for project in self.projects:
                project_items += f'<a href="{project[1]}">{project[0]}</a>'
            result.sibling('h2', 'Проекты') \
                  .sibling('p', project_items) \

        contacts_items = ', '.join([f"{k}: {v}" for k, v in self.contacts.items()])
        result.sibling('h2', 'Контакты') \
              .sibling('p', contacts_items)

        full_result = root.build()
        return full_result


cv1 = CVBuilder('Иванов Иван Иванович', 26, 'художник-фрилансер', 'ivv@abc.de')\
    .add_education('Архитектурная Академия', 'Компьютерный дизайн', 2019)\
    .add_project('Разработка логотипа для компании по производству снеков', 'url1')\
    .add_project('UI разработка для интернет-магазина для восковых дел мастеров', 'url2')\
    .add_contact(telegram='@ivovuvan', icq='123456789')
cv1 = cv1.build()
print(cv1)


