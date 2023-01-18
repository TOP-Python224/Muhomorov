import re


class TextParser:
    """Парсер текстовых данных в некой системе."""

    def __init__(self, text: str):
        tmp = re.sub(r'\W', ' ', text.lower())
        tmp = re.sub(r' +', ' ', tmp).strip()
        self.text = tmp

    def get_processed_text(self, processor) -> None:
        """Вызывает метод класса обработчика.

        :param processor: экземпляр класса обработчика
        """
        result = processor.process_text(self.text)
        print(*result, sep='\n')


class WordCounter:
    """Счётчик частотности слов в тексте."""

    def __init__(self, text: str) -> None:
        """Обрабатывает переданный текст и создаёт словарь с частотой слов."""
        self.__words = dict()
        for word in text.split():
            self.__words[word] = self.__words.get(word, 0) + 1

    def get_count(self, word: str) -> int:
        """Возвращает частоту переданного слова."""
        return self.__words.get(word, 0)

    def get_all_words(self) -> dict[str, int]:
        """Возвращает словарь с частотой слов."""
        return self.__words.copy()


class Adapter:
    """Адаптер для использования методов счетчика в парсере."""

    # ДОБАВИТЬ: аннотации типов параметров для всех методов и возвращаемых значений для не встроенных методов — это особенно важно для структурных классов

    def __init__(self, adapted: WordCounter):
        self.adapted = adapted

    def process_text(self, text: str):
        """Вызывает методы счетчика, и передает результат в парсер."""
        self.adapted.__init__(text)
        # ИСПОЛЬЗОВАТЬ: очевидные имена идентификаторов
        words_rate = self.adapted.get_all_words()
        return sorted(words_rate, key=lambda word: self.adapted.get_count(word), reverse=True)


dirty_text = """
У нас есть две системы для работы с текстом!
У  есть  системы  работы  текстом@
У две  работы с !#
"""

parser = TextParser(dirty_text)
counter = WordCounter('')
adapter = Adapter(counter)
parser.get_processed_text(adapter)


# ИТОГ: очень хорошо — 5/6
