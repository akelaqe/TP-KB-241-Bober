
## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
students = [
    {"name": "Bob", "phone": "0631234567", "email": "bob@mail.com", "address": "Kyiv"},
    {"name": "Emma", "phone": "0631234567", "email": "emma@mail.com", "address": "Lviv"},
    {"name": "Jon", "phone": "0631234567", "email": "jon@mail.com", "address": "Odesa"},
    {"name": "Zak", "phone": "0631234567", "email": "zak@mail.com", "address": "Dnipro"}
]

def printAllList():
    for elem in students:
        strForPrint = (
            f"Student name: {elem['name']}, "
            f"Phone: {elem['phone']}, "
            f"Email: {elem['email']}, "
            f"Address: {elem['address']}"
        )
        print(strForPrint)
    return

def addNewElement():
    name = input("Enter student name: ")
    phone = input("Enter student phone: ")
    email = input("Enter student email: ")
    address = input("Enter student address: ")

    newItem = {"name": name, "phone": phone, "email": email, "address": address}

    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)
    print("New element has been added")
    return


def deleteElement():
    name = input("Enter name to be deleted: ")
    found = None
    for item in students:
        if name == item["name"]:
            found = item
            break

    if found is None:
        print("Student was not found")
    else:
        students.remove(found)
        print(f"Student {name} has been deleted")


def updateElement():
    name = input("Enter name of student to update: ")
    found = None
    for item in students:
        if item["name"] == name:
            found = item
            break

    if found is None:
        print("Student not found")
        return

    print("Leave field empty if you don't want to change it.")
    new_name = input(f"New name (current: {found['name']}): ") or found['name']
    new_phone = input(f"New phone (current: {found['phone']}): ") or found['phone']
    new_email = input(f"New email (current: {found['email']}): ") or found['email']
    new_address = input(f"New address (current: {found['address']}): ") or found['address']

    students.remove(found)
    updatedItem = {
        "name": new_name,
        "phone": new_phone,
        "email": new_email,
        "address": new_address
    }

    insertPosition = 0
    for item in students:
        if new_name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, updatedItem)

    print("Student information updated")

def main():
    while True:
        chouse = input("Action [ C create, U update, D delete, P print, X exit ]: ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong choice")


main()