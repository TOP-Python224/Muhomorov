from dataclasses import dataclass
from typing import Self

import os


if os.name == 'nt':
    PATH_SEP = '\\'
else:
    PATH_SEP = '/'


@dataclass
class File:
    """Файл в файловой системе."""
    name: str
    dir: str

    @property
    def extension(self) -> str:
        return self.name.rsplit('.', 1)[-1]

    def ls(self) -> str:
        return self.dir + PATH_SEP + self.name


class Folder(list):
    """Каталог в файловой системе. Может содержать вложенные каталоги и файлы."""
    def __init__(self, name: str, /, *objects: File | Self):
        super().__init__()
        self.name = name
        self.extend(objects)
        # УДАЛИТЬ: здесь не нужна привязка к реальной файловой системе
    # КОММЕНТАРИЙ: это задание на шаблон Компоновщик — подумайте в этом контексте
    # ДОБАВИТЬ: свой метод и/или переопределение встроенного — для добавления объектов к каталогу

    def ls(self) -> str:
        return '\n'.join([obj.ls() for obj in self])


def ls(*objects: File | Folder) -> str:
    for obj in objects:
        print(obj.ls())


file1 = File('text_1.txt', 'd:\\test_1')
file2 = File('text_2.txt', 'd:\\test_1')
file3 = File('text_3.doc', 'd:\\test_2')
file4 = File('text_4.doc', 'd:\\test_2')
file5 = File('text_5.rtf', 'd:\\test_3')
file6 = File('text_6.rtf', 'd:\\test_3')

d1 = Folder('test_2', file3, file4)
d2 = Folder('test_3', file5, file6, d1)
d3 = Folder('test_4', file1, file2, d2)
ls(d3)

# stdout:
# d:\test_1\text_1.txt
# d:\test_1\text_2.txt
# d:\test_3\text_5.rtf
# d:\test_3\text_6.rtf
# d:\test_2\text_3.doc
# d:\test_2\text_4.doc

# ИТОГ: выполнить работу над ошибками — 2/6
