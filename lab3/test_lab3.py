import pytest
from student import Student
from student_list import StudentList


@pytest.fixture
def setup_list():
    sl = StudentList()
    sl.students = [
        Student("Bob", "1", "b@x.com", "Kyiv"),
        Student("Emma", "2", "e@x.com", "Lviv"),
        Student("Jon", "3", "j@x.com", "Odesa"),
    ]
    return sl


def test_add(setup_list):
    sl = setup_list
    s = Student("Chris", "5", "c@x.com", "Kharkiv")

    sl.add(s)

    names = [st.name for st in sl.get_all()]
    assert names == ["Bob", "Chris", "Emma", "Jon"]


def test_delete_exists(setup_list):
    sl = setup_list

    assert sl.delete("Emma") is True
    names = [st.name for st in sl.get_all()]
    assert names == ["Bob", "Jon"]


def test_delete_not_exists(setup_list):
    sl = setup_list

    assert sl.delete("Alex") is False
    assert len(sl.get_all()) == 3


def test_update(setup_list):
    sl = setup_list

    new = Student("Jon Smith", "99", "smith@mail.com", "Odesa")
    assert sl.update("Jon", new) is True

    names = [st.name for st in sl.get_all()]
    assert names == ["Bob", "Emma", "Jon Smith"]

    last = sl.get_all()[-1]
    assert last.phone == "99"
    assert last.email == "smith@mail.com"