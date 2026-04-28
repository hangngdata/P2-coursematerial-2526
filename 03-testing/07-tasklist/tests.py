from datetime import date, timedelta
import pytest
from tasks import *
from calendars import *

def setup_function():
    global today, tomorrow, yesterday, calendar, sut
    today = date(2000, 1, 1)
    tomorrow = today + timedelta(days=1)
    yesterday = today - timedelta(days=1)
    calendar = CalendarStub(today)
    sut = TaskList(calendar)


def test_task_becomes_overdue():
    # Arrange
    next_week = date(2000, 1, 8)
    task = Task('description', tomorrow)
    sut.add_task(task)

    # Act
    calendar.today = next_week

    # Assert
    assert [task] == sut.overdue_tasks

def test_creation():
    assert 0 == len(sut)
    assert [] == sut.due_tasks
    assert [] == sut.overdue_tasks
    assert [] == sut.finished_tasks

def test_adding_task_with_due_day_in_future():
    # Arrange
    today = date(2026, 4, 28)
    tomorrow = date(2026, 4, 29)

    task = Task('bake bread', tomorrow)

    # Action
    sut.add_task(task)

    # Assert
    assert 1 == len(sut)
    assert [task] == sut.due_tasks

def test_adding_task_with_due_day_in_past():
    # Arrange
    task = Task('bake bread', yesterday)

    # Action Assert
    with pytest.raises(RuntimeError):
        sut.add_task(task)

def test_task_becomes_finished():
    # Arrange
    task = Task('bake bread', tomorrow)

    sut.add_task(task)
    assert [task] == sut.due_tasks

    # Action
    task.finished = True

    # Assert
    assert [] == sut.due_tasks



