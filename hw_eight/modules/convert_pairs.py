import json


def convert_txt_pairs_to_json(txt_file, json_file):
    data = []

    # Чтение данных из текстового файла
    with open(txt_file, 'r') as file:
        lines = file.readlines()

    # Обработка каждой строки и добавление данных в список
    for line in lines:
        name, number = line.strip().split('; ')
        data.append({'Name': name.capitalize(), 'Number': float(number)})

    # Запись данных в файл в формате JSON
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)
