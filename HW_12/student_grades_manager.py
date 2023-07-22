import csv
import os


class FirstCapitalLetter:
    """
    Дескриптор для проверки, что имена содержат только буквы и начинаются с заглавной буквы.
    """

    def __init__(self, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if not value.isalpha() or not value[0].isupper():
            raise ValueError(
                "{} должно содержать только буквы и начинаться с заглавной буквы.".format(
                    self._name
                )
            )
        instance.__dict__[self._name] = value


class Student:
    """
    Представляет студента с именем, фамилией, отчеством, предметами и соответствующими оценками и результатами тестов.
    """

    first_name = FirstCapitalLetter("_first_name")
    last_name = FirstCapitalLetter("_last_name")
    patronymic = FirstCapitalLetter("_patronymic")

    DEFAULT_ITEMS = ["Математика", "Физика", "Литература"]

    def __init__(self, first_name, last_name, patronymic, items_csv):
        """
        Инициализирует новый экземпляр класса Student с заданным именем, фамилией, отчеством и загружает названия предметов
        из CSV-файла, если такой файл существует, в противном случае создает CSV-файл с предметами по умолчанию.

        :param first_name: Имя студента.
        :param last_name: Фамилия студента.
        :param patronymic: Отчество студента.
        :param items_csv: Путь к CSV-файлу с названиями предметов.
        """
        self._first_name = first_name
        self._last_name = last_name
        self._patronymic = patronymic
        self._load_items_from_csv(items_csv)
        self.subjects = {item: {"grades": [], "results": []} for item in self.items}

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
        with open(items_csv, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(Student.DEFAULT_ITEMS)

    @staticmethod
    def _read_items_from_csv(items_csv):
        """
        Считывает названия предметов из CSV-файла.

        :param items_csv: Путь к CSV-файлу с названиями предметов.
        :return: Список названий предметов.
        """
        with open(items_csv, "r", encoding="utf-8") as file:
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
            raise ValueError("Недопустимый предмет: {}.".format(subject))
        if not 2 <= grade <= 5:
            raise ValueError("Оценка должна быть от 2 до 5.")
        if not 0 <= test_score <= 100:
            raise ValueError("Результат теста должен быть от 0 до 100.")

        self.subjects[subject]["grades"].append(grade)
        self.subjects[subject]["results"].append(test_score)

    def get_subject_average_score(self, subject):
        """
        Вычисляет средний результат теста по предмету.

        :param subject: Предмет, для которого вычисляется средний результат теста.
        :return: Средний результат теста по предмету.
        """
        if subject not in self.items:
            raise ValueError("Недопустимый предмет: {}.".format(subject))
        scores = self.subjects[subject]["results"]
        return sum(scores) / len(scores) if scores else 0

    def get_total_average_score(self):
        """
        Вычисляет средний результат теста по всем предметам.

        :return: Средний результат теста по всем предметам.
        """
        total_scores = [
            score for subject in self.subjects.values() for score in subject["results"]
        ]
        return sum(total_scores) / len(total_scores) if total_scores else 0

    def get_combined_grades(self):
        """
        Возвращает список всех оценок, объединенных для всех предметов.

        :return: Список всех оценок, объединенных для всех предметов.
        """
        combined_grades = [
            grade for subject in self.subjects.values() for grade in subject["grades"]
        ]
        return combined_grades

    @classmethod
    def create_from_csv(cls, csv_file):
        """
        Создает объекты класса Student на основе данных из CSV-файла.

        :param csv_file: Путь к CSV-файлу с данными студентов.
        :return: Список объектов класса Student с данными из CSV-файла.
        """
        csv_file = os.path.abspath(csv_file)
        if not os.path.exists(csv_file):
            # Если файл не существует, создаем CSV-файл с предметами по умолчанию
            cls._create_items_csv(csv_file)

        students = []
        with open(csv_file, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for first_name, last_name, patronymic in reader:
                student = cls(first_name, last_name, patronymic, csv_file)
                for subject, grades_and_scores in reader:
                    grades_and_scores = grades_and_scores.split(",")
                    for grade_and_score in grades_and_scores:
                        grade, score = map(int, grade_and_score.strip().split())
                        student.add_subject_score(subject, grade, score)
                students.append(student)

        return students

    @classmethod
    def add_student_to_csv(cls, csv_file, first_name, last_name, patronymic, subjects):
        """
        Добавляет данные о новом студенте в CSV-файл.

        :param csv_file: Путь к CSV-файлу с данными студентов.
        :param first_name: Имя студента.
        :param last_name: Фамилия студента.
        :param patronymic: Отчество студента.
        :param subjects: Список предметов, для которых добавляется оценка и результат теста.
        """
        csv_file = os.path.abspath(csv_file)
        if not os.path.exists(csv_file):
            cls._create_items_csv(csv_file)

        with open(csv_file, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([first_name, last_name, patronymic])
            writer.writerow(["Оценки и Результаты Тестов"])
            for subject_data in subjects:
                subject, grade, test_score = subject_data
                writer.writerow([subject, f"{grade} {test_score}"])


if __name__ == "__main__":
    items_csv_file = "student_data.csv"

    # Get student's personal information interactively from the user
    first_name = input("Введите имя студента: ")
    last_name = input("Введите фамилию студента: ")
    patronymic = input("Введите отчество студента: ")

    # Initialize the student object with the provided personal information
    student = Student(first_name, last_name, patronymic, items_csv_file)

    # Get the number of subjects the user wants to add
    num_subjects = int(input("Сколько предметов вы хотите добавить? "))

    # Add subject scores interactively
    subjects = []
    for i in range(num_subjects):
        subject = input(f"Введите название предмета {i + 1}: ")
        grade = int(input(f"Введите оценку для предмета {subject}: "))
        test_score = int(input(f"Введите результат теста для предмета {subject}: "))
        subjects.append((subject, grade, test_score))

    # Add the new student to the CSV file
    Student.add_student_to_csv(
        items_csv_file, first_name, last_name, patronymic, subjects
    )

    # Calculate and display the average results
    math_average = student.get_subject_average_score("Математика")
    physics_average = student.get_subject_average_score("Физика")
    literature_average = student.get_subject_average_score("Литература")
    total_average = student.get_total_average_score()
    combined_grades = student.get_combined_grades()

    print("Средний результат по Математике: {:.2f}".format(math_average))
    print("Средний результат по Физике: {:.2f}".format(physics_average))
    print("Средний результат по Литературе: {:.2f}".format(literature_average))
    print("Средний результат по всем предметам: {:.2f}".format(total_average))
    print("Все оценки для всех предметов: {}".format(combined_grades))

    # Create a new student object from the CSV file
    new_student = Student.create_from_csv("student_data.csv")
    print("\nНовый студент, созданный из CSV-файла:")
    print("Имя: {}".format(new_student._first_name))
    print("Фамилия: {}".format(new_student._last_name))
    print("Отчество: {}".format(new_student._patronymic))
    print("Предметы: {}".format(list(new_student.subjects.keys())))
