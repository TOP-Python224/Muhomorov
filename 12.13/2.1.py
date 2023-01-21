from enum import Enum
from datetime import time
from decimal import Decimal as Dec
from json import load as jload
from sys import path
from pathlib import Path

local_dir = Path(path[0])
movies_file = local_dir / 'movies.json'
movies_db = []
actors_db = []


class Genre(Enum):
    FANTASTIC = 'Фантастика'
    THRILLER = 'Триллер'
    HORROR = 'Ужасы'
    ADVENTURE = 'Приключения'
    ACTION = 'Боевик'
    UNDEFINED = ''

    def __str__(self):
        return self.value


class Awards(Enum):
    OSCAR = 'Оскар'
    GOLD = 'Золотой глобус'
    CANNES = 'Каннский кинофестиваль'
    UNDEFINED = ''

    def __str__(self):
        return self.value


class Actor:
    def __init__(self,
                 name: str,
                 surname: str):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"


class FilmCard:
    """Определяет карточку фильма."""
    def __init__(self,
                 name: str,
                 country: str,
                 year: int,
                 genre: Genre = None,
                 length: int = None,
                 cache: int = None,
                 age_limit: int = None,
                 actors: list[Actor] = None,
                 producers: str = None,
                 awards: str = None
                 ):
        self.genre = genre
        self.length = length
        self.cache = cache
        self.age_limit = age_limit
        self.actors = actors
        self.producers = producers
        self.awards = awards
        self.name = name
        self.country = country
        self.year = year
        # ДОБАВИТЬ: атрибуты экземпляра, объявленные в FilmFactory.create_movie()

    def __str__(self):
        # ОТВЕТИТЬ: чем-то аргументируется решение по конструированию строкового представления в фабрике или просто так захотелось?)
        # Случайно )
        return f"Наименование: {self.name}\n" \
               f"Страна: {self.country}\n" \
               f"Год выпуска: {self.year}\n" \
               f"Жанр: {self.genre}\n" \
               f"Продолжительность: {self.length}\n" \
               f"Кассовые сборы: {self.cache}\n" \
               f"Возрастное ограничение: {self.age_limit}\n" \
               f"Актеры: {', '.join([str(actor) for actor in self.actors])}\n" \
               f"Режиссер: {self.producers}\n" \
               f"Награды: {self.awards}\n"


class FilmFactory:
    """Фабрика для создания, редактирования и вывода экземпляров класса FilmCard."""
    # КОММЕНТАРИЙ: конструктор фабрики вполне может быть весьма объёмным, особенно для классов данных (каковым и является FilmCard)
    # КОММЕНТАРИЙ: на практике мы практически никогда не передаём аргументы конструкторам в виде литералов (вспомните задачу 2 из 11.23) — почти всегда это будет получение данных от других функций/методов: из файла или БД или по URL — а значит данные уже будут структурированы тем или иным образом, см. например возвращаемое значение от API Кинопоиска: https://clck.ru/339bpR (Response 200 Show)
    # ИСПРАВИТЬ: таким образом, одной из задач фабрики часто бывает обработка полученной из внешних источников структуры данных с целью их преобразования для конструктора и атрибутов формируемого фабрикой экземпляра
    @staticmethod
    def create_movies(name, country, year, genre, length, cache, age_limit, actors, producers, awards) -> FilmCard:
        """Создает и возвращает экземпляр класса FilmCard."""
        movie = FilmCard(name, country, year, genre, length, cache, age_limit, actors, producers, awards)
        # УДАЛИТЬ: ничего не мешает объявить эти атрибуты в конструкторе FilmCard — именно так и следует сделать
        # ИСПРАВИТЬ: в таких случаях, когда необходимо создать атрибут, но работать с ним предполагается позже, намного эффективнее присвоить в атрибут None — обычно это оказывается полезным для дальнейшей проверки атрибутов, так как attr is None отличается от bool(attr)
        return movie

    # УДАЛИТЬ: все эти методы содержательно относятся скорее к шаблону Строитель, а не Фабрика

    @staticmethod
    def load_movies() -> dict:
        """Считывает данные о фильмах из json-файла."""
        with open(movies_file, encoding='utf-8') as filein:
            return jload(filein)

    @staticmethod
    def parse_movies(movie) -> dict:
        """Подготавливает полученные данные о фильмах для генерации объектов."""
        actors_lst = []
        if movie['genre']:
            for genre in list(Genre):
                if movie['genre'] == genre.value:
                    movie['genre'] = genre
        else:
            movie['genre'] = Genre.UNDEFINED

        if movie['awards']:
            for awards in list(Awards):
                if movie['awards'] == awards.value:
                    movie['awards'] = awards
        else:
            movie['awards'] = Awards.UNDEFINED

        for actor in movie['actors']:
            curr_actor = Actor(actor['name'], actor['surname'])
            actors_db.append(curr_actor)
            actors_lst.append(curr_actor)
        movie['actors'] = actors_lst

        curr_movie = {'name': movie['name'],
                      'country': movie['country'],
                      'year': int(movie['year']),
                      'genre': movie['genre'],
                      'length': time.fromisoformat(movie['length']),
                      'cache': Dec(movie['cache']),
                      'age_limit': int(movie['age_limit']),
                      'actors': movie['actors'],
                      'producers': movie['producers'],
                      'awards': movie['awards']}
        return curr_movie

    def start_factory(self):
        """Запускает фабрику: считывание из файла, обрабатка считанных данных, создание и добавление экземпляров класса FilmCard и Actor в БД фильмов и актеров."""
        movies = self.load_movies()
        for movie in movies:
            parsed_movie = self.parse_movies(movie)
            result = self.create_movies(**parsed_movie)
            movies_db.append(result)

# СДЕЛАТЬ: если не получается просто, давайте немного усложним задачу, чтобы вы лучше прочувствовали смысл фабрики
#  - напишите дополнительный класс Actor с полями name и surname
#  - в классе FilmCard должен быть атрибут actors: list[Actor]
#  - в конструктор фабрики для актёров должны передаваться строки формата "<имя> <фамилия>"
#  таким образом, фабрика должна будет в процессе инициализации экземпляра FilmCard ещё создать экземпляр(-ы) Actor
#  а данные для фабрики давайте уже традиционно поместим в JSON файл


cinema_center = FilmFactory()
cinema_center.start_factory()

for m in movies_db:
    print(m)

for a in actors_db:
    print(a)

# КОММЕНТАРИЙ: дальнейшее как-то слишком уж похоже на строитель, не находите?) пошаговый подход — прерогатива именно строителя, фабрика же больше про "штамповку", т.е. создание объекта за один явный шаг

# stdout:
# Наименование: Брат
# Страна: Россия
# Год выпуска: 1997
# Жанр: Боевик
# Продолжительность: 01:40:00
# Кассовые сборы: 10000000
# Возрастное ограничение: 14
# Актеры: Сергей Бодров, Виктор Сухоруков
# Режиссер: Александр Балабанов
# Награды:
#
# Наименование: Терминатор-2
# Страна: США
# Год выпуска: 1991
# Жанр: Боевик
# Продолжительность: 01:36:00
# Кассовые сборы: 100000000
# Возрастное ограничение: 14
# Актеры: Арнольд Шварценеггер, Линда Хэмилтон
# Режиссер: Джеймс Кэмерон
# Награды: Оскар
#
# Наименование: Гравитация
# Страна: США
# Год выпуска: 2013
# Жанр: Приключения
# Продолжительность: 01:30:00
# Кассовые сборы: 274000000
# Возрастное ограничение: 12
# Актеры: Сандра Буллок, Джордж Клуни
# Режиссер: Альфонсо Куарон
# Награды: Оскар
#
# Наименование: Чужие
# Страна: США
# Год выпуска: 1986
# Жанр: Фантастика
# Продолжительность: 02:17:00
# Кассовые сборы: 131000000
# Возрастное ограничение: 14
# Актеры: Сигурни Уивер
# Режиссер: Джеймс Кэмерон
# Награды: Оскар
#
# Сергей Бодров
# Виктор Сухоруков
# Арнольд Шварценеггер
# Линда Хэмилтон
# Сандра Буллок
# Джордж Клуни
# Сигурни Уивер

# ИТОГ: хорошая попытка, жду следующую =) — 3/8
