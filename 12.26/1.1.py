from datetime import datetime as dt
from random import randrange as rr, choice as ch
from string import ascii_lowercase as alc


class TestCase:
    """Адресат."""
    def __init__(self):
        self.messages = [
            ''.join(ch(alc) for _ in range(rr(3, 6)))
            for _ in range(1000)
        ]
        self.numbers = [
            (rr(10, 100) for _ in range(rr(4, 7)))
            for _ in range(1000)
        ]
        # ... другие поля?
        self.dict_ = dict(zip(
            (k for k in range(1000)),
            (rr(100, 1000) for _ in range(1000))
        ))

    def print_msg(self):
        msg = self.messages.pop()
        print(msg)
        return msg

    def sum_nums(self):
        nums = self.numbers.pop()
        print(sum(nums))
        return nums

    # ... другие методы?
    def sum_digits(self):
        item = self.dict_.popitem()
        print(sum(map(int, str(item[1]))))
        return item


class TestLogger:
    """Протоколирует все выполняемые команды."""
    log = []

    @classmethod
    def append_data(cls, data: str):
        cls.log.append(data)


# ИСПОЛЬЗОВАТЬ: собственные исключения для команды
class CommandError(Exception):
    pass


class TestCommand:
    """Команда."""
    def __init__(self, case: TestCase, method: str):
        self.case = case
        self.method = method
        self.pop_list = []
        self.undo_cnt = 0

    def __log(self, pop_elem: str, action: str) -> None:
        TestLogger.append_data(f"{dt.now():%Y-%m-%d %H:%M:%S} - {self.method} - {pop_elem} - {action}")

    def execute(self, redo: bool = False) -> None:
        action = ('POP', 'REDO')
        # КОММЕНТАРИЙ: докопались значит до этой конструкции..)) имейте в виду, она пока в обсуждении: баг-трекер и dev версии python завалены дискуссиями — меняться будет точно
        # match self.method:
        #     case 'print_msg':
        #         pop_elem = self.case.print_msg()
        #     case 'sum_nums':
        #         pop_elem = self.case.sum_nums()
        #     case 'sum_digits':
        #         pop_elem = self.case.sum_digits()
        #     case _:
        #         raise TypeError('unknown command')
        # ИСПОЛЬЗОВАТЬ: если обрабатываете имена идентификаторов, то лучше использовать встроенную функцию getattr()
        try:
            pop_elem = getattr(self.case, self.method)()
        except AttributeError:
            raise CommandError('unknown command')
        self.pop_list.append(pop_elem)
        self.__log(pop_elem, action[redo])

    def undo(self) -> None:
        if self.pop_list:
            pop_elem = self.pop_list.pop()
            match self.method:
                case 'print_msg':
                    self.case.messages.append(pop_elem)
                case 'sum_nums':
                    self.case.numbers.append(pop_elem)
                case 'sum_digits':
                    self.case.dict_.update([pop_elem])
                case _:
                    raise TypeError('unknown command')
            self.__log(pop_elem, 'UNDO')
            self.undo_cnt += 1
        else:
            print('nothing to undo')

    def redo(self) -> None:
        if self.undo_cnt > 0:
            self.execute(redo=True)
            self.undo_cnt -= 1
        else:
            print('nothing to redo')


# test_case1 = TestCase()
# tc1 = TestCommand(test_case1, 'sum_digits')
# tc1.execute()
# tc1.execute()
# tc1.execute()
# tc1.redo()
# tc1.undo()
# tc1.undo()
# tc1.undo()
# tc1.undo()
# tc1.redo()
# tc1.redo()
# tc1.redo()
# tc1.undo()
# tc1.undo()
# tc1.undo()
# print(*TestLogger.log, sep='\n')


# stdout:
# 15
# 14
# 17
# nothing to redo
# nothing to undo
# 15
# 14
# 17
# 2023-01-07 18:15:59 - sum_digits - (999, 690) - POP
# 2023-01-07 18:15:59 - sum_digits - (998, 905) - POP
# 2023-01-07 18:15:59 - sum_digits - (997, 674) - POP
# 2023-01-07 18:15:59 - sum_digits - (997, 674) - UNDO
# 2023-01-07 18:15:59 - sum_digits - (998, 905) - UNDO
# 2023-01-07 18:15:59 - sum_digits - (999, 690) - UNDO
# 2023-01-07 18:15:59 - sum_digits - (999, 690) - REDO
# 2023-01-07 18:15:59 - sum_digits - (998, 905) - REDO
# 2023-01-07 18:15:59 - sum_digits - (997, 674) - REDO
# 2023-01-07 18:15:59 - sum_digits - (997, 674) - UNDO
# 2023-01-07 18:15:59 - sum_digits - (998, 905) - UNDO
# 2023-01-07 18:15:59 - sum_digits - (999, 690) - UNDO


# ИТОГ: отлично — 7/7
