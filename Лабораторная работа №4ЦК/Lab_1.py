import json


def task() -> float:  # функция возвращает число с плавающей запятой
    filename = "input.json"
    try:
        with open(filename) as f:  # with гарантирует что файл будет закрыт автоматически после завершения блока кода
            json_data = json.load(f)  # загружается содержимое открытого файла f
    except FileNotFoundError:   # если файл не найден, то появится сообщение об ошибке
        print(f"Ошибка: Файл '{filename}' не найден.")
        return 0.0

    sum_values = sum([item["score"] * item["weight"] for item in json_data])  # генератор списка, который перебирает
    # каждый элемент item / для каждого элемента json_data происходит умножение значений по ключам score и weight
    return round(sum_values, 3)  # возвращаем sum_values, округляем до 3-х знаков


print(task())
