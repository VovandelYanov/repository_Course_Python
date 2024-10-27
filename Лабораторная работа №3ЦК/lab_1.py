# TODO Напишите функцию для поиска индекса товара
def search_index(items, item):  # принимает список элементов и элемент, индекс которого нужно найти
    for index, real_item in enumerate(items):  # проходим по всем элементам списка enumerate возвращает
        # индекс и элемент наа каждой итерации
        if real_item == item:  # проверяем, равен ли текущий элемент искомому элементу
            return index  # Если текущий элемент совпадает с искомым, мы возвращаем его индекс


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = search_index(items_list, find_item)    # для каждого элемента спика вызываем search_index передавая
    # items_list и текущий элемент find_item
    if index_item is not None:    # проверяем, не равно ли значение index_item None (исли не равно, значит элемент найден)
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
