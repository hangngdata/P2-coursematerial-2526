from datetime import date, timedelta
from calendars import Calendar

class Task:
    def __init__(self, description, due_date):
        self.__description = description
        self.__due_date = due_date
        self.finished = False
    
    @property
    def description(self):
        return self.__description
    
    @property
    def due_date(self):
        return self.__due_date
    
    @property
    def finished(self):
        return self.__finished
    
    @finished.setter
    def finished(self, value):
        self.__finished = value

    def __repr__(self):
        return f"{self.description}"


class TaskList:
    def __init__(self, calendar):
        self.tasks = []
        self.__calendar = calendar
    
    @property
    def current_date(self):
        return self.__calendar.today
    
    def __len__(self):
        return len(self.tasks)

    def add_task(self, task):
        if task.due_date < self.current_date:
            raise RuntimeError
        self.tasks.append(task)

    @property
    def finished_tasks(self):
        return [task for task in self.tasks if task.finished]
    
    @property
    def due_tasks(self):
        return [task for task in self.tasks if not task.finished]
    
    @property
    def overdue_tasks(self):
        return [task for task in self.tasks if not task.finished and task.due_date < self.current_date]
    
