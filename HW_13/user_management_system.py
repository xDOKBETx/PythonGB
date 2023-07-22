''' Задание №5
Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы: 
загрузка данных (функция из задания 4) вход в систему - требует указать имя и id пользователя. 
Для проверки наличия пользователя в множестве используйте магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение доступа. 
А если пользователь есть, получите его уровень из множества пользователей. 
Добавление пользователя: если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.
'''


import json
import os


class BaseCustomException(Exception):
    """Базовый класс пользовательского исключения."""
    pass


class LevelError(BaseCustomException):
    """Дочерний класс исключения для ошибок уровня."""

    def __init__(self, message, current_level, required_level):
        self.message = message
        self.current_level = current_level
        self.required_level = required_level
        super().__init__(message)


class AccessError(BaseCustomException):
    """Дочерний класс исключения для ошибок доступа."""

    def __init__(self, message, user_id):
        self.message = message
        self.user_id = user_id
        super().__init__(message)


class User:
    def __init__(self, name, user_id, access_level):
        self.name = name
        self.user_id = user_id
        self.access_level = access_level

    def __eq__(self, other):
        if isinstance(other, User):
            return self.user_id == other.user_id
        return False


def get_ids(filename):
    all_ids = set()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for level in data:
                all_ids.update(level.keys())
    return all_ids


def get_name():
    name = input("Введите имя пользователя: ")
    return name


def get_user_id(all_ids):
    user_id = -1
    while user_id < 0 or user_id in all_ids:
        try:
            user_id = int(input("Введите личный идентификатор пользователя: "))
        except ValueError:
            print("Ошибка: Некорректный идентификатор. Повторите ввод.")
    all_ids.add(user_id)
    return user_id


def get_access_level():
    access_level = 0
    while not 1 <= access_level <= 7:
        try:
            access_level = int(input("Введите уровень доступа пользователя (от 1 до 7): "))
        except ValueError:
            print("Ошибка: Некорректный уровень доступа. Повторите ввод.")
    return access_level


def add_user_to_dict(all_ids):
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
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(working_dict, f, ensure_ascii=False, indent=4)


def generate_users_from_json(filename):
    users = set()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for level in data.values():
                for user_data in level.values():
                    user = User(user_data['name'], user_data['user_id'], user_data['access_level'])
                    users.add(user)
    return users


class Project:
    def __init__(self, filename):
        self.filename = filename
        self.users = generate_users_from_json(filename)

    def load_data(self):
        self.users = generate_users_from_json(self.filename)

    def login(self, name, user_id):
        user_to_login = User(name, user_id, 0)
        if user_to_login not in self.users:
            raise AccessError(f"Ошибка доступа - Пользователь с идентификатором {user_id} не найден.", user_id)

        for user in self.users:
            if user == user_to_login:
                user_to_login.access_level = user.access_level
                break

        return user_to_login.access_level

    def add_user(self, name, user_id, access_level):
        user_to_add = User(name, user_id, access_level)
        current_user = User("", -1, 0)

        for user in self.users:
            if user == current_user:
                current_user = user
                break

        if current_user.access_level < access_level:
            raise LevelError(f"Ошибка уровня - Недостаточный уровень доступа ({current_user.access_level}) для добавления пользователя с уровнем доступа {access_level}.", current_user.access_level, access_level)

        self.users.add(user_to_add)
        save_dict_to_json({access_level: [user.__dict__ for user in self.users]}, self.filename)


def main():
    filename = 'users.json'
    project = Project(filename)

    while True:
        try:
            name = get_name()
            if not name:
                break

            user_id = get_user_id({user.user_id for user in project.users})
            access_level = get_access_level()

            project.add_user(name, user_id, access_level)

        except ValueError as ve:
            print("Ошибка:", ve)
        except LevelError as le:
            print(le.message)
            print(f"Текущий уровень доступа: {le.current_level}, Требуемый уровень доступа: {le.required_level}")
        except AccessError as ae:
            print(ae.message)
            print(f"Идентификатор пользователя: {ae.user_id}")


if __name__ == '__main__':
    main()
