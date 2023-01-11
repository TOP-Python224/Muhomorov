import re


class HTMLParser:
    """
    Строитель для пошаговой обработки HTML документа.
    """
    single: set[str] = {'area', 'base', 'br', 'col', 'command', 'embed', 'hr', 'img', 'input', 'keygen', 'link', 'meta', 'param', 'source', 'track', 'wbr'}

    def __init__(self, html_doc: str):
        self.html = html_doc

    def add_eol(self, before_value: bool = True):
        pattern = re.compile(r'<(!-- )?/?\w+.*?( --)?>', re.S)
        bf = '\n' if before_value else ''
        return HTMLParser(pattern.sub(rf'\n\g<0>{bf}', self.html))

    def optimize_eol(self) -> 'HTMLParser':
        pattern = re.compile(r'\n{2,10}')
        return HTMLParser(pattern.sub('\n', self.html))

    def delete_eol(self) -> 'HTMLParser':
        pattern = re.compile(r'>\s*<')
        return HTMLParser(pattern.sub('><', self.html))

    def delete_empty(self) -> 'HTMLParser':
        pattern = re.compile(r'<(?P<tag>\w+?)>\s*</(?P=tag)>', re.S)
        return HTMLParser(pattern.sub('', self.html))

    def delete_tags(self, *tags: str) -> 'HTMLParser':
        """Важно: теги контейнеры удаляются вместе со всем содержимым, включая любые вложенные теги!"""
        q = self.html
        for tag in set(tags) - self.single:
            pat_op = re.compile(rf'<{tag}.*?>.*?<(?P<slash>/?){tag}', re.S)
            pat_cl = re.compile(rf'</{tag}.*?>.*?<(?P<slash>/?){tag}', re.S)
            lt = len(tag)
            while mo := pat_op.search(q):
                if mo:
                    sl = 1 if mo['slash'] else 0
                    start, i = mo.start(), mo.end() - (lt + sl + 1)
                    c = 1
                    while True:
                        if mo := pat_op.match(q, i):
                            sl = 1 if mo['slash'] else 0
                            i = mo.end() - (lt + sl + 1)
                            c += 1
                        elif mo := pat_cl.match(q, i):
                            sl = 1 if mo['slash'] else 0
                            if c > 1:
                                i = mo.end() - (lt + sl + 1)
                            elif c == 1:
                                i += lt + 3
                            c -= 1
                        else:
                            i += lt + 3
                            c -= 1
                        if not c:
                            break
                    q = q[:start] + q[i:]

        for tag in set(tags) & self.single:
            pattern = re.compile(rf'<{tag}.*?>', re.S)
            q = pattern.sub('', q)

        return HTMLParser(q)

    def delete_attrs(self, *attrs: str, all: bool = False) -> 'HTMLParser':
        q = self.html
        if all:
            # Исправил, выдавало исключение.
            # pattern = re.compile(r'<\w+?( .*?)?>', re.S)
            pattern = re.compile(r'<(?P<name>\w+?)( .*?)?>', re.S)
            q = pattern.sub(r'<\g<name>>', q)
        else:
            for attr_key in attrs:
                pattern = re.compile(rf'\s+?{attr_key}=\".*?\"')
                q = pattern.sub('', q)
        return HTMLParser(q)


class HTMLTag:
    """
    Описывает HTML тег, который может содержать вложенные теги.
    Может быть инициализирован с помощью строителя.
    """
    default_indent_spaces: int = 2

    def __init__(self, name: str, value: str = '', **kwargs):
        self.name = name
        self.value = value
        self.tag_attrs = ' '.join([f'{k}="{v}"' for k, v in kwargs.items()])
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
        result = f"{margin}<{self.name}" \
                 f"{' ' if self.tag_attrs else ''}" \
                 f"{self.tag_attrs}>" \
                 f"{self.value}"
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


class HTMLManager:
    """Реализует фасад для удобного взаимодействия с HTML элементами."""
    def __init__(self, input_html: str):
        self.html = input_html
        self.parser = HTMLParser(input_html)

    def squeeze(self) -> str:
        """Удаляет все символы пространства между тегами, а также пустые теги."""
        # ИСПОЛЬЗОВАТЬ: операцию атрибуции
        return self.parser.delete_eol().delete_empty().html

    def del_tags(self, *tags: str) -> str:
        """Удаляет заданные тег/теги."""
        return self.parser.delete_tags(*tags).__dict__['html']

    def del_attrs(self, *attrs: str, del_all: bool = False) -> str:
        """Удаляет заданные атрибут/атрибуты."""
        return self.parser.delete_attrs(*attrs, all=del_all).__dict__['html']

    # КОММЕНТАРИЙ: очень хорошо
    def add_indent(self) -> HTMLTag:
        """Добавляет символы пространства для формирования отступов вложенных тегов."""
        tags_lst = []
        html = self.parser.add_eol(before_value=True).html.lstrip('\n')
        tags = html.split('\n\n')
        root_tag = tags[0].strip('(<,>)')
        for tag in tags[1:]:
            sub_t = tag.split('\n')
            if '/' in sub_t[0]:
                pass
            elif len(sub_t) == 1:
                res = f"root.nested{sub_t[0].strip('(<,>)'), ''}"
                tags_lst.append(res)
            else:
                res = f".sibling{sub_t[0].strip('(<,>)'), *sub_t[1:-1]}"
                if tags_lst:
                    tags_lst[-1] = tags_lst[-1] + res
                else:
                    tags_lst.append(f"root{res}")
        root = HTMLTag.create(root_tag, '')
        # КОММЕНТАРИЙ: хотя я и предполагал, что вы будете пошагово работать строителем в самом методе — это тоже красиво =)
        for t in tags_lst:
            exec(t)
        # КОММЕНТАРИЙ: но имейте в виду на будущее, что для динамически формируемого и выполняемого кода чертовски сложно проводить тестирование и отладку — именно поэтому профессиональные разработчики не увлекаются такими конструкциями
        return root.build()


html1 = """<div>
  <p id='top'>Menu</p>
  <p>     </p>
  <ul>
    <li>File</li>
    
    <li>Edit</li>
    
    <li>View</li>
    
  </ul>
  <ul style='normal'>
    <li>File-1</li>
    <li>Edit-1</li>
    <li>View-1</li>
  </ul>
</div>"""

html2 = "<div><p id='top'>Menu</p><ul><li>File</li><li>Edit</li><li>View</li></ul><ul style='normal'><li>File-1</li><li>Edit-1</li><li>View-1</li></ul></div>"


# h2 = HTMLParser(html2).add_eol(before_value=True).optimize_eol()
# h1 = HTMLParser(html2).add_eol(before_value=True)
# print(h2.__dict__['html'])

print(HTMLManager(html1).squeeze(), end='\n====================\n')
# print(HTMLManager(html1).del_tags('p', 'li'), end='\n====================\n')
# print(HTMLManager(html1).del_attrs('id', 'style'), end='\n====================\n')
# print(HTMLManager(html1).del_attrs(del_all=True))

t1 = HTMLManager(html2).add_indent()
print(t1)

# stdout:
# <div><p id='top'>Menu</p><ul><li>File</li><li>Edit</li><li>View</li></ul><ul style='normal'><li>File-1</li><li>Edit-1</li><li>View-1</li></ul></div>
# ====================
# <div>
#   <p id='top'>Menu</p id='top'>
#   <ul>
#     <li>File</li>
#     <li>Edit</li>
#     <li>View</li>
#   </ul>
#   <ul style='normal'>
#     <li>File-1</li>
#     <li>Edit-1</li>
#     <li>View-1</li>
#   </ul style='normal'>
# </div>


# КОММЕНТАРИЙ: вот вам и будни проф.разработчика — куча кода, который так и зудит переписать, но это не твоя задача, а твоя задача заключается в том, чтобы собрать кучу не твоего кода в твоё собственное работающее нечто =) вы справились очень даже хорошо, я считаю


# ИТОГ: отлично — 8/8
