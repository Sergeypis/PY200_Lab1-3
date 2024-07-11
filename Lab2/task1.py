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


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__