from pathlib import Path
from file_operations import return_file


# ИСПОЛЬЗОВАТЬ: есть, конечно, мнение о том, что полное имя файла — это полный абсолютный путь к файлу — но всё же лучше уточнить
lost_file = Path(input('Введите абсолютный путь к файлу: '))
return_file(lost_file)

import lost_file


# stdout:
# Введите имя файла: D:\Step\python\ДЗ\09.21\# folder\lost_file.py
# lost_file.py: Я нашёлся!


# ИТОГ: отлично — 4/4
