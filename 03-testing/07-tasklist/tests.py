from datetime import date, timedelta
import pytest
from tasks import *
from calendars import *

@pytest.fixture
def today():
    return date(2000, 1, 1)

@pytest.fixture
def tomorrow(today):
    return today + timedelta(days=1)

@pytest.fixture
def yesterday(today):
    return today - timedelta(days=1)

@pytest.fixture
def calendar(today):
    return CalendarStub(today)

@pytest.fixture
def sut(calendar):
    return TaskList(calendar)

def test_task_becomes_overdue(sut, tomorrow, calendar):
    # Arrange
    next_week = date(2000, 1, 8)
    task = Task('description', tomorrow)
    sut.add_task(task)

    # Act
    calendar.today = next_week

    # Assert
    assert [task] == sut.overdue_tasks

def test_creation(sut):
    assert 0 == len(sut)
    assert [] == sut.due_tasks
    assert [] == sut.overdue_tasks
    assert [] == sut.finished_tasks

def test_adding_task_with_due_day_in_future(tomorrow, sut):
    # Arrange
    task = Task('bake bread', tomorrow)

    # Action
    sut.add_task(task)

    # Assert
    assert 1 == len(sut)
    assert [task] == sut.due_tasks

def test_adding_task_with_due_day_in_past(yesterday, sut):
    # Arrange
    task = Task('bake bread', yesterday)

    # Action Assert
    with pytest.raises(RuntimeError):
        sut.add_task(task)

def test_task_becomes_finished(tomorrow, sut):
    # Arrange
    task = Task('bake bread', tomorrow)

    sut.add_task(task)
    assert [task] == sut.due_tasks

    # Action
    task.finished = True

    # Assert
    assert [] == sut.due_tasks



