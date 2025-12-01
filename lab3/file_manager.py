import csv
from student import Student


class FileManager:

    @staticmethod
    def load(filename: str):
        students = []
        try:
            with open(filename, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    students.append(Student(
                        row["name"], row["phone"], row["email"], row["address"]
                    ))
        except FileNotFoundError:
            print(f"Файл {filename} не знайдено. Починаємо з порожнього списку.")
        return students

    @staticmethod
    def save(filename: str, students: list[Student]):
        with open(filename, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(
                file, fieldnames=["name", "phone", "email", "address"]
            )
            writer.writeheader()
            for s in students:
                writer.writerow(s.to_dict())