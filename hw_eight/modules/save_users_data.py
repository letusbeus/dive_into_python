import csv
import json


def save_users_to_json():
    while True:
        name = input("Enter username (or 'q' to log out): ")
        if name == 'q':
            break

        user_id = input("Enter your personal user ID:")

        while True:
            access_level = input("Enter access level (from 1 to 7): ")
            if access_level.isdigit() and 1 <= int(access_level) <= 7:
                break
            else:
                print("Invalid access level. Try again.")

        # Загрузка существующих данных из файла
        try:
            with open('users.json', 'r') as file:
                data = json.load(file)
                if isinstance(data, list):
                    users = {}
                else:
                    users = data
        except FileNotFoundError:
            users = {}

        # Создание нового пользователя
        user = {
            'name': name,
            'user_id': user_id,
            'access_level': int(access_level)
        }

        # Проверка уникальности идентификатора пользователя
        for existing_user in users.get(access_level, []):
            if existing_user['user_id'] == user_id:
                print("A user with this ID already exists.")
                break
        else:
            # Добавление нового пользователя в словарь пользователей
            if access_level in users:
                users[access_level].append(user)
            else:
                users[access_level] = [user]

            # Сохранение обновленных данных в файл
            with open('users.json', 'w', encoding='utf-8') as file:
                json.dump(users, file, indent=4)

            print("User data successfully added.")


def save_users_to_csv():
    try:
        with open('users.json', 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        print("File users.json not found.")
        return

    fieldnames = ['Name', 'User ID', 'Access Level']

    try:
        with open('users.csv', 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for user_list in users.values():
                for user in user_list:
                    writer.writerow(
                        {'Name': user['name'], 'User ID': user['user_id'], 'Access Level': user['access_level']})

        print("User data successfully saved to file users.csv.")
    except IOError:
        print("Error saving data to file users.csv.")


def update_user_data(csv_file, json_file):
    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)
            rows = list(reader)
    except FileNotFoundError:
        print(f"File {csv_file} not found.")
        return

    converted_data = []
    for row in rows:
        # Преобразование данных и добавление хеша
        name = row[0].capitalize()
        user_id = row[1].zfill(10)
        access_level = int(row[2])
        hash_value = hash(name + user_id)

        converted_data.append({
            'Name': name,
            'User ID': user_id,
            'Access Level': access_level,
            'Hash': hash_value
        })

    try:
        with open(json_file, 'w', encoding='utf-8') as file:
            json.dump(converted_data, file, indent=4)
        print(f"Data from {csv_file} successfully read, converted and saved to {json_file}.")
    except IOError:
        print(f"Error saving data to file {json_file}.")
