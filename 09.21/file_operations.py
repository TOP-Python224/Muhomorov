from pathlib import Path
from shutil import copy


# ИСПОЛЬЗОВАТЬ: в имени параметра функции особенно важно указать, что вы ожидаете: путь или файлоподобный объект
def return_file(lostfile_path: Path) -> None:
    """Осуществляет копирование потерянного файла в каталог к основным файлам."""
    curr_dir = Path.cwd()
    copy(lostfile_path, curr_dir)
