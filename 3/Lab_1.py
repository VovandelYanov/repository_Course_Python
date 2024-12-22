class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name      # название книги
        self._author = author     # автор

    @property   # позволяет создать только геттеры, без сеттеров это делает атрибуты name и author неизменяемыми после инициализации
    def name(self):
        # свойство для получения имени книги
        return self._name

    @property
    def author(self):
        # свойство для получения автора книги
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):      # наследуем от Book

    def __init__(self, name: str, author: str, pages: int):
        # инициализируем бумажную книгу с указанием количества страниц
        super().__init__(name, author)
        self.pages = pages  # будет вызван setter pages

    @property
    def pages(self):
        # свойство для получения количества страниц
        return self._pages

    @pages.setter
    def pages(self, value: int):
        # сеттер для установки количества страниц
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целое.")
        if value <= 0:
            raise ValueError("Количество страниц должно быть больше нуля.")
        self._pages = value

    def __str__(self):
        return f"{super().__str__()}. Страниц: {self.pages}"


class AudioBook(Book):

    def __init__(self, name: str, author: str, duration: float):
        # инициализируем книгу с указанием продолжительности
        super().__init__(name, author)
        self.duration = duration  # будет вызван setter duration

    @property
    def duration(self):
        # свойство для получения продолжительности аудиокниги
        return self._duration

    @duration.setter
    def duration(self, value: float):
        # сеттер для установки продолжительности с проверкой
        if not isinstance(value, (float, int)):
            raise TypeError("Продолжительность должна быть числом.")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительной.")
        self._duration = float(value)

    def __str__(self):
        # Строковое представление аудиокниги
        return f"{super().__str__()}. Продолжительность: {self.duration} часов."
