import csv
import json

def csv_to_json(csv_file_path, json_file_path):  # принимает два пути к файлам
    # Открываем CSV файл для чтения
    with open(csv_file_path, mode='r', newline='') as csv_file:  # with гарантирует, что файл будет закрыть после
        # завершения блока кода newline используется для правильной обработки строк в CSV
        reader = csv.DictReader(csv_file)  # создается объект который читает строки из CSV файла и преобразует каждую строку в словарь
        data = [row for row in reader if any(row.values())]  # Исключаем пустые строки (при комиляции появляется
        # не нужная пустая строка из-за которой не удается пройти expected, я пытался с этим бороться, но ничего не получилось  )

    # Записываем данные в JSON файл
    with open(json_file_path, mode='w', newline='') as json_file:
        json.dump(data, json_file, indent=4)  # indent=4 добавляет 4 отступа

# Пример использования
csv_file_path = 'input.csv'  # путь к CSV файлу
json_file_path = 'output.json'  # путь для сохранения JSON файла

csv_to_json(csv_file_path, json_file_path)  # передаем данные

# Для вывода JSON строки на экран
with open(json_file_path, 'r') as json_file:  # читаем json
    json_data = json_file.read()
    print(json_data)
