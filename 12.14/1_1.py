import re

dirty_text = """
У нас есть две системы для работы с текстом!
У  есть  системы  работы  текстом@
У две  работы с !#
"""


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

    def __init__(self, adapted):
        self.adapted = adapted

    def process_text(self, text):
        """Вызывает методы счетчика, и передает результат в парсер."""
        self.adapted.__init__(text)
        result = self.adapted.get_all_words()
        return sorted(result, key=lambda word: self.adapted.get_count(word), reverse=True)


parser = TextParser(dirty_text)
counter = WordCounter('')
adapter = Adapter(counter)
parser.get_processed_text(adapter)
