from pathlib import Path
from sys import path, modules
from importlib.util import spec_from_file_location, module_from_spec
from datetime import date
from decimal import Decimal

local_dir = Path(path[0])
module_path = local_dir / '1.py'
spec = spec_from_file_location('university', module_path)
tusur = module_from_spec(spec)
modules['university'] = tusur
spec.loader.exec_module(tusur)

administrator_1 = tusur.Administrator('Семенов', 'Иван', 'Семенович', date(1955, 11, 22), tusur.Person.Gender.M,
                  tusur.Contact('79131234567', 'semenov@mail.ru', '73831234567', '73831234568', '@Semen', '987654321'),
                  date(1990, 2, 1), 5, Decimal(45000), 'Декан', 'Мин.обр. РФ', 'Деканат', [])

dormitory_1 = tusur.Dormitory({2021: Decimal(1000)}, 'Общежитие №1', [], '', tusur.Contact(), Decimal(2000), {})

institute_1 = tusur.Institute({2021: Decimal(100000)}, 'ЯГПИ', [], '',
              tusur.Contact('79131234567', 'yagpi@mail.ru', '73831234567', '73831234568', '@Yagpi', '987654321'),
              Decimal(110000), [])

institute_2 = tusur.Institute({2021: Decimal(100000)}, 'ЯГТИ', [], '',
              tusur.Contact('79131234567', 'yagti@mail.ru', '73831234567', '73831234568', '@Yagti', '987654321'),
              Decimal(110000), [])

university_1 = tusur.University({2021: Decimal(1000000)}, 'ЯГУ', [], '',
               tusur.Contact('79131234567', 'yagu@mail.ru', '73831234567', '73831234568', '@Yagu', '987654321'),
               Decimal(1100000), [institute_1, institute_2], [dormitory_1])

administrator_2 = tusur.Administrator('Геринг', 'Марта', 'Степановна', date(1975, 11, 13), tusur.Person.Gender.F,
                  tusur.Contact('79131234567', 'gering@mail.ru', '73831234567', '73831234568', '@Gering', '987654321'),
                  date(1990, 2, 1), 5, Decimal(45000), 'Ректор', administrator_1, 'Ректорат', [])

administrator_3 = tusur.Administrator('Смирнов', 'Игорь', 'Игоревич', date(1959, 9, 22), tusur.Person.Gender.M,
                  tusur.Contact('79131234567', 'igor@mail.ru', '73831234567', '73831234568', '@Igor', '987654321'),
                  date(1990, 2, 1), 5, Decimal(45000), 'Ректор', administrator_1, 'Ректорат', [])

department_1 = tusur.Department({2021: Decimal(1000000)}, 'Факультет информатики', [], '',
               tusur.Contact('79131234567', 'fi@mail.ru', '73831234567', '73831234568', '@FI', '987654321'),
               Decimal(1100000), [])

department_2 = tusur.Department({2021: Decimal(1000000)}, 'Физический факультет', [], '',
               tusur.Contact('79131234567', 'ff@mail.ru', '73831234567', '73831234568', '@FF', '987654321'),
               Decimal(1100000), [])

department_3 = tusur.Department({2021: Decimal(1000000)}, 'Математический факультет', [], '',
               tusur.Contact('79131234567', 'mf@mail.ru', '73831234567', '73831234568', '@MF', '987654321'),
               Decimal(1100000), [])

department_4 = tusur.Department({2021: Decimal(1000000)}, 'Геологический факультет', [], '',
               tusur.Contact('79131234567', 'gf@mail.ru', '73831234567', '73831234568', '@GF', '987654321'),
               Decimal(1100000), [])

student_1 = tusur.Student('Иванов', 'Иван', 'Иванович', date(1977, 1, 25), tusur.Person.Gender.M,
            tusur.Contact('79141234567', 'ivan@mail.ru', '74951234567', '74951234568', '@Ivan', '123456789'),
            tusur.Student.EducationForm.I, tusur.Student.Contract.B, 2021, 'IT', Decimal(20000))

student_2 = tusur.Student('Петров', 'Петр', 'Петрович', date(1977, 2, 26), tusur.Person.Gender.M,
            tusur.Contact('79141234567', 'peter@mail.ru', '74951234567', '74951234568', '@Peter', '123456789'),
            tusur.Student.EducationForm.I, tusur.Student.Contract.B, 2021, 'IT', Decimal(20000))

student_3 = tusur.Student('Николаева', 'Инна', 'Ивановна', date(1977, 3, 27), tusur.Person.Gender.F,
            tusur.Contact('79141234567', 'inna@mail.ru', '74951234567', '74951234568', '@Inna', '123456789'),
            tusur.Student.EducationForm.I, tusur.Student.Contract.C, 2021, 'IT', Decimal(20000))

student_4 = tusur.Student('Попова', 'Светлана', 'Петровна', date(1977, 4, 28), tusur.Person.Gender.F,
            tusur.Contact('79141234567', 'sveta@mail.ru', '74951234567', '74951234568', '@Svetlana', '123456789'),
            tusur.Student.EducationForm.I, tusur.Student.Contract.P, 2021, 'IT', Decimal(20000))

teacher_1 = tusur.Teacher('Петрова', 'Жанна', 'Николаевна', date(1965, 10, 21), tusur.Person.Gender.F,
            tusur.Contact('79131234567', 'zhanna@mail.ru', '73831234567', '73831234568', '@Zhanna', '987654321'),
            date(1990, 2, 1), 5, Decimal(45000), 'Преподаватель', '', tusur.Degree.C, ['Python', 'JS'], False)

teacher_2 = tusur.Teacher('Борисов', 'Сергей', 'Ильич', date(1964, 11, 22), tusur.Person.Gender.M,
            tusur.Contact('79131234567', 'sergey@mail.ru', '73831234567', '73831234568', '@Sergey', '987654321'),
            date(1988, 10, 10), 7, Decimal(45000), 'Преподаватель', '', tusur.Degree.M, ['Python', 'JS'], False)

researcher_1 = tusur.Researcher('Яковлев', 'Илья', 'Сергеевич', date(1963, 12, 23), tusur.Person.Gender.M,
               tusur.Contact('79131234567', 'ilya@mail.ru', '73831234567', '73831234568', '@Ilya', '987654321'),
               date(1980, 11, 11), 17, Decimal(45000), 'Зав. лабораторией', '', tusur.Degree.D)

car_driver_1 = tusur.GeneralPersonnel('Дымов', 'Андрей', 'Иванович', date(1973, 1, 2), tusur.Person.Gender.M,
               tusur.Contact('79131234567', 'andrey@mail.ru', '73831234567', '73831234568', '@Andrey', '987654321'),
               date(2001, 11, 11), 10, Decimal(45000), 'Водитель', '')

group_1 = tusur.Group('И-1', student_1, teacher_1)
group_2 = tusur.Group('М-1', student_2, teacher_2)
group_3 = tusur.Group('Ф-1', student_3, teacher_1)
group_4 = tusur.Group('Г-1', '', '')
group_4.change_chief(student_4)
group_4.change_curator(teacher_2)
university_1.change_head(administrator_1)
institute_1.change_head(administrator_2)
institute_2.change_head(administrator_3)
department_1.change_head(administrator_2)
department_2.change_head(administrator_2)
department_3.change_head(administrator_3)
department_4.change_head(administrator_3)
car_driver_1.head = administrator_2
researcher_1.head = administrator_1
group_1 += [student_1]
group_1 += [student_2]
group_4 += [student_3, student_4]
department_1.add_group(group_1)
department_2.add_group(group_4)
dormitory_1.checkin_student('1', student_1)
dormitory_1.checkin_student('1', student_2)
dormitory_1.checkin_student('2', student_3)
dormitory_1.checkin_student('3a', student_4)
print(dormitory_1.rooms)
print(group_4.__dict__)
print(university_1.__dict__)
print(student_1.__dict__)
print(teacher_2.__dict__)
print(university_1.__dict__)
print(tusur.Employee.__dict__)

# stdout:
# {'1': [Student(surname='Иванов', name='Иван', patronymic='Иванович', birthdate=datetime.date(1977, 1, 25), gender=<Gender.M: 'male'>, contact=Contact(mobile='79141234567', email='ivan@mail.ru', office='74951234567', home='74951234568', telegram='@Ivan', icq='123456789')), Student(surname='Петров', name='Петр', patronymic='Петрович', birthdate=datetime.date(1977, 2, 26), gender=<Gender.M: 'male'>, contact=Contact(mobile='79141234567', email='peter@mail.ru', office='74951234567', home='74951234568', telegram='@Peter', icq='123456789'))], '2': [Student(surname='Николаева', name='Инна', patronymic='Ивановна', birthdate=datetime.date(1977, 3, 27), gender=<Gender.F: 'female'>, contact=Contact(mobile='79141234567', email='inna@mail.ru', office='74951234567', home='74951234568', telegram='@Inna', icq='123456789'))], '3a': [Student(surname='Попова', name='Светлана', patronymic='Петровна', birthdate=datetime.date(1977, 4, 28), gender=<Gender.F: 'female'>, contact=Contact(mobile='79141234567', email='sveta@mail.ru', office='74951234567', home='74951234568', telegram='@Svetlana', icq='123456789'))]}
# {'name': 'Г-1', 'chief': Student(surname='Попова', name='Светлана', patronymic='Петровна', birthdate=datetime.date(1977, 4, 28), gender=<Gender.F: 'female'>, contact=Contact(mobile='79141234567', email='sveta@mail.ru', office='74951234567', home='74951234568', telegram='@Svetlana', icq='123456789')), 'curator': Teacher(surname='Борисов', name='Сергей', patronymic='Ильич', birthdate=datetime.date(1964, 11, 22), gender=<Gender.M: 'male'>, contact=Contact(mobile='79131234567', email='sergey@mail.ru', office='73831234567', home='73831234568', telegram='@Sergey', icq='987654321'))}
# {'_OrganizationLevel__budgets': {2021: Decimal('1000000')}, 'name': 'ЯГУ', '_OrganizationLevel__employees': [], 'head': Administrator(surname='Семенов', name='Иван', patronymic='Семенович', birthdate=datetime.date(1955, 11, 22), gender=<Gender.M: 'male'>, contact=Contact(mobile='79131234567', email='semenov@mail.ru', office='73831234567', home='73831234568', telegram='@Semen', icq='987654321')), 'contact': Contact(mobile='79131234567', email='yagu@mail.ru', office='73831234567', home='73831234568', telegram='@Yagu', icq='987654321'), '_OrganizationLevel__budget': Decimal('1100000'), 'institute': [<university.Institute object at 0x0000021EDD683550>, <university.Institute object at 0x0000021EDD6835D0>], 'dormitories': [<university.Dormitory object at 0x0000021EDD683490>]}
# {'surname': 'Иванов', 'name': 'Иван', 'patronymic': 'Иванович', 'birthdate': datetime.date(1977, 1, 25), 'gender': <Gender.M: 'male'>, 'contact': Contact(mobile='79141234567', email='ivan@mail.ru', office='74951234567', home='74951234568', telegram='@Ivan', icq='123456789'), 'form': <EducationForm.I: 'INTRAMURAL'>, 'contract': <Contract.B: 'BUDGET'>, 'year': 2021, 'speciality': 'IT', 'grant': Decimal('20000')}
# {'surname': 'Борисов', 'name': 'Сергей', 'patronymic': 'Ильич', 'birthdate': datetime.date(1964, 11, 22), 'gender': <Gender.M: 'male'>, 'contact': Contact(mobile='79131234567', email='sergey@mail.ru', office='73831234567', home='73831234568', telegram='@Sergey', icq='987654321'), 'hire_date': datetime.date(1988, 10, 10), '_prev_experience': 7, 'salary': Decimal('45000'), 'position': 'Преподаватель', 'head': '', 'degree': <Degree.M: 'MASTER'>, 'courses': ['Python', 'JS'], 'professorship': False}
# {'_OrganizationLevel__budgets': {2021: Decimal('1000000')}, 'name': 'ЯГУ', '_OrganizationLevel__employees': [], 'head': Administrator(surname='Семенов', name='Иван', patronymic='Семенович', birthdate=datetime.date(1955, 11, 22), gender=<Gender.M: 'male'>, contact=Contact(mobile='79131234567', email='semenov@mail.ru', office='73831234567', home='73831234568', telegram='@Semen', icq='987654321')), 'contact': Contact(mobile='79131234567', email='yagu@mail.ru', office='73831234567', home='73831234568', telegram='@Yagu', icq='987654321'), '_OrganizationLevel__budget': Decimal('1100000'), 'institute': [<university.Institute object at 0x0000021EDD683550>, <university.Institute object at 0x0000021EDD6835D0>], 'dormitories': [<university.Dormitory object at 0x0000021EDD683490>]}
# {'__module__': 'university', '__doc__': 'Описывает работников.', '__init__': <function Employee.__init__ at 0x0000021EDD686660>, 'experience': <property object at 0x0000021EDD657420>, '__abstractmethods__': frozenset(), '_abc_impl': <_abc._abc_data object at 0x0000021EDD681D40>}
