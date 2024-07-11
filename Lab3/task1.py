class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга '{self._name}'. Автор: {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration!r})"


if __name__ == '__main__':
    paper_book = PaperBook('Бумажная книга', 'Пушкин', 200)
    audio_book = AudioBook('Аудио книга', 'Тургенев', 600.53)

    print(paper_book)
    print(audio_book)

    paper_book.author = 'Есенин'
    print(paper_book)
    print(audio_book)