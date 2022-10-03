"""Модуль для вывода сообщения."""
from shutil import get_terminal_size as gts

def important_message(msg: str) -> None:
    """Выводит в терминал сообщение, обрамленное рамкой"""
    columns = gts()[0] - 2
    border = f"#{'=' * columns}#"
    line = f"#{' ' * columns}#"
    msg_len = len(msg)
    print(f"{border}\n{line}")
    if msg_len >= columns:
        n = msg_len // columns
        for _ in range(n + 1):
            print(f"#  {msg[:columns - 4].ljust(columns - 2)}#")
            msg = msg[columns - 4:]
    else:
        print(f"#  {msg.ljust(columns - 2)}#")
    print(f"{line}\n{border}")
    

