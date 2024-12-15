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


# TODO: написать класс Book
class Book:
    def __init__(self, id_, name, pages):   # метод __init__ принимает три параметра
        self.id = id_   # идентификатор книги (целое число)
        self.name = name    # Название книги
        self.pages = pages   # Количество страниц в книге

    def __str__(self):     # метод __str__ возвращает строку в формате (Книга "название_книги"),
        # название книги берется из атрибута name
        return f'Книга "{self.name}"'

    def __repr__(self):     # метод __repr__  возвращает строку в формате Book(id_=1, name='test_name_1', pages=200)
        return f'Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})'


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__

