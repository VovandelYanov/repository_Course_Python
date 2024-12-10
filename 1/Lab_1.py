import doctest

class Stack:
    def __init__(self, max_size: int, name: str):
        """
        Создание и подготовка к работе объекта "Стек"

        :param max_size: Максимальный размер стека
        :param name: Имя стека

        Примеры:
        >>> stack = Stack(10, "Мой стек")
        >>> stack.max_size
        10
        >>> stack.name
        'Мой стек'
        """
        if not isinstance(max_size, int):
            raise TypeError("Максимальный размер стека должен быть типа int")
        if max_size <= 0:
            raise ValueError("Максимальный размер стека должен быть положительным числом")
        self.max_size = max_size
        self.stack = []
        self.name = name

    def is_empty_stack(self) -> bool:
        """
        Функция которая проверяет является ли стек пустым

        :return: Является ли стек пустым

        Примеры:
        >>> stack = Stack(10, "Мой стек")
        >>> stack.is_empty_stack()
        True
        """
        return len(self.stack) == 0

    def push_element(self, element: object) -> None:
        """
        Добавление элемента в стек.

        :param element: Добавляемый элемент

        :raise ValueError: Если размер стека превышает максимальный размер, то вызываем ошибку

        Примеры:
        >>> stack = Stack(10, "Мой стек")
        >>> stack.push_element(5)
        >>> stack.is_empty_stack()
        False
        """
        if len(self.stack) >= self.max_size:
            raise ValueError("Размер стека превышает максимальный размер")
        self.stack.append(element)

    def pop_element(self) -> object:
        """
        Извлечение элемента из стека.

        :return: Извлеченный элемент

        :raise IndexError: Если стек пуст, то вызываем ошибку

        Примеры:
        >>> stack = Stack(10, "Мой стек")
        >>> stack.push_element(5)
        >>> stack.pop_element()
        5
        >>> stack.is_empty_stack()
        True
        """
        if self.is_empty_stack():
            raise IndexError("Стек пуст")
        return self.stack.pop()


class Tree:
    def __init__(self, height: float, age: int):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param height: Высота дерева
        :param age: Возраст дерева

        Примеры:
        >>> tree = Tree(10.5, 20)
        >>> tree.height
        10.5
        >>> tree.age
        20
        """
        if not isinstance(height, (int, float)):
            raise TypeError("Высота дерева должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом")
        self.height = height

        if not isinstance(age, int):
            raise TypeError("Возраст дерева должен быть типа int")
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным числом")
        self.age = age

    def is_mature_tree(self) -> bool:
        """
        Функция которая проверяет является ли дерево взрослым

        :return: Является ли дерево взрослым

        Примеры:
        >>> tree = Tree(10.5, 20)
        >>> tree.is_mature_tree()
        True
        """
        return self.age >= 10

    def grow_tree(self, years: int = 1) -> None:
        """
        Рост дерева.

        :param years: Количество лет, на которое дерево будет расти

        :raise ValueError: Если количество лет отрицательное, то вызываем ошибку

        Примеры:
        >>> tree = Tree(10.5, 20)
        >>> tree.grow_tree(5)
        >>> tree.age
        25
        >>> tree.height
        13.0
        """
        if years < 0:
            raise ValueError("Количество лет не может быть отрицательным числом")
        self.age += years
        self.height += years * 0.5


class Facebook:
    def __init__(self, username: str, password: str):
        """
        Создание и подготовка к работе объекта "Фейсбук"

        :param username: Имя пользователя
        :param password: Пароль

        Примеры:
        >>> facebook = Facebook("user123", "password123")
        >>> facebook.username
        'user123'
        >>> facebook.password
        'password123'
        """
        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно быть типа str")
        if not username:
            raise ValueError("Имя пользователя не может быть пустым")
        self.username = username

        if not isinstance(password, str):
            raise TypeError("Пароль должен быть типа str")
        if not password:
            raise ValueError("Пароль не может быть пустым")
        self.password = password

    def is_valid_password(self, password: str) -> bool:
        """
        Функция которая проверяет является ли пароль валидным

        :param password: Пароль для проверки

        :return: Является ли пароль валидным

        :raise ValueError: Если пароль пуст, то вызываем ошибку

        Примеры:
        >>> facebook = Facebook("user123", "password123")
        >>> facebook.is_valid_password("password123")
        True
        >>> facebook.is_valid_password("wrongpassword")
        False
        """
        if not password:
            raise ValueError("Пароль не может быть пустым")
        return password == self.password

    def change_password(self, new_password: str) -> None:
        """
        Изменение пароля.

        :param new_password: Новый пароль

        :raise ValueError: Если новый пароль пуст, то вызываем ошибку

        Примеры:
        >>> facebook = Facebook("user123", "password123")
        >>> facebook.change_password("new_password123")
        >>> facebook.is_valid_password("new_password123")
        True
        """
        if not new_password:
            raise ValueError("Новый пароль не может быть пустым")
        self.password = new_password


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

