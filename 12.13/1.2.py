class HTMLTag:
    """
    Описывает HTML тег, который может содержать вложенные теги.
    Может быть инициализирован с помощью строителя.
    """
    default_indent_spaces: int = 2

    def __init__(self, name: str, value: str = '', **kwargs):
        self.name = name
        # ИСПОЛЬЗОВАТЬ: пример того, как с помощью реорганизации формирования строки избежать лишней проверки
        self.tag_attrs = ''.join([f' {k.replace("class_", "class")}="{v}"' for k, v in kwargs.items()])
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
        result = (f"{margin}<{self.name}"
                  # ИСПОЛЬЗОВАТЬ: вот эта проверка на самом деле не нужна
                  # f"{' ' if self.tag_attrs else ''}"
                  f"{self.tag_attrs}>"
                  f"{self.value}")
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
    def create(name: str, value: str = '', **kwargs):
        return HTMLBuilder(name, value, **kwargs)


class HTMLBuilder:
    """
    Предоставляет методы для пошаговой инициализации экземпляра HTMLTag.
    """
    def __init__(self, root: HTMLTag | str, value: str = '', **kwargs):
        if isinstance(root, HTMLTag):
            self.root = root
        elif isinstance(root, str):
            self.root = HTMLTag(root, value, **kwargs)
        else:
            raise TypeError('use HTMLTag or str instance for root parameter')

    def nested(self, name: str, value: str = '', **kwargs) -> 'HTMLBuilder':
        """Добавляет вложенный тег к текущему тегу и возвращает строитель для вложенного тега."""
        tag = HTMLTag(name, value, **kwargs)
        self.root.nested = tag
        return HTMLBuilder(tag)

    def sibling(self, name: str, value: str = '', **kwargs) -> 'HTMLBuilder':
        """Добавляет вложенный тег к текущему тегу и возвращает текущий строитель."""
        tag = HTMLTag(name, value, **kwargs)
        self.root.nested = tag
        return self

    def build(self) -> HTMLTag:
        return self.root


root = HTMLTag.create('div', id='bottom')
# ДОБАВИТЬ: многие HTML теги используют атрибут class, а в python это слово является зарезервированным — как с помощью строителя создать экземпляр HTMLTag с атрибутом class?
# Используем class_, заменяем на class в конструкторе HTMLTag.
root.sibling('p', 'Menu', id='main', section='top')\
    .nested('ul', section='middle')\
    .sibling('li', 'File', style='modern')\
    .sibling('li', 'Edit', class_='new')\
    .sibling('li', 'View')
div = root.build()
print(div)


# stdout:
# <div id="bottom">
#   <p id="main" section="top">Menu</p>
#   <ul section="middle">
#     <li style="modern">File</li>
#     <li class="new">Edit</li>
#     <li>View</li>
#   </ul>
# </div>


# ИТОГ: очень хорошо — 3/3
