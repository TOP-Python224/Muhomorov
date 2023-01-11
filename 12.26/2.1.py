from abc import ABC
from random import choice
from typing import Optional
from typing import Self
from enum import Enum


class Codes(Enum):
    """Предоставляет справочник кодов ответа вэб-сервера."""
    OK = '200'
    MOVED = '301'
    FORBIDDEN = '403'
    NOT_FOUND = '404'
    BAD_GATEWAY = '502'


class WebServer:
    """Возвращает случайно выбранный ответ вэб-сервера с кодом."""
    def __init__(self):
        self.answers = [
            (f"HTTP/1.1 {Codes.OK.value} OK", 'Payload'),
            (f"HTTP/1.1 {Codes.MOVED.value} Moved Permanently", 'Payload'),
            (f"HTTP/1.1 {Codes.FORBIDDEN.value} Forbidden", 'Payload'),
            (f"HTTP/1.1 {Codes.NOT_FOUND.value} Not Found", 'Payload'),
            (f"HTTP/1.1 {Codes.BAD_GATEWAY.value} Bad Gateway", 'Payload')
        ]

    def get(self):
        return choice(self.answers)


class CodeChecker(ABC):
    """Базовый класс обработчиков, являющийся корневым элементом цепочки обработчиков и предоставляющий методы
    для прохождения по всем элементам цепочки."""
    def __init__(self, code: tuple[str, str]):
        self.code = code
        self.next_checker: Optional[CodeChecker] = None

    def add_checker(self, checker: Self):
        if self.next_checker is None:
            self.next_checker = checker
        else:
            self.next_checker.add_checker(checker)

    def handle(self):
        if self.next_checker:
            self.next_checker.handle()


class CodeOkChecker(CodeChecker):
    """При наличии кода 200 в ответе вэб-сервера, выводит сообщение и прерывает цепочку команд,
    иначе передает код следующему обработчику в цепочке."""
    def handle(self):
        if Codes.OK.value in self.code[0]:
            print(f"{self.__class__.__name__} - {Codes.OK.value}")
        else:
            super().handle()


class CodeMovedPermChecker(CodeChecker):
    """При наличии кода 301 в ответе вэб-сервера, выводит сообщение и прерывает цепочку команд,
    иначе передает код следующему обработчику в цепочке."""

    def handle(self):
        if Codes.MOVED.value in self.code[0]:
            print(f"{self.__class__.__name__} - {Codes.MOVED.value}")
        else:
            super().handle()


class CodeForbiddenChecker(CodeChecker):
    """При наличии кода 403 в ответе вэб-сервера, выводит сообщение и прерывает цепочку команд,
    иначе передает код следующему обработчику в цепочке."""
    def handle(self):
        if Codes.FORBIDDEN.value in self.code[0]:
            print(f"{self.__class__.__name__} - {Codes.FORBIDDEN.value}")
        else:
            super().handle()


class CodeNotFoundChecker(CodeChecker):
    """При наличии кода 404 в ответе вэб-сервера, выводит сообщение и прерывает цепочку команд,
    иначе передает код следующему обработчику в цепочке."""
    def handle(self):
        if Codes.NOT_FOUND.value in self.code[0]:
            print(f"{self.__class__.__name__} - {Codes.NOT_FOUND.value}")
        else:
            super().handle()


class CodeBadGatewayChecker(CodeChecker):
    """При наличии кода 502 ответе вэб-сервера, выводит сообщение и прерывает цепочку команд,
    иначе передает код следующему обработчику в цепочке."""
    def handle(self):
        if Codes.BAD_GATEWAY.value in self.code[0]:
            print(f"{self.__class__.__name__} - {Codes.BAD_GATEWAY.value}")
        else:
            super().handle()


ws = WebServer()
answer = ws.get()
cc = CodeChecker(answer)
cc.add_checker(CodeOkChecker(answer))
cc.add_checker(CodeMovedPermChecker(answer))
cc.add_checker(CodeForbiddenChecker(answer))
cc.add_checker(CodeNotFoundChecker(answer))
cc.add_checker(CodeBadGatewayChecker(answer))
cc.handle()


# stdout:
# CodeForbiddenChecker - 403
