from pathlib import Path
from file_operations import return_file


lost_file = Path(input('Введите имя файла: '))
return_file(lost_file)

import lost_file


# stdout:
# Введите имя файла: D:\Step\python\ДЗ\09.21\# folder\lost_file.py
# lost_file.py: Я нашёлся!
