from os import cpu_count
from pathlib import Path
from shutil import copy

def return_file(lostfile: Path) -> None:
    """Осуществляет копирование потерянного файла в каталог к основным файлам."""
    curr_dir = Path.cwd()
    copy(lostfile, curr_dir)
