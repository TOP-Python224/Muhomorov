from enum import Enum
from datetime import time
from decimal import Decimal as dec


class Genre(Enum):
    FANTASTIC = 'Фантастика'
    THRILLER = 'Триллер'
    HORROR = 'Ужасы'
    ADVENTURE = 'Приключения'
    ACTION = 'Боевик'
    UNDEFINED = ''


class Awards(Enum):
    OSCAR = 'Оскар'
    GOLD = 'Золотой глобус'
    CANNES = 'Каннский кинофестиваль'
    UNDEFINED = ''


class FilmCard:
    """Определяет карточку фильма с минимальным количеством атрибутов."""
    def __init__(self, name: str, country: str, year: int):
        self.name = name
        self.country = country
        self.year = year
        # ДОБАВИТЬ: атрибуты экземпляра, объявленные в FilmFactory.create_movie()

    def __str__(self):
        # ОТВЕТИТЬ: чем-то аргументируется решение по конструированию строкового представления в фабрике или просто так захотелось?)
        return FilmFactory.print_movie(self)


class FilmFactory:
    """Фабрика для создания, редактирования и вывода экземпляров класса FilmCard."""
    def __init__(self):
        self.movies_db = []

    # КОММЕНТАРИЙ: конструктор фабрики вполне может быть весьма объёмным, особенно для классов данных (каковым и является FilmCard)
    # КОММЕНТАРИЙ: на практике мы практически никогда не передаём аргументы конструкторам в виде литералов (вспомните задачу 2 из 11.23) — почти всегда это будет получение данных от других функций/методов: из файла или БД или по URL — а значит данные уже будут структурированы тем или иным образом, см. например возвращаемое значение от API Кинопоиска: https://clck.ru/339bpR (Response 200 Show)
    # ИСПРАВИТЬ: таким образом, одной из задач фабрики часто бывает обработка полученной из внешних источников структуры данных с целью их преобразования для конструктора и атрибутов формируемого фабрикой экземпляра
    def create_movie(self, name, country, year) -> FilmCard:
        """Создает и возвращает экземпляр класса FilmCard."""
        movie = FilmCard(name, country, year)
        # УДАЛИТЬ: ничего не мешает объявить эти атрибуты в конструкторе FilmCard — именно так и следует сделать
        movie.genre = Genre.UNDEFINED
        # ИСПРАВИТЬ: в таких случаях, когда необходимо создать атрибут, но работать с ним предполагается позже, намного эффективнее присвоить в атрибут None — обычно это оказывается полезным для дальнейшей проверки атрибутов, так как attr is None отличается от bool(attr)
        movie.length = 0
        movie.cache = 0
        movie.age_limit = 0
        movie.actors = []
        movie.producers = []
        movie.awards = Awards.UNDEFINED
        self.movies_db += [movie]
        return movie

    # УДАЛИТЬ: все эти методы содержательно относятся скорее к шаблону Строитель, а не Фабрика

    @staticmethod
    # ИСПРАВИТЬ здесь и далее: не add, а set
    def add_genre(movie: FilmCard, genre: Genre):
        """Устанавливает значение атрибута жанр. """
        movie.genre = genre

    @staticmethod
    def add_length(movie: FilmCard, length: str):
        """Устанавливает значение атрибута продолжительность. """
        movie.length = time.fromisoformat(length)

    @staticmethod
    def add_cache(movie: FilmCard, cache: int):
        """Устанавливает значение атрибута кассовые сборы. """
        movie.cache = dec(cache)

    @staticmethod
    def add_age_limit(movie: FilmCard, age_limit: int):
        """Устанавливает значение атрибута возрастные ограничения. """
        movie.age_limit = age_limit

    @staticmethod
    # КОММЕНТАРИЙ: а вот здесь именно add
    def add_actor(movie: FilmCard, actor: str):
        # ИСПРАВИТЬ: значит не Устанавливает, а Добавляет
        """Устанавливает значение атрибута актеры. """
        movie.actors += [actor]

    @staticmethod
    def add_producer(movie: FilmCard, producer: str):
        """Устанавливает значение атрибута режиссер. """
        movie.producers += [producer]

    @staticmethod
    def add_awards(movie: FilmCard, awards: Awards):
        """Устанавливает значение атрибута награды. """
        movie.awards = awards

    @staticmethod
    def print_movie(movie):
        """Выводит экземпляр класса FilmCard на печать."""
        return f"Наименование: {movie.name}\n" \
               f"Страна: {movie.country}\n" \
               f"Год выпуска: {movie.year}\n" \
               f"Жанр: {movie.genre.value}\n" \
               f"Продолжительность: {movie.length}\n" \
               f"Кассовые сборы: {movie.cache}\n" \
               f"Возрастное ограничение: {movie.age_limit}\n" \
               f"Актеры: {movie.actors}\n" \
               f"Режиссер: {movie.producers}\n" \
               f"Награды: {movie.awards.value}\n"


# СДЕЛАТЬ: если не получается просто, давайте немного усложним задачу, чтобы вы лучше прочувствовали смысл фабрики
#  - напишите дополнительный класс Actor с полями name и surname
#  - в классе FilmCard должен быть атрибут actors: list[Actor]
#  - в конструктор фабрики для актёров должны передаваться строки формата "<имя> <фамилия>"
#  таким образом, фабрика должна будет в процессе инициализации экземпляра FilmCard ещё создать экземпляр(-ы) Actor
#  а данные для фабрики давайте уже традиционно поместим в JSON файл

cinema_center = FilmFactory()

terminator1 = cinema_center.create_movie('Терминатор', 'США', 1985)
# КОММЕНТАРИЙ: дальнейшее как-то слишком уж похоже на строитель, не находите?) пошаговый подход — прерогатива именно строителя, фабрика же больше про "штамповку", т.е. создание объекта за один явный шаг
cinema_center.add_actor(terminator1, 'Арнольд Шварценеггер')
cinema_center.add_actor(terminator1, 'Линда Хэмилтон')
cinema_center.add_producer(terminator1, 'Джеймс Кэмерон')
cinema_center.add_genre(terminator1, Genre.ACTION)
cinema_center.add_length(terminator1, '01:47')
cinema_center.add_age_limit(terminator1, 14)

terminator2 = cinema_center.create_movie('Терминатор-2', 'США', 1991)
cinema_center.add_actor(terminator2, 'Арнольд Шварценеггер')
cinema_center.add_actor(terminator2, 'Линда Хэмилтон')
cinema_center.add_producer(terminator2, 'Джеймс Кэмерон')
cinema_center.add_genre(terminator2, Genre.ACTION)
cinema_center.add_awards(terminator2, Awards.OSCAR)
cinema_center.add_length(terminator2, '02:36')
cinema_center.add_age_limit(terminator2, 14)

gravity = cinema_center.create_movie('Гравитация', 'США', 2013)
cinema_center.add_actor(gravity, 'Сандра Буллок')
cinema_center.add_genre(gravity, Genre.FANTASTIC)

alien = cinema_center.create_movie('Чужой', 'США', 1979)
cinema_center.add_actor(alien, 'Сигурни Уивер')
cinema_center.add_genre(alien, Genre.FANTASTIC)
cinema_center.add_awards(alien, Awards.OSCAR)

for movie in cinema_center.movies_db:
    if movie.genre.value == 'Фантастика':
        print(movie)

for movie in cinema_center.movies_db:
    if movie.awards.value == 'Оскар':
        print(movie)


# stdout:
# Наименование: Гравитация
# Страна: США
# Год выпуска: 2013
# Жанр: Фантастика
# Продолжительность: 0
# Кассовые сборы: 0
# Возрастное ограничение: 0
# Актеры: ['Сандра Буллок']
# Режиссер: []
# Награды:
#
# Наименование: Чужой
# Страна: США
# Год выпуска: 1979
# Жанр: Фантастика
# Продолжительность: 0
# Кассовые сборы: 0
# Возрастное ограничение: 0
# Актеры: ['Сигурни Уивер']
# Режиссер: []
# Награды: Оскар
#
# Наименование: Терминатор-2
# Страна: США
# Год выпуска: 1991
# Жанр: Боевик
# Продолжительность: 02:36:00
# Кассовые сборы: 0
# Возрастное ограничение: 14
# Актеры: ['Арнольд Шварценеггер', 'Линда Хэмилтон']
# Режиссер: ['Джеймс Кэмерон']
# Награды: Оскар
#
# Наименование: Чужой
# Страна: США
# Год выпуска: 1979
# Жанр: Фантастика
# Продолжительность: 0
# Кассовые сборы: 0
# Возрастное ограничение: 0
# Актеры: ['Сигурни Уивер']
# Режиссер: []
# Награды: Оскар


# ИТОГ: хорошая попытка, жду следующую =) — 3/8
