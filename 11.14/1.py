class Person:
    """Описывает человека."""
    def __init__(self,
                 surname: str,
                 name: str,
                 patronymic: str):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic

    def is_educating(self) -> bool:
        return isinstance(self, Student)

    def is_employed(self) -> bool:
        return isinstance(self, Employee)

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"


class Student(Person):
    """Описывает студента."""
    def __init__(self,
                 surname: str,
                 name: str,
                 patronymic: str,
                 educational_organization: str,
                 commercial: bool = False):
        super().__init__(surname, name, patronymic)
        self.educational_organization = educational_organization
        self.commercial = commercial

    def __str__(self):
        return super().__str__() + \
               f" учится в {self.educational_organization}" \
               f" на {'коммерческой' if self.commercial else 'бюджетной'} основе."


class Employee(Person):
    """Описывает работающего человека."""
    def __init__(self,
                 surname: str,
                 name: str,
                 patronymic: str,
                 company: str,
                 salary: int):
        super().__init__(surname, name, patronymic)
        self.company = company
        self.salary = salary

    def __str__(self):
        return super().__str__() + \
               f"работает в {self.company} " \
               f"с зарплатой {self.salary} рублей."


# p1 = Person('Иванов', 'Сергей', 'Петрович')
# print(p1)
# print(p1.is_educating(), p1.is_employed())
# print()
#
# s1 = Student('Борисов', 'Иннокентий', 'Кимович', 'ЯГУ')
# print(s1)
# print(s1.is_educating(), s1.is_employed())
# print()
#
# s2 = Student('Волков', 'Андрей', 'Ибрагимович', 'ТУСУР', True)
# print(s2)
# print(s2.is_educating(), s2.is_employed())
# print()
#
# e1 = Employee('Петров', 'Александр', 'Сергеевич', 'Ярче', 30000)
# print(e1)
# print(e1.is_educating(), e1.is_employed())

# stdout:
# Иванов Сергей Петрович
# False False
#
# Борисов Иннокентий Кимович учится в ЯГУ на бюджетной основе.
# True False
#
# Волков Андрей Ибрагимович учится в ТУСУР на коммерческой основе.
# True False
#
# Петров Александр Сергеевич работает в Ярче с зарплатой 30000 рублей.
# False True


# ИТОГ: отлично — 5/5
