import csv
import os
import re


class FirstCapitalLetter:
    """
    Дескриптор для проверки, что имена содержат только буквы и начинаются с заглавной буквы.
    """

    def __get__(self, instance, owner):
        return instance._value

    def __set__(self, instance, value):
        if not value.isalpha() or not value[0].isupper():
            raise ValueError(f"{instance._name} должно содержать только буквы и начинаться с заглавной буквы.")
        instance._value = value


class Student:
    """
    Представляет студента с именем, фамилией, отчеством, предметами и соответствующими оценками и результатами тестов.
    """

    first_name = FirstCapitalLetter()
    last_name = FirstCapitalLetter()
    patronymic = FirstCapitalLetter()

    DEFAULT_ITEMS = ['Математика', 'Физика', 'Литература']

    def __init__(self, first_name, last_name, patronymic, items_csv):
        """
        Инициализирует новый экземпляр класса Student с заданным именем, фамилией, отчеством и загружает названия предметов
        из CSV-файла, если такой файл существует, в противном случае создает CSV-файл с предметами по умолчанию.

        :param first_name: Имя студента.
        :param last_name: Фамилия студента.
        :param patronymic: Отчество студента.
        :param items_csv: Путь к CSV-файлу с названиями предметов.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self._load_items_from_csv(items_csv)
        self.subjects = {item: {'grades': [], 'results': []} for item in self.items}

    def _load_items_from_csv(self, items_csv):
        """
        Загружает названия предметов из CSV-файла или создает CSV-файл с предметами по умолчанию, если он не существует.

        :param items_csv: Путь к CSV-файлу с названиями предметов.
        """
        if not os.path.exists(items_csv):
            self._create_items_csv(items_csv)
        self.items = self._read_items_from_csv(items_csv)

    @staticmethod
    def _create_items_csv(items_csv):
        """
        Создает CSV-файл с предметами по умолчанию.

        :param items_csv: Путь к CSV-файлу, который будет создан.
        """
        with open(items_csv, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(Student.DEFAULT_ITEMS)

    @staticmethod
    def _read_items_from_csv(items_csv):
        """
        Считывает названия предметов из CSV-файла.

        :param items_csv: Путь к CSV-файлу с названиями предметов.
        :return: Список названий предметов.
        """
        with open(items_csv, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            return next(reader)

    def add_subject_score(self, subject, grade, test_score):
        """
        Добавляет оценку и результат теста по предмету.

        :param subject: Предмет, для которого добавляется оценка и результат теста.
        :param grade: Оценка (от 2 до 5).
        :param test_score: Результат теста (от 0 до 100).
        """
        if subject not in self.items:
            raise ValueError(f"Недопустимый предмет: {subject}.")
        if not 2 <= grade <= 5:
            raise ValueError("Оценка должна быть от 2 до 5.")
        if not 0 <= test_score <= 100:
            raise ValueError("Результат теста должен быть от 0 до 100.")

        self.subjects[subject]['grades'].append(grade)
        self.subjects[subject]['results'].append(test_score)

    def get_subject_average_score(self, subject):
        """
        Вычисляет средний результат теста по предмету.

        :param subject: Предмет, для которого вычисляется средний результат теста.
        :return: Средний результат теста по предмету.
        """
        if subject not in self.items:
            raise ValueError(f"Недопустимый предмет: {subject}.")
        scores = self.subjects[subject]['results']
        return sum(scores) / len(scores) if scores else 0

    def get_total_average_score(self):
        """
        Вычисляет средний результат теста по всем предметам.

        :return: Средний результат теста по всем предметам.
        """
        total_scores = [score for subject in self.subjects.values() for score in subject['results']]
        return sum(total_scores) / len(total_scores) if total_scores else 0

    def get_combined_grades(self):
        """
        Возвращает список всех оценок, объединенных для всех предметов.

        :return: Список всех оценок, объединенных для всех предметов.
        """
        combined_grades = [grade for subject in self.subjects.values() for grade in subject['grades']]
        return combined_grades


if __name__ == "__main__":
    items_csv_file = "item_names.csv"
    first_name = "Алексей"
    last_name = "Дмитриев"
    patronymic = "Михайлович"

    # Добавление оценок и результатов тестов по предметам
    student = Student(first_name, last_name, patronymic, items_csv_file)
    student.add_subject_score('Математика', 4, 87)
    student.add_subject_score('Физика', 4, 88)
    student.add_subject_score('Литература', 5, 98)

    # Вычисление средних результатов тестов
    math_average = student.get_subject_average_score('Математика')
    physics_average = student.get_subject_average_score('Физика')
    literature_average = student.get_subject_average_score('Литература')
    total_average = student.get_total_average_score()
    combined_grades = student.get_combined_grades()

    print(f"Средний результат по Математике: {math_average:.2f}")
    print(f"Средний результат по Физике: {physics_average:.2f}")
    print(f"Средний результат по Литературе: {literature_average:.2f}")
    print(f"Средний результат по всем предметам: {total_average:.2f}")
    print(f"Все оценки для всех предметов: {combined_grades}")
