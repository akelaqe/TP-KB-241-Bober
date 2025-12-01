import sys
from student import Student
from student_list import StudentList
from file_manager import FileManager


def main():
    if len(sys.argv) < 2:
        print("Помилка: Не вказано ім'я CSV файлу.")
        print("Приклад: python main.py students.csv")
        return

    filename = sys.argv[1]
    student_list = StudentList()

    # load
    student_list.students = FileManager.load(filename)
    student_list.sort()

    while True:
        choice = input("Дія [C,U,D,P,X]: ").lower()

        if choice == "c":
            name = input("Ім'я: ")
            phone = input("Телефон: ")
            email = input("Email: ")
            address = input("Адреса: ")
            student_list.add(Student(name, phone, email, address))
            print("Студента додано.")

        elif choice == "u":
            target = input("Кого оновити (ім'я): ")
            if not any(s.name == target for s in student_list.get_all()):
                print("Не знайдено.")
                continue

            new_name = input("Нове ім'я: ")
            phone = input("Новий телефон: ")
            email = input("Новий email: ")
            address = input("Нова адреса: ")

            student_list.update(target, Student(new_name, phone, email, address))
            print("Оновлено.")

        elif choice == "d":
            target = input("Кого видалити: ")
            if student_list.delete(target):
                print("Видалено.")
            else:
                print("Не знайдено.")

        elif choice == "p":
            print("\nПоточний список студентів:")
            for s in student_list.get_all():
                print(f"{s.name}, {s.phone}, {s.email}, {s.address}")

        elif choice == "x":
            FileManager.save(filename, student_list.get_all())
            print("Дані збережено. Вихід.")
            break

        else:
            print("Невірна команда.")


if __name__ == "__main__":
    main()