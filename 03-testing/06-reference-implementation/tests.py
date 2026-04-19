import pytest
from search import *

class Student:
    def __init__(self, id):
        self.id = id

john = Student(1)
mary = Student(2)
bryan = Student(3)
lucy = Student(4)
dan = Student(5)


@pytest.mark.parametrize('students, target_id', [
    ([john, mary, bryan, lucy, dan], 1),
    ([john, mary, bryan, lucy, dan], 5),
    ([john, mary, bryan, lucy, dan], 3)
])

def test_linear_search(students, target_id):
    assert linear_search(students, target_id).id == target_id


@pytest.mark.parametrize('students, target_id', [
    ([john, mary, bryan, lucy, dan], 1),
    ([john, mary, bryan, lucy, dan], 5),
    ([john, mary, bryan, lucy, dan], 3)
])
def test_binary_search(students, target_id):
    assert binary_search(students, target_id).id == target_id

@pytest.mark.parametrize('students, target_id', [
    ([john, mary, bryan, lucy, dan], 8),
    ([], 4)
])
def test_return_none_linear_search(students, target_id):
    assert linear_search(students, target_id) == None

@pytest.mark.parametrize('students, target_id', [
    ([john, mary, bryan, lucy, dan], 8),
    ([], 4)
])


@pytest.mark.parametrize('id', range(0, 100))
def test_return_none_binary_search(students, target_id):
    assert binary_search(students, target_id) == None