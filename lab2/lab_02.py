import csv
import sys


students = []

def load_data(filename):
    """Завантажує дані студентів із CSV-файлу до глобального списку students."""
    global students
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            students = [row for row in reader]
            students.sort(key=lambda x: x['name']) 
        print(f"Дані успішно завантажено з файлу {filename}")
    except FileNotFoundError:
        print(f"Увага: Файл {filename} не знайдено. Починаємо з порожнього довідника.")
        students = [] 
    except Exception as e:
        print(f"Виникла помилка при завантаженні файлу: {e}")
        sys.exit(1)

def save_data(filename):
    """Зберігає поточні дані студентів у CSV-файл."""
    if not students:
        print("Список студентів порожній, нічого зберігати.")
        return
        
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = students[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
        print(f"Дані успішно збережено у файл {filename}")
    except Exception as e:
        print(f"Виникла помилка при збереженні файлу: {e}")

def printAllList():
    if not students:
        print("Довідник порожній.")
        return
    for elem in students:
        strForPrint = (
            f"Ім'я: {elem['name']}, "
            f"Телефон: {elem['phone']}, "
            f"Email: {elem['email']}, "
            f"Адреса: {elem['address']}"
        )
        print(strForPrint)

def addNewElement():
    name = input("Введіть ім'я студента: ")
    phone = input("Введіть телефон студента: ")
    email = input("Введіть email студента: ")
    address = input("Введіть адресу студента: ")

    newItem = {"name": name, "phone": phone, "email": email, "address": address}

    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)
    print("Нового студента було додано.")

def deleteElement():
    name = input("Введіть ім'я студента для видалення: ")
    found = None
    for item in students:
        if name == item["name"]:
            found = item
            break

    if found is None:
        print("Студента не знайдено.")
    else:
        students.remove(found)
        print(f"Студента {name} було видалено.")

def updateElement():
    name = input("Введіть ім'я студента для оновлення: ")
    original_item = None
    for item in students:
        if item["name"] == name:
            original_item = item
            break

    if original_item is None:
        print("Студента не знайдено.")
        return

    print("Залиште поле порожнім, якщо не бажаєте його змінювати.")
    new_name = input(f"Нове ім'я (поточне: {original_item['name']}): ") or original_item['name']
    new_phone = input(f"Новий телефон (поточний: {original_item['phone']}): ") or original_item['phone']
    new_email = input(f"Новий email (поточний: {original_item['email']}): ") or original_item['email']
    new_address = input(f"Нова адреса (поточна: {original_item['address']}): ") or original_item['address']

    updatedItem = {
        "name": new_name,
        "phone": new_phone,
        "email": new_email,
        "address": new_address
    }
    
    students.remove(original_item)
    
    insertPosition = 0
    for item in students:
        if new_name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, updatedItem)

    print("Інформацію про студента оновлено.")

def main():
    if len(sys.argv) < 2:
        print("Помилка: Не вказано ім'я файлу для роботи.")
        print("Приклад запуску: python main.py students.csv")
        sys.exit(1)
        
    csv_filename = sys.argv[1]
    load_data(csv_filename)
    
    while True:
        choice = input("Дія [C-створити, U-оновити, D-видалити, P-друк, X-вихід]: ")
        match choice.lower():
            case "c":
                print("Створення нового запису:")
                addNewElement()
                printAllList()
            case "u":
                print("Оновлення існуючого запису:")
                updateElement()
                printAllList()
            case "d":
                print("Видалення запису:")
                deleteElement()
                printAllList()
            case "p":
                print("Поточний список студентів:")
                printAllList()
            case "x":
                print("Збереження даних та вихід...")
                save_data(csv_filename)
                break
            case _:
                print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()