"""Описывает университет."""
from abc import ABC
from datetime import date
from enum import Enum
from decimal import Decimal
from dataclasses import dataclass
import re
from random import choice


# КОММЕНТАРИЙ: с точки зрения наследования код объявлений классов размещается сверху вниз от родительского к дочерним, а с точки зрения агрегации — сверху вниз от вложенного к внешним

# ИСПРАВИТЬ: вот здесь зря в датакласс и статические методы пошли — я бы лучше работу с атрибутами и валидацию сделал на основе свойств (геттеров) и сеттеров, включая инициализацию в конструкторе
@dataclass
class Contact:
    """Описывает контактные данные."""
    mobile: str = None
    email: str = None
    office: str = None
    home: str = None
    telegram: str = None
    icq: str = None

    # ИСПРАВИТЬ: методы не используются
    @staticmethod
    def validate_mobile(mobile):
        return mobile.isdecimal() and len(mobile) == 11

    @staticmethod
    def validate_email(email):
        return bool(re.match(r"^[\w.-]+@([\w-]+.)+[\w-]{2,}$", email))

    @staticmethod
    def validate_office(office):
        return office.isdecimal() and len(office) == 11

    @staticmethod
    def validate_home(home):
        return home.isdecimal() and len(home) == 11

    @staticmethod
    def validate_telegram(telegram):
        return bool(re.match(r"^@([\w.-]+)$", telegram))

    @staticmethod
    def validate_icq(icq):
        return icq.isdecimal()


@dataclass
class Person(ABC):
    """Описывает человека."""
    class Gender(Enum):
        """Описывает пол человека."""
        M = 'male'
        F = 'female'

    surname: str
    name: str
    patronymic: str
    birthdate: date
    gender: Gender
    # ДОБАВИТЬ: значение по умолчанию — None
    contact: Contact


class Student(Person):
    """Описывает студента."""
    # ИСПРАВИТЬ: вообще, в перечислителях обычно не слишком сокращают имена атрибутов, т.к. цель заключается ещё и в том, чтобы прямо в коде понятно объяснить какая именно константа используется — здесь стоит поменять местами имена и значения
    class EducationForm(Enum):
        """Описывает форму обучения."""
        I = 'INTRAMURAL'
        E = 'EXTRAMURAL'
        R = 'REMOTE'

    class Contract(Enum):
        """Описывает источник финансирования обучения."""
        B = 'BUDGET'
        C = 'COMPANY'
        P = 'PERSONAL'

    def __init__(self, surname, name, patronymic, birthdate, gender, contact,
                 # ДОБАВИТЬ: значение по умолчанию — очная форма
                 form: EducationForm,
                 # ДОБАВИТЬ: значение по умолчанию — бюджет
                 contract: "Contract",
                 # ДОБАВИТЬ: значение по умолчанию — подавляющее большинство создаваемых объектов студентов будут добавляться на первый курс
                 year: int,
                 speciality: str,
                 # ДОБАВИТЬ: значение по умолчанию — у большинства студентов на старте одинаковая стипендия (а её изменение в основном обусловлено успеваемостью и прочими заслугами студента, либо особыми льготами, что можно проверять и устанавливать отдельным методом)
                 grant: Decimal):
        super().__init__(surname, name, patronymic, birthdate, gender, contact)
        self.form = form
        self.contract = contract
        self.year = year
        self.speciality = speciality
        self.grant = grant


class Employee(Person, ABC):
    """Описывает работников."""
    def __init__(self, surname, name, patronymic, birthdate, gender, contact,
                 # ДОБАВИТЬ: значение по умолчанию — сегодня
                 hire_date: date,
                 prev_experience: int,
                 salary: Decimal,
                 position: str,
                 head: "Administrator"):
        super().__init__(surname, name, patronymic, birthdate, gender, contact)
        self.hire_date = hire_date
        self._prev_experience = prev_experience
        self.salary = salary
        self.position = position
        self.head = head

    @property
    def experience(self):
        """Выводи суммарный стаж работника."""
        return date.today().year - self.hire_date.year + self._prev_experience


class Administrator(Employee):
    """Описывает руководителей."""
    def __init__(self, surname, name, patronymic, birthdate, gender, contact, hire_date,
                 _prev_experience, salary, position, head,
                 division: str,
                 # ДОБАВИТЬ: значение по умолчанию — пустой список
                 subordinates: list[Employee]):
        super().__init__(surname, name, patronymic, birthdate, gender, contact, hire_date,
                         _prev_experience, salary, position, head)
        self.division = division
        self.subordinates = subordinates


class Degree(Enum):
    """Описывает ученую степень."""
    B = 'BACHELOR'
    S = 'SPECIALIST'
    M = 'MASTER'
    C = 'CANDIDATE'
    D = 'DOCTOR'


class ProfessionalEmployee(Employee):
    """Описывает научно-преподавательский персонал."""
    def __init__(self, surname, name, patronymic, birthdate, gender, contact, hire_date,
                 _prev_experience, salary, position, head,
                 degree: Degree):
        super().__init__(surname, name, patronymic, birthdate, gender, contact, hire_date,
                         _prev_experience, salary, position, head)
        self.degree = degree


class Teacher(ProfessionalEmployee):
    """Описывает преподавателей."""
    def __init__(self, surname, name, patronymic, birthdate, gender, contact, hire_date,
                 _prev_experience, salary, position, head, degree,
                 courses: list[str],
                 # ДОБАВИТЬ: значение по умолчанию — False (принятие на работу готового профессора довольно редкое событие)
                 professorship: bool):
        super().__init__(surname, name, patronymic, birthdate, gender, contact, hire_date,
                         _prev_experience, salary, position, head, degree)
        self.courses = courses
        self.professorship = professorship


class GeneralPersonnel(Employee):
    """Описывает общий персонал."""
    pass


class Researcher(ProfessionalEmployee):
    """Описывает исследовательский персонал."""
    pass


class OrganizationLevel(ABC):
    """Описывает организацию."""
    # КОММЕНТАРИЙ: на диаграмме атрибут budgets у нас помечен подчёркиванием — это означает "статический" или "атрибут класса" (что, в некотором смысле, одно и то же)
    def __init__(self,
                 # ДОБАВИТЬ: значение по умолчанию — пустой словарь
                 budgets: dict[int, Decimal],
                 name: str,
                 # ДОБАВИТЬ: значение по умолчанию — пустой список
                 employees: list[Employee],
                 # ДОБАВИТЬ: значение по умолчанию — None
                 head: Administrator,
                 contact: Contact,
                 budget: Decimal
                 ):
        # КОММЕНТАРИЙ: впрочем, я согласен, что следует перенести это в атрибуты экземпляра, потому что у каждого университета/общежития/института/кафедры своя история бюджета — но об этом необходимо было написать в комментарии: иначе, непонятно, сознательное ли это действие или вы просто в диаграмме не разобрались
        self.__budgets = budgets
        self.name = name
        self.__employees = employees
        self.head = head
        self.contact = contact
        # ИСПРАВИТЬ: использовать метод для изменения бюджета или не использовать в конструкторе аргумент
        self.__budget = budget

    def hire_employee(self, employee: Employee) -> Employee:
        """Прием на работу."""
        self.__employees.append(employee)
        return employee

    def fire_employee(self, employee: Employee):
        """Увольнение с работы."""
        self.__employees.remove(employee)

    def change_head(self, new_head: Administrator):
        """Смена руководителя назначением нового."""
        self.head = new_head

    def set_budget(self, new_budget: Decimal):
        """Установка бюджета."""
        # ИСПРАВИТЬ: добавьте использование словаря __budgets — установка бюджета возможна только один раз в месяц каждого года; стоит ещё общие границы допустимого установить, а то пропишет себе самая умная кафедра месячный бюджет в охренеллиард рублей..)
        self.__budget = new_budget


class Dormitory(OrganizationLevel):
    """Описывает общежитие."""
    def __init__(self, budgets, name, employees, head, contact, budget,
                 rooms: int):
        """
        :param rooms: общее количество комнат
        """
        super().__init__(budgets, name, employees, head, contact, budget)
        # ДОБАВИТЬ: инициализацию словаря "пустыми комнатами"
        self.rooms: dict[str, list[Student]] = {}

    def checkin_student(self, room_number: str, new_student: Student):
        """Регистрация студента в общежитии."""
        self.rooms[room_number] = self.rooms.setdefault(room_number, []) + [new_student]


class University(OrganizationLevel):
    """Описывает университет."""
    def __init__(self, budgets, name, employees, head, contact, budget,
                 institutes: list["Institute"],
                 dormitories: list[Dormitory]):
        super().__init__(budgets, name, employees, head, contact, budget)
        self.institute = institutes
        self.dormitories = dormitories


class Institute(OrganizationLevel):
    """Описывает институт."""
    def __init__(self, budgets, name, employees, head, contact, budget,
                 departments: list["Department"]):
        super().__init__(budgets, name, employees, head, contact, budget)
        self.departments = departments

    # ИСПОЛЬЗОВАТЬ: стоит как-то явно обозначить переопределение
    def change_head(self, candidates: list[Administrator]):
        """Смена руководителя с помощью голосования."""
        self.head = choice(candidates)


class Department(OrganizationLevel):
    """Описывает кафедру."""
    def __init__(self, budgets, name, employees, head, contact, budget,
                 # ИСПОЛЬЗОВАТЬ: существует мысленное допущение (см. PEP 483), что изменяемые контейнеры используются преимущественно для произвольного количества однотипных элементов; в то время как неизменяемые контейнеры куда чаще используются для конечного и в основном небольшого количества разнотипных элементов — именно из этих допущений вытекают правила аннотации: для списков и прочих изменяемых контейнеров мы задаём тип каждого элемента не уточняя их количество т.к. оно произвольно, а для кортежей и прочих неизменяемых мы прописываем тип каждого отдельного элемента используя многоточие для имитации поведения списка
                 groups: list["Group"]):
        super().__init__(budgets, name, employees, head, contact, budget)
        self.groups = groups

    # ИСПОЛЬЗОВАТЬ: стоит как-то явно обозначить переопределение
    def change_head(self, candidates: list[Administrator]):
        """Смена руководителя с помощью голосования."""
        self.head = choice(candidates)

    def add_group(self, new_group: "Group"):
        """Добавление группы."""
        self.groups.append(new_group)

    def remove_group(self, group: "Group"):
        """Удаление группы."""
        self.groups.remove(group)


class Group(list):
    """Описывает группу."""
    def __init__(self,
                 name: str,
                 # ДОБАВИТЬ: значения по умолчанию для chief и curator — мы вполне можем предположить ситуацию, когда экземпляр группы создаётся, например приёмной комиссией, и студенты зачисляются туда постепенно — а куратор и староста назначены будут уже после окончательного формирования группы
                 chief: Student,
                 curator: Teacher):
        self.name = name
        self.chief = chief
        self.curator = curator
        super().__init__()

    def change_chief(self, new_chief: Student):
        """Смена старосты."""
        self.chief = new_chief

    def change_curator(self, new_curator: Teacher):
        """Смена куратора."""
        self.curator = new_curator


# ДОБАВИТЬ: __repr__()/__str__() методы очень не помешали бы в следующей задаче


# ИТОГ: хорошо — 9/12
