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

class Contact:
    """Описывает контактные данные."""

    def __init__(self,
                 mobile: str = None,
                 email: str = None,
                 office: str = None,
                 home: str = None,
                 telegram: str = None,
                 icq: str = None):
        self.mobile = mobile
        self.email = email
        self.office = office
        self.home = home
        self.telegram = telegram
        self.icq = icq

    # ИСПРАВИТЬ: методы не используются
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        if value is None:
            self._mobile = None
        elif value.isdecimal() and len(value) == 11:
            self._mobile = value
        else:
            raise ValueError('некорректный номер телефона')

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if value is None:
            self._email = None
        elif re.match(r"^[\w.-]+@([\w-]+.)+[\w-]{2,}$", value):
            self._email = value
        else:
            raise ValueError('некорректный email')

    @property
    def office(self):
        return self._office

    @office.setter
    def office(self, value):
        if value is None:
            self._office = None
        elif value.isdecimal() and len(value) == 11:
            self._office = value
        else:
            raise ValueError('некорректный номер телефона')

    @property
    def home(self):
        return self._home

    @home.setter
    def home(self, value):
        if value is None:
            self._home = None
        elif value.isdecimal() and len(value) == 11:
            self._home = value
        else:
            raise ValueError('некорректный номер телефона')

    @property
    def telegram(self):
        return self._telegram

    @telegram.setter
    def telegram(self, value):
        if value is None:
            self._telegram = None
        elif re.match(r"^@([\w.-]+)$", value):
            self._telegram = value
        else:
            raise ValueError('некорректное имя пользователя telegram')

    @property
    def icq(self):
        return self._icq

    @icq.setter
    def icq(self, value):
        if value is None:
            self._icq = None
        elif value.isdecimal():
            self._icq = value
        else:
            raise ValueError('некорректный UIN')

    def __str__(self):
        return f"Мобильный: {self.mobile}\n" \
               f"e-mail: {self.email}\n" \
               f"Рабочий: {self.office}\n" \
               f"Домашний: {self.home}\n" \
               f"Телеграм: {self.telegram}\n" \
               f"ICQ: {self.icq}"


@dataclass
class Person(ABC):
    """Описывает человека."""

    class Gender(Enum):
        """Описывает пол человека."""
        MALE = 'мужской'
        FEMALE = 'женский'

    surname: str
    name: str
    patronymic: str
    birthdate: date
    gender: Gender
    # ДОБАВИТЬ: значение по умолчанию — None
    contact: Contact = None

    def __str__(self):
        return f"ФИО: {self.surname} {self.name} {self.patronymic}\n" \
               f"Дата рождения: {self.birthdate}\n" \
               f"Пол: {self.gender.value}\n" \
               f"{self.contact}"


class Student(Person):
    """Описывает студента."""

    # ИСПРАВИТЬ: вообще, в перечислителях обычно не слишком сокращают имена атрибутов, т.к. цель заключается ещё и в том, чтобы прямо в коде понятно объяснить какая именно константа используется — здесь стоит поменять местами имена и значения
    class EducationForm(Enum):
        """Описывает форму обучения."""
        INTRAMURAL = 'Очная'
        EXTRAMURAL = 'Заочная'
        REMOTE = 'Дистанционная'

    class Contract(Enum):
        """Описывает источник финансирования обучения."""
        BUDGET = 'Бюджет'
        COMPANY = 'Предприятие'
        PERSONAL = 'Платно'

    def __init__(self, surname, name, patronymic, birthdate, gender, contact,
                 speciality: str,
                 # ДОБАВИТЬ: значение по умолчанию — очная форма
                 form: EducationForm = EducationForm.INTRAMURAL,
                 # ДОБАВИТЬ: значение по умолчанию — бюджет
                 contract: "Contract" = Contract.BUDGET,
                 # ДОБАВИТЬ: значение по умолчанию — подавляющее большинство создаваемых объектов студентов будут добавляться на первый курс
                 year: int = 1,
                 # ДОБАВИТЬ: значение по умолчанию — у большинства студентов на старте одинаковая стипендия (а её изменение в основном обусловлено успеваемостью и прочими заслугами студента, либо особыми льготами, что можно проверять и устанавливать отдельным методом)
                 grant: Decimal = 3000):
        super().__init__(surname, name, patronymic, birthdate, gender, contact)
        self.speciality = speciality
        self.form = form
        self.contract = contract
        self.year = year
        self.grant = grant

    def __str__(self):
        return f"{super().__str__()}\n" \
               f"Форма обучения: {self.form.value}\n" \
               f"Форма оплаты: {self.contract.value}\n" \
               f"Курс: {self.year}\n" \
               f"Стипендия: {self.grant}"


class Employee(Person, ABC):
    """Описывает работников."""

    def __init__(self, surname, name, patronymic, birthdate, gender, contact,
                 # ДОБАВИТЬ: значение по умолчанию — сегодня
                 prev_experience: int,
                 salary: Decimal,
                 position: str,
                 head: "Administrator",
                 hire_date: date = date.today()):
        super().__init__(surname, name, patronymic, birthdate, gender, contact)
        self._prev_experience = prev_experience
        self.salary = salary
        self.position = position
        self.head = head
        self.hire_date = hire_date

    @property
    def experience(self):
        """Выводит суммарный стаж работника."""
        return date.today().year - self.hire_date.year + self._prev_experience

    def __str__(self):
        return f"{super().__str__()}\n" \
               f"Предыдущий стаж: {self._prev_experience}\n" \
               f"Зарплата: {self.salary}\n" \
               f"Должность: {self.position}\n" \
               f"Руководитель: {self.head}\n" \
               f"Дата приема на работу: {self.hire_date}"


class Administrator(Employee):
    """Описывает руководителей."""

    def __init__(self, surname, name, patronymic, birthdate, gender, contact,
                 _prev_experience, salary, position, head, hire_date,
                 division: str,
                 # ДОБАВИТЬ: значение по умолчанию — пустой список
                 subordinates: list[Employee] = []):
        super().__init__(surname, name, patronymic, birthdate, gender, contact,
                         _prev_experience, salary, position, head, hire_date)
        self.division = division
        self.subordinates = subordinates


class Degree(Enum):
    """Описывает ученую степень."""
    BACHELOR = 'Bachelor'
    SPECIALIST = 'Specialist'
    MASTER = 'Master'
    CANDIDATE = 'Candidate'
    DOCTOR = 'Doctor'


class ProfessionalEmployee(Employee):
    """Описывает научно-преподавательский персонал."""

    def __init__(self, surname, name, patronymic, birthdate, gender, contact,
                 _prev_experience, salary, position, head, hire_date,
                 degree: Degree):
        super().__init__(surname, name, patronymic, birthdate, gender, contact,
                         _prev_experience, salary, position, head, hire_date)
        self.degree = degree


class Teacher(ProfessionalEmployee):
    """Описывает преподавателей."""

    def __init__(self, surname, name, patronymic, birthdate, gender, contact,
                 _prev_experience, salary, position, head, hire_date, degree,
                 courses: list[str],
                 # ДОБАВИТЬ: значение по умолчанию — False (принятие на работу готового профессора довольно редкое событие)
                 professorship: bool = False):
        super().__init__(surname, name, patronymic, birthdate, gender, contact,
                         _prev_experience, salary, position, head, hire_date, degree)
        self.courses = courses
        self.professorship = professorship

    def __str__(self):
        return f"{super().__str__()}\n" \
               f"Предметы: {self.courses}\n" \
               f"Профессор: {self.professorship}"


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
                 name: str,
                 contact: Contact,
                 budget: Decimal = Decimal(100000),
                 # ДОБАВИТЬ: значение по умолчанию — пустой словарь
                 budgets: dict[str, Decimal] = {},
                 # ДОБАВИТЬ: значение по умолчанию — пустой список
                 employees: list[Employee] = [],
                 # ДОБАВИТЬ: значение по умолчанию — None
                 head: Administrator = None,
                 ):
        # КОММЕНТАРИЙ: впрочем, я согласен, что следует перенести это в атрибуты экземпляра, потому что у каждого университета/общежития/института/кафедры своя история бюджета — но об этом необходимо было написать в комментарии: иначе, непонятно, сознательное ли это действие или вы просто в диаграмме не разобрались
        self.name = name
        self.contact = contact
        self.__budget = budget
        self.__budgets = budgets
        self.__employees = employees
        self.head = head
        # ИСПРАВИТЬ: использовать метод для изменения бюджета или не использовать в конструкторе аргумент

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
        min_budget = Decimal(90000)
        max_budget = Decimal(110000)
        default_budget = Decimal(100000)
        today = date.today().strftime('%m-%Y')
        if today not in self.__budgets:
            if min_budget <= new_budget <= max_budget:
                self.__budgets[today] = Decimal(new_budget)
                self.__budget = Decimal(new_budget)
            else:
                self.__budgets[today] = default_budget
                self.__budget = default_budget
        else:
            raise ValueError('бюджет на текущий месяц уже установлен')

    def __str__(self):
        return f"Наименование: {self.name}\n" \
               f"Бюджеты: {self.__budgets}\n" \
               f"Персонал: {self.__employees}\n" \
               f"Руководитель: \n" \
               f"{self.head}\n" \
               f"Контакты организации:\n" \
               f"{self.contact}\n" \
               f"Бюджет: {self.__budget}"


class Dormitory(OrganizationLevel):
    """Описывает общежитие."""

    def __init__(self, *, name, contact, budget, budgets, employees=[], head=[],
                 rooms={}):
        """
        :param rooms: общее количество комнат
        """
        super().__init__(name, contact, budget, budgets, employees, head)
        # ДОБАВИТЬ: инициализацию словаря "пустыми комнатами"
        self.rooms: dict[str, list[Student]] = {room: [] for room in range(1, 51)}

    def checkin_student(self, room_number: str, new_student: Student):
        """Регистрация студента в общежитии."""
        self.rooms[room_number] = self.rooms.setdefault(room_number, []) + [new_student]


class University(OrganizationLevel):
    """Описывает университет."""

    def __init__(self, *, name, contact, budget, budgets, employees=[], head='',
                 institutes: list["Institute"] = [],
                 dormitories: list[Dormitory] = []):
        super().__init__(name, contact, budget, budgets, employees, head)
        self.institute = institutes
        self.dormitories = dormitories


class Institute(OrganizationLevel):
    """Описывает институт."""

    def __init__(self, *, name, contact, budget, budgets, employees=[], head='',
                 departments: list["Department"]=[]):
        super().__init__(name, contact, budget, budgets, employees, head)
        self.departments = departments

    # ИСПОЛЬЗОВАТЬ: стоит как-то явно обозначить переопределение
    def change_head(self, candidates: list[Administrator]):
        """Смена руководителя с помощью голосования."""
        self.head = choice(candidates)


class Department(OrganizationLevel):
    """Описывает кафедру."""

    def __init__(self, name, contact, budget, budgets, employees=[], head='',
                 # ИСПОЛЬЗОВАТЬ: существует мысленное допущение (см. PEP 483), что изменяемые контейнеры используются преимущественно для произвольного количества однотипных элементов; в то время как неизменяемые контейнеры куда чаще используются для конечного и в основном небольшого количества разнотипных элементов — именно из этих допущений вытекают правила аннотации: для списков и прочих изменяемых контейнеров мы задаём тип каждого элемента не уточняя их количество т.к. оно произвольно, а для кортежей и прочих неизменяемых мы прописываем тип каждого отдельного элемента используя многоточие для имитации поведения списка
                 groups: list["Group"]=[]):
        super().__init__(name, contact, budget, budgets, employees, head)
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
                 chief: Student = None,
                 curator: Teacher = None):
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

    def __str__(self):
        std = [f"{i.surname} {i.name} {i.patronymic}" for i in self]
        return f"Название: {self.name}\n" \
               f"Староста: {self.chief}\n" \
               f"Куратор: {self.curator}\n" \
               f"Студенты: {std}"

# ДОБАВИТЬ: __repr__()/__str__() методы очень не помешали бы в следующей задаче


# ИТОГ: хорошо — 9/12
# p = Person('Мухоморов', 'Иван', 'Александрович', date(1975, 6, 25), Person.Gender.MALE)
# print(p)
# print(p.__repr__())
#
# c = Contact('79142713636', 'ioi@sfdff.ru', '79142552525', '79135256485', '@uijjh', '12346578')
# print(c)
# print(c.__repr__())
