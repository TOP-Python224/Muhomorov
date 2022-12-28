from typing import Self


class HTMLTag:
    """
    Описывает HTML тег, который может содержать вложенные теги.
    Может быть инициализирован с помощью строителя.
    """
    default_indent_spaces: int = 2

    def __init__(self, name: str, value: str = ''):
        self.name = name
        # ДОБАВИТЬ: в задании было сказано использовать класс HTMLTag из предыдущей задачи — с атрибутами, они пригодятся для вёрстки
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

    # ДОБАВИТЬ: в задании было сказано использовать класс HTMLBuilder из предыдущей задачи — с возможностью добавления атрибутов, они пригодятся для вёрстки

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

    # КОММЕНТАРИЙ: удобство использования таких дополнительных методов, как три метода ниже, во многом зависит от того, как вы настроите их сигнатуры — здесь вы предлагаете тому, кто будет их использовать, передавать какие угодно аргументы в каком угодно порядке: следовательно кому-то может захотеться передать сюда явно не учитываемые вами значения и/или типы

    # ДОБАВИТЬ: документацию к методам с описанием параметров
    #  https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html

    def add_education(self, *args) -> Self:
        # ИСПРАВИТЬ: а если необходимо указать несколько учебных заведений? мы выделяем этот раздел в отдельный метод как раз затем, чтобы пользователь класса имел возможность использовать его произвольное количество раз
        self.education = args
        return self

    # ИСПРАВИТЬ: мне представляется, что параметры данного метода стоит раскрыть уже потому, что в методе build() вы используете содержимое каждого кортежа довольно определённым образом: заголовок и ссылка — но при этом нигде и никак не обозначаете, что планируете использовать второй по счёту аргумент в качестве значения для атрибута href тега <a>, а первый аргумент — в качестве значения для тега <a>
    def add_project(self, *args) -> Self:
        self.projects += args,
        return self

    def add_contact(self, **kwargs) -> Self:
        self.contacts.update(kwargs)
        return self

    def build(self) -> 'HTMLTag':
        root = HTMLTag.create('html')

        # ИСПРАВИТЬ: это очень ленивая сборка, вы не реализовали даже минимальную вёрстку, которую я просил — добавьте экспорт в .html да посмотрите, как это выглядит на рендере, ну грустно же

        # ИСПРАВИТЬ: тег <head> должен быть закрыт, после чего на одном уровне с ним должен быть расположен тег <body> — оба вложены в тег <html>
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
            # ИСПРАВИТЬ: ваша уверенность, что элементы в кортеже self.education расположены именно в этом порядке, не имеет основания
            result.sibling('h2', 'Образование') \
                  .sibling('p', f"Учебное заведение: {self.education[0]}, "
                                f"факультет: {self.education[1]}, "
                                f"год окончания: {self.education[2]}")

        if self.projects:
            project_items = ''
            for project in self.projects:
                # ИСПРАВИТЬ: аналогично про содержимое кортежа project
                project_items += f'<a href="{project[1]}">{project[0]}</a>'
            # ИСПРАВИТЬ: два проекта в один абзац, серьёзно?
            result.sibling('h2', 'Проекты') \
                  .sibling('p', project_items) \

        contacts_items = ', '.join([f"{k}: {v}" for k, v in self.contacts.items()])
        result.sibling('h2', 'Контакты') \
              .sibling('p', contacts_items)

        full_result = root.build()
        return full_result

    # КОММЕНТАРИЙ: у вас получился очень наглядный пример совершенно не очевидного в использовании класса: чтобы разобраться, как он работает, надо либо лезть в отдельную документацию (если она есть), либо в исходники — это возможная, но далеко не лучшая практика разработки: старайтесь её избегать


cv1 = CVBuilder('Иванов Иван Иванович', 26, 'художник-фрилансер', 'ivv@abc.de')\
    .add_education('Архитектурная Академия', 'Компьютерный дизайн', 2019)\
    .add_project('Разработка логотипа для компании по производству снеков', 'url1')\
    .add_project('UI разработка для интернет-магазина для восковых дел мастеров', 'url2')\
    .add_contact(telegram='@ivovuvan', icq='123456789')
cv1 = cv1.build()
print(cv1)


# ДОБАВИТЬ: stdout


# ИТОГ: задача явно требует доработки, сделайте её — 6/12
