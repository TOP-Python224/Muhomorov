from dataclasses import dataclass

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
    def __init__(self, folder: str):
        super().__init__()
        self.folder = folder

        # УДАЛИТЬ: здесь не нужна привязка к реальной файловой системе
        for root, dirs, files in os.walk(self.folder):
            for file in files:
                self.append(f"{root}{PATH_SEP}{file}")

    # КОММЕНТАРИЙ: это задание на шаблон Компоновщик — подумайте в этом контексте

    # ДОБАВИТЬ: свой метод и/или переопределение встроенного — для добавления объектов к каталогу

    def ls(self) -> str:
        return '\n'.join(self)


def ls(*objects: File | Folder, end='\n') -> None:
    for obj in objects:
        print(obj.ls(), end)


f1 = File('text_1.txt', 'd:\\test_1')
f2 = File('text_2.txt', 'd:\\test_2')
d1 = Folder('d:\\test_1')
d2 = Folder('d:\\test_2')
ls(f1, f2, d1, d2)


# stdout:

# d:\test_1\text_1.txt
#
# d:\test_2\text_2.txt
#
# d:\test_1\text_1.txt
# d:\test_1\text_2.txt
# d:\test_1\test_1\text_3.txt
# d:\test_1\test_2\text_4.txt
# d:\test_1\test_2\test_3\text_5.txt
#
# d:\test_2\text_1.txt
# d:\test_2\text_2.txt
# d:\test_2\test_1\text_3.txt
# d:\test_2\test_2\text_4.txt
# d:\test_2\test_2\test_3\text_5.txt


# ИТОГ: выполнить работу над ошибками — 2/6
