import pytest
import lab_02 as dm  

@pytest.fixture
def setup_students(monkeypatch):
    """Ця фікстура готує "чистий" стан списку студентів перед кожним тестом."""
    test_data = [
        {"name": "Bob", "phone": "0631111111", "email": "bob@mail.com", "address": "Kyiv"},
        {"name": "Emma", "phone": "0632222222", "email": "emma@mail.com", "address": "Lviv"},
        {"name": "Jon", "phone": "0633333333", "email": "jon@mail.com", "address": "Odesa"},
    ]
    monkeypatch.setattr(dm, 'students', test_data)


def test_add_new_element(monkeypatch, setup_students):
    """Тестує додавання нового студента до довідника."""
    inputs = iter(["Chris", "0635555555", "chris@mail.com", "Kharkiv"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    dm.addNewElement()

    assert len(dm.students) == 4
    assert dm.students[1]["name"] == "Chris"
    assert dm.students[1]["phone"] == "0635555555"
    student_names = [s['name'] for s in dm.students]
    assert student_names == ["Bob", "Chris", "Emma", "Jon"]

def test_delete_element_exists(monkeypatch, setup_students):
    """Тестує видалення існуючого студента."""
    monkeypatch.setattr('builtins.input', lambda _: "Emma")
    
    dm.deleteElement()
    
    assert len(dm.students) == 2
    student_names = [s['name'] for s in dm.students]
    assert "Emma" not in student_names
    assert student_names == ["Bob", "Jon"]

def test_delete_element_not_exists(monkeypatch, setup_students):
    """Тестує спробу видалення студента, якого немає в списку."""
    initial_length = len(dm.students)
    monkeypatch.setattr('builtins.input', lambda _: "Alex")

    dm.deleteElement()

    assert len(dm.students) == initial_length

def test_update_element(monkeypatch, setup_students):
    """Тестує оновлення даних існуючого студента."""
    inputs = iter(["Jon", "Jon Smith", "0998887766", "jon.s@mail.com", "Odesa"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    dm.updateElement()
    assert len(dm.students) == 3
    
    student_names = [s['name'] for s in dm.students]
    assert student_names == ["Bob", "Emma", "Jon Smith"]
    
    updated_student = dm.students[2]
    assert updated_student['phone'] == "0998887766"
    assert updated_student['email'] == "jon.s@mail.com"