def find_common_participants(group1, group2, separator=','):
    # Разбиваем строки на списки участников
    participants1 = group1.split(separator)
    participants2 = group2.split(separator)

    # Находим общих участников
    common_participants = set(participants1) & set(participants2)

    # Сортируем общих участников в алфавитном порядке
    common_participants = sorted(list(common_participants))

    return common_participants


# Пример использования функции
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
separator = ','

result = find_common_participants(participants_first_group, participants_second_group, separator)
print("Все участники", result)
