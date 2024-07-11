BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    """Класс описывает объект 'Книга'"""
    def __init__(self, id_: int, name: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга".

        :param id_: Идентификатор книги в библиотеке.
        :param name: Название.
        :param pages: Количество страниц.
        """
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """
        :return: Возвращает строку с названием книги.
        """
        return f'Книга "{self.name}"'

    def __repr__(self):
        """
        :return: Возвращает строку, по которой можно инициализировать точно такой же экземпляр.
        """
        return f"{self.__class__.__name__}(id_={self.id_}, name='{self.name}', pages={self.pages})"


class Library:
    """Класс описывает объект 'Библиотека'"""
    def __init__(self, books: list = None):
        """
        Создание и подготовка к работе объекта "Библиотека".

        :param books: Список книг.
        """
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self) -> int:
        """
        Метод возвращает идентификатор для добавления новой книги в библиотеку.

        :return: Если книг в библиотеке нет, то вернуть 1.
                 Если книги есть, то вернуть идентификатор последней книги увеличенный на 1
        """
        return 1 if len(self.books) == 0 else max(self.books, key=lambda x: x.id_).id_ + 1

    def get_index_by_book_id(self, ident: int) -> int:
        """
        Метод возвращает индекс книги в списке по id книги.

        :param ident: Идентификатор книги в библиотеке.
        :raise ValueError: Если книги с запрашиваемым id нет в библиотеке, возвращается ошибка.

        :return: Если книга существует, то вернуть индекс из списка.
        """
        list_index = [index for index, value in enumerate(self.books) if value.id_ == ident]
        if list_index:
            return list_index[0]

        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
