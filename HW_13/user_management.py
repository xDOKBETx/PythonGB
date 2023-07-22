""" Задание №4
Вспоминаем задачу из семинара 8 про сериализацию данных, 
где в бесконечном цикле запрашивали имя, личный идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей
"""

import json
import os


class User:
    def __init__(self, name, user_id, access_level):
        self.name = name
        self.user_id = user_id
        self.access_level = access_level


def get_ids(filename):
    """
    Возвращает все уникальные идентификаторы из JSON-файла.

    Args:
        filename (str): Имя файла JSON.

    Returns:
        set: Множество уникальных идентификаторов.
    """
    all_ids = set()
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            for level in data:
                all_ids.update(level.keys())
    return all_ids


def get_name():
    """
    Запрашивает имя пользователя.

    Returns:
        str: Имя пользователя.
    """
    name = input("Введите имя пользователя: ")
    return name


def get_user_id(all_ids):
    """
    Запрашивает личный идентификатор пользователя.

    Args:
        all_ids (set): Множество уникальных идентификаторов.

    Returns:
        int: Личный идентификатор пользователя.
    """
    user_id = -1
    while user_id < 0 or user_id in all_ids:
        try:
            user_id = int(input("Введите личный идентификатор пользователя: "))
        except ValueError:
            print("Ошибка: Некорректный идентификатор. Повторите ввод.")
    all_ids.add(user_id)
    return user_id


def get_access_level():
    """
    Запрашивает уровень доступа пользователя.

    Returns:
        int: Уровень доступа пользователя.
    """
    access_level = 0
    while not 1 <= access_level <= 7:
        try:
            access_level = int(
                input("Введите уровень доступа пользователя (от 1 до 7): ")
            )
        except ValueError:
            print("Ошибка: Некорректный уровень доступа. Повторите ввод.")
    return access_level


def add_user_to_dict(all_ids):
    """
    Добавляет информацию о пользователе в словарь.

    Args:
        all_ids (set): Множество уникальных идентификаторов.

    Returns:
        dict: Словарь с информацией о пользователях.
    """
    working_dict = {}

    while True:
        name = get_name()
        if not name:
            break

        user_id = get_user_id(all_ids)
        access_level = get_access_level()

        user = User(name, user_id, access_level)

        if access_level in working_dict:
            working_dict[access_level].update({user_id: user.__dict__})
        else:
            working_dict[access_level] = {user_id: user.__dict__}

        print("Информация о пользователе успешно добавлена.")

    return working_dict


def save_dict_to_json(working_dict, filename):
    """
    Сохраняет словарь в JSON-файл.

    Args:
        working_dict (dict): Словарь с информацией о пользователях.
        filename (str): Имя файла JSON.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(working_dict, f, ensure_ascii=False, indent=4)


def generate_users_from_json(filename):
    """
    Читает информацию из JSON-файла и генерирует множество пользователей.

    Args:
        filename (str): Имя файла JSON.

    Returns:
        set: Множество пользователей (объекты класса User).
    """
    users = set()
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            for level in data.values():
                for user_data in level.values():
                    user = User(
                        user_data["name"],
                        user_data["user_id"],
                        user_data["access_level"],
                    )
                    users.add(user)
    return users


def main():
    filename = "users.json"
    all_ids = get_ids(filename)

    working_dict = add_user_to_dict(all_ids)
    save_dict_to_json(working_dict, filename)

    generated_users = generate_users_from_json(filename)
    print("\nСгенерированные пользователи:")
    for user in generated_users:
        print(
            f"Имя: {user.name}, Личный идентификатор: {user.user_id}, Уровень доступа: {user.access_level}"
        )


if __name__ == "__main__":
    main()
