"""Описывает университет."""
from abc import ABC
from datetime import date
from enum import Enum
from decimal import Decimal
from dataclasses import dataclass
import re


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
    contact: "Contact"


@dataclass
class Contact:
    """Описывает контактные данные."""
    mobile: str = None
    email: str = None
    office: str = None
    home: str = None
    telegram: str = None
    icq: str = None

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


class Student(Person):
    """Описывает студента."""
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
                 form: EducationForm,
                 contract: "Contract",
                 year: int,
                 speciality: str,
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
                 subordinates: list[Employee]):
        super().__init__(surname, name, patronymic, birthdate, gender, contact, hire_date,
                         _prev_experience, salary, position, head)
        self.division = division
        self.subordinates = subordinates


class ProfessionalEmployee(Employee):
    """Описывает научно-преподавательский персонал."""
    def __init__(self, surname, name, patronymic, birthdate, gender, contact, hire_date,
                 _prev_experience, salary, position, head,
                 degree: "Degree"):
        super().__init__(surname, name, patronymic, birthdate, gender, contact, hire_date,
                         _prev_experience, salary, position, head)
        self.degree = degree


class Degree(Enum):
    """Описывает ученую степень."""
    B = 'BACHELOR'
    S = 'SPECIALIST'
    M = 'MASTER'
    C = 'CANDIDATE'
    D = 'DOCTOR'


class Teacher(ProfessionalEmployee):
    """Описывает преподавателей."""
    def __init__(self, surname, name, patronymic, birthdate, gender, contact, hire_date,
                 _prev_experience, salary, position, head, degree,
                 courses: list[str],
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
    def __init__(self,
                 budgets: dict[int, Decimal],
                 name: str,
                 employees: list[Employee],
                 head: Administrator,
                 contact: Contact,
                 budget: Decimal
                 ):
        self.__budgets = budgets
        self.name = name
        self.__employees = employees
        self.head = head
        self.contact = contact
        self.__budget = budget

    def hire_employee(self, employee: Employee) -> Employee:
        """Прием на работу."""
        self.__employees.append(employee)
        return employee

    def fire_employee(self, employee: Employee):
        """Увольнение с работы."""
        self.__employees.remove(employee)

    def change_head(self, new_head: Administrator):
        """Смена руководителя."""
        self.head = new_head

    def set_budget(self, new_budget: Decimal):
        """Установка бюджета."""
        self.__budget = new_budget


class Dormitory(OrganizationLevel):
    """Описывает общежитие."""
    def __init__(self, budgets, name, employees, head, contact, budget,
                 rooms: dict[str, list[Student]]):
        super().__init__(budgets, name, employees, head, contact, budget)
        self.rooms = rooms

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

    def change_head(self, new_head: Administrator):
        """Смена руководителя."""
        self.head = new_head


class Department(OrganizationLevel):
    """Описывает факультет."""
    def __init__(self, budgets, name, employees, head, contact, budget,
                 groups: list["Group", ...]):
        super().__init__(budgets, name, employees, head, contact, budget)
        self.groups = groups

    def change_head(self, new_head: Administrator):
        """Смена руководителя."""
        self.head = new_head

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

