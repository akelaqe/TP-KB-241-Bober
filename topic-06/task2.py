students = [
    {"name": "Anna", "grade": 95},
    {"name": "Oleksii", "grade": 72},
    {"name": "Maria", "grade": 88},
    {"name": "Ivan", "grade": 60},
    {"name": "Sofiia", "grade": 100}
]

sorted_by_name = sorted(students, key=lambda x: x["name"])
print("Сортування за ім’ям:", sorted_by_name)


sorted_by_grade = sorted(students, key=lambda x: x["grade"], reverse=True)
print("Сортування за оцінкою:", sorted_by_grade)
