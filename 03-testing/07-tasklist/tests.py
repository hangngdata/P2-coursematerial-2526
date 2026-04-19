from datetime import date, timedelta
from tasks import *
from calendars import *


def test_task_becomes_overdue():
    today_date = date.today()
    calendar_stub = CalendarStub(today_date)
    tasks = TaskList(calendar_stub)

    tomorrow = today_date + timedelta(days=1)
    task = Task('bake bread', tomorrow)
    tasks.add_task(task)

    assert len(tasks.overdue_tasks) == 0

    calendar_stub.today = today_date + timedelta(days=2)

    assert [task] == tasks.overdue_tasks

