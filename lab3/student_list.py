from student import Student


class StudentList:
    def __init__(self):
        self.students: list[Student] = []

    def sort(self):
        self.students.sort(key=lambda s: s.name)

    def add(self, student: Student):
        """Додає нового студента у відсортовану позицію."""
        index = 0
        for s in self.students:
            if student.name > s.name:
                index += 1
            else:
                break
        self.students.insert(index, student)

    def delete(self, name: str) -> bool:
        """Повертає True якщо видалення відбулося."""
        for s in self.students:
            if s.name == name:
                self.students.remove(s)
                return True
        return False

    def update(self, name: str, new_student: Student) -> bool:
        """Оновлює інформацію про студента."""
        for s in self.students:
            if s.name == name:
                self.students.remove(s)
                self.add(new_student)
                return True
        return False

    def get_all(self) -> list[Student]:
        return self.students