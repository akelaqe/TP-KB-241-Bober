class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age} років)"



students = [
    Student("Anna", 19),
    Student("Oleksii", 21),
    Student("Maria", 18),
    Student("Ivan", 20),
]


sorted_list = sorted(students, key=lambda s: s.age)

print("Сортування за віком:")
for s in sorted_list:
    print(s)