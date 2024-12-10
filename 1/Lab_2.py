from task_1 import Stack, Tree, Facebook
# TODO: импортируйте классы, созданные в ходе выполнения прошлого задания
if __name__ == "__main__":
    # Инстанцирование классов
    stack = Stack(10, "Мой стек")
    tree = Tree(10.5, 20)
    facebook = Facebook("user123", "password123")
    # TODO: инстанцировать все описанные классы, создав три объекта.C()
    # Проверка класса Stack
    try:
        stack.push_element(5)
        stack.push_element(6)
        stack.push_element(7)
        # Пробуем добавить элемент, когда стек уже полон
        for _ in range(8):  # 10 - 3 = 7, добавляем еще 8
            stack.push_element(8)
    except ValueError:
        print('Ошибка: неправильные данные')
    # TODO: вызвать метод с некорректными аргументами(b)
    # Проверка класса Tree
    try:
        tree.grow_tree(-5)  # Пробуем вызвать метод с отрицательным значением
    except ValueError:
        print('Ошибка: неправильные данные')
    # TODO: вызвать метод с некорректными аргументами(a)
    # Проверка класса Facebook
    try:
        facebook.change_password("")  # Пробуем установить пустой пароль
    except ValueError:
        print('Ошибка: неправильные данные')
  # TODO: вызвать метод с некорректными аргументами(a)