from pathlib import Path

directory = Path(input('path: '))

def show_files(dir: str) -> tuple[str]:
    """Выводит список файлов в принятом каталоге."""
    result = ()
    for elem in dir.iterdir():
        if Path.is_file(elem):
            result += (elem.name, )
    print(result)
    return result

show_files(directory)

# stdout:
# PS D:\Step\python\ДЗ\09.19> py .\2.py
# path: C:\Python310
# ('LICENSE.txt', 'NEWS.txt', 'python.exe', 'python3.dll', 'python310.dll', 'pythonw.exe', 'vcruntime140.dll', 'vcruntime140_1.dll')