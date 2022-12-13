from pathlib import Path
from sys import path, modules
from importlib.util import spec_from_file_location, module_from_spec
from datetime import date
from decimal import Decimal
import json

students = {}
teachers = {}
researchers = {}
administrators = {}
generals = {}

local_dir = Path(path[0])
module_path = local_dir / '1.py'
spec = spec_from_file_location('university', module_path)
# ОТВЕТИТЬ: что скрывается за именем tusur? не могу разгадать этот ребус (на самом деле не хочу)
# ТУСУР - Томский университет систем управления и радиоэлектроники, когда-то я там учился.
tusur = module_from_spec(spec)
modules['university'] = tusur
spec.loader.exec_module(tusur)


# ИСПРАВИТЬ: как-то всё это грустно читается, не находите?) как насчёт создать JSON файл(-ы) с соответствующими ключами и значениями, например, с помощью generatedata.com? прочитать все данные, а потом коротко и изящно распаковать полученные словари в конструкторы соответствующих классов; имхо, лучший студент группы может сам проявить такую инициативу =Ъ
# Оставил создание "штучных" объектов прямо в коде, создание "множественных" объектов из json-файлов сделал с помощью функции.
def load_persons(*, type_persons: str = 'students', json_file: str | Path):
    """Загружает данные о физических лицах из json-файлов, нормализует их, и формирует словари содержащие экземпляры классов, соответствующие типу физического лица.
    :param type_persons: тип загружаемых физических лиц: 'students', 'teachers', 'researchers', 'administrators', 'generals'.
    :param json_file: json-файл с данными физических лиц.
    """
    cnt = 0
    json_file_path = local_dir / json_file
    with open(json_file_path, 'r', encoding='utf-8') as in_file:
        data = json.load(in_file)

    for item in data:
        cnt += 1
        item['birthdate'] = date.fromisoformat(item['birthdate'])
        item['gender'] = tusur.Person.Gender.MALE if item['gender'] == 'MALE' else tusur.Person.Gender.MALE
        item['contact'] = tusur.Contact(**item['contact'])

        if 'grant' in item:
            item['grant'] = Decimal(item['grant'])

        if 'form' in item:
            match item['form']:
                case 'INTRAMURAL':
                    item['form'] = tusur.Student.EducationForm.INTRAMURAL
                case 'EXTRAMURAL':
                    item['form'] = tusur.Student.EducationForm.EXTRAMURAL
                case 'REMOTE':
                    item['form'] = tusur.Student.EducationForm.REMOTE

        if 'contract' in item:
            match item['contract']:
                case 'BUDGET':
                    item['contract'] = tusur.Student.Contract.BUDGET
                case 'COMPANY':
                    item['contract'] = tusur.Student.Contract.COMPANY
                case 'PERSONAL':
                    item['contract'] = tusur.Student.Contract.PERSONAL

        if 'degree' in item:
            match item['degree']:
                case 'BACHELOR':
                    item['degree'] = tusur.Degree.BACHELOR
                case 'SPECIALIST':
                    item['degree'] = tusur.Degree.SPECIALIST
                case 'MASTER':
                    item['degree'] = tusur.Degree.MASTER
                case 'CANDIDATE':
                    item['degree'] = tusur.Degree.CANDIDATE
                case 'DOCTOR':
                    item['degree'] = tusur.Degree.DOCTOR

        if 'salary' in item:
            item['salary'] = Decimal(item['salary'])

        if 'hire_date' in item:
            item['hire_date'] = date.fromisoformat(item['hire_date'])

        match type_persons:
            case 'students':
                students[cnt] = tusur.Student(**item)
            case 'teachers':
                teachers[cnt] = tusur.Teacher(**item)
            case 'researchers':
                researchers[cnt] = tusur.Researcher(**item)
            case 'administrators':
                administrators[cnt] = tusur.Administrator(**item)
            case 'generals':
                generals[cnt] = tusur.GeneralPersonnel(**item)
            case _:
                raise ValueError('некорректный тип физического лица')


load_persons(type_persons='students', json_file='students.json')
load_persons(type_persons='teachers', json_file='teachers.json')
load_persons(type_persons='researchers', json_file='researchers.json')
load_persons(type_persons='administrators', json_file='administrators.json')
load_persons(type_persons='generals', json_file='generals.json')

# ИСПОЛЬЗОВАТЬ: пример оформления передачи большого количества аргументов, в ситуации, когда иначе не получается
# СДЕЛАТЬ: такое количество аргументов неизбежно запутывает — вы должны были об задуматься уже после первого подобного ввода — а значит есть насущная потребность использовать строго ключевые параметры, как минимум для аргументов конструкторов подклассов Person и OrganizationLevel
university_1 = tusur.University(
    name='ЯГУ',
    contact=tusur.Contact(
        mobile='79131234567',
        email='yagu@mail.ru',
        office='73831234567',
        home='73831234568',
        telegram='@Yagu',
        icq='987654321'
    ),
    budget=Decimal(110000),
    budgets={'11-2022': Decimal(100000)},
)

dormitory_1 = tusur.Dormitory(
    name='Общежитие №1',
    contact=tusur.Contact(),
    budget=Decimal(2000),
    budgets={'11-2022': Decimal(1000)}
)

institute_1 = tusur.Institute(
    name = 'ЯГПИ',
    contact = tusur.Contact(
        mobile='79131234567',
        email='yagpi@mail.ru',
        office='73831234567',
        home='73831234568',
        telegram='@Yagpi',
        icq='987654321'
    ),
    budget=Decimal(110000),
    budgets={'11-2022': Decimal(100000)},
)

institute_2 = tusur.Institute(
    name='ЯГТИ',
    contact=tusur.Contact(
        mobile='79131234567',
        email='yagti@mail.ru',
        office='73831234567',
        home='73831234568',
        telegram='@Yagti',
        icq='987654321'
    ),
    budget=Decimal(110000),
    budgets={'11-2022': Decimal(100000)},
)

# КОММЕНТАРИЙ: а ещё, постоянное использование пустых списков/строк/словарей/... должно было навести вас на мысль о значениях по умолчанию в модели
# ИСПРАВИТЬ: Institute — институт, он же факультет, а Department — это кафедра на факультете или институте (допускаю, что есть структуры в которых присутствуют и институты и факультеты, но у нас не так)
department_1 = tusur.Department(
    name='Кафедра информатики',
    contact=tusur.Contact(
        mobile='79131234567',
        email='fi@mail.ru',
        office='73831234567',
        home='73831234568',
        telegram='@FI',
        icq='987654321'
    ),
    budget=Decimal(110000),
    budgets={'11-2022': Decimal(100000)},
)

department_2 = tusur.Department(
    name='Кафедра физики',
    contact=tusur.Contact(
        mobile='79131234567',
        email='ff@mail.ru',
        office='73831234567',
        home='73831234568',
        telegram='@FF',
        icq='987654321'
    ),
    budget=Decimal(110000),
    budgets={'11-2022': Decimal(100000)},
)

department_3 = tusur.Department(
    name='Кафедра математики',
    contact=tusur.Contact(
        mobile='79131234567',
        email='mf@mail.ru',
        office='73831234567',
        home='73831234568',
        telegram='@MF',
        icq='987654321'
    ),
    budget=Decimal(110000),
    budgets={'11-2022': Decimal(100000)},

)

department_4 = tusur.Department(
    name='Кафедра геологии',
    contact=tusur.Contact(
        mobile='79131234567',
        email='gf@mail.ru',
        office='73831234567',
        home='73831234568',
        telegram='@GF',
        icq='987654321'
    ),
    budget=Decimal(110000),
    budgets={'11-2022': Decimal(100000)},
)

group_1 = tusur.Group('И-1', students[1], teachers[1])
group_2 = tusur.Group('М-1', students[2], teachers[2])
group_3 = tusur.Group('Ф-1', students[3], teachers[1])
group_4 = tusur.Group('Г-1', '', '')
group_4.change_chief(students[4])
group_4.change_curator(teachers[2])
university_1.change_head(administrators[1])
institute_1.change_head([administrators[2], administrators[3]])
generals[1].head = administrators[2]
researchers[1].head = administrators[1]
group_1 += [students[1]]
group_1 += [students[2]]
group_4 += [students[3], students[4]]
department_1.add_group(group_1)
department_2.add_group(group_4)
dormitory_1.checkin_student('1', students[1])
dormitory_1.checkin_student('1', students[2])
dormitory_1.checkin_student('2', students[3])
dormitory_1.checkin_student('3', students[4])

# stdout:
# print(university_1)
# Наименование: ЯГУ
# Бюджеты: {'11-2022': Decimal('100000')}
# Персонал: []
# Руководитель:
# ФИО: Hall Grace Basil
# Дата рождения: 1979-01-06
# Пол: мужской
# Мобильный: 43822586464
# e-mail: lectus.rutrum@google.com
# Рабочий: 99488286773
# Домашний: 56088960310
# Телеграм: @Rqzveijj
# ICQ: 368773270
# Предыдущий стаж: 1
# Зарплата: 10000
# Должность: administrator
# Руководитель: None
# Дата приема на работу: 2019-10-22
# Контакты организации:
# Мобильный: 79131234567
# e-mail: yagu@mail.ru
# Рабочий: 73831234567
# Домашний: 73831234568
# Телеграм: @Yagu
# ICQ: 987654321
# Бюджет: 110000

# print(dormitory_1)
# Наименование: Общежитие №1
# Бюджеты: {'11-2022': Decimal('1000')}
# Персонал: []
# Руководитель:
# []
# Контакты организации:
# Мобильный: None
# e-mail: None
# Рабочий: None
# Домашний: None
# Телеграм: None
# ICQ: None
# Бюджет: 2000

# print(institute_1)
# Наименование: ЯГПИ
# Бюджеты: {'11-2022': Decimal('100000')}
# Персонал: []
# Руководитель:
# ФИО: Drake Yen Caesar
# Дата рождения: 1975-06-10
# Пол: мужской
# Мобильный: 37711327647
# e-mail: pede.praesent@google.com
# Рабочий: 97693546217
# Домашний: 81183026249
# Телеграм: @Ygnxqvpe
# ICQ: 257750551
# Предыдущий стаж: 7
# Зарплата: 10000
# Должность: administrator
# Руководитель:
# Дата приема на работу: 2020-08-24
# Контакты организации:
# Мобильный: 79131234567
# e-mail: yagpi@mail.ru
# Рабочий: 73831234567
# Домашний: 73831234568
# Телеграм: @Yagpi
# ICQ: 987654321
# Бюджет: 110000

# print(department_3)
# Наименование: Кафедра математики
# Бюджеты: {'11-2022': Decimal('100000')}
# Персонал: []
# Руководитель:
# Контакты организации:
# Мобильный: 79131234567
# e-mail: mf@mail.ru
# Рабочий: 73831234567
# Домашний: 73831234568
# Телеграм: @MF
# ICQ: 987654321
# Бюджет: 110000

# print(students[1])
# ФИО: Woodward Myra Kessie
# Дата рождения: 2001-09-29
# Пол: мужской
# Мобильный: 78894744145
# e-mail: dapibus.quam.quis@google.org
# Рабочий: 71837877517
# Домашний: 73158612717
# Телеграм: @Kzohbehc
# ICQ: 717921103
# Форма обучения: Очная
# Форма оплаты: Платно
# Курс: 1
# Стипендия: 1000

# print(generals[5])
# ФИО: Lowe Kellie Colin
# Дата рождения: 1972-08-08
# Пол: мужской
# Мобильный: 20101458471
# e-mail: tellus.non@aol.couk
# Рабочий: 44473736256
# Домашний: 27612196056
# Телеграм: @Xahvocue
# ICQ: 874242728
# Предыдущий стаж: 5
# Зарплата: 10000
# Должность: driver
# Руководитель:
# Дата приема на работу: 2022-12-19

# КОММЕНТАРИЙ: скомбинировать объекты согласно модели получилось, но не увидел, чтобы инициализация и использование объектов привели к полезным промежуточным выводам по модели


# ИТОГ: хорошо — 8/12
