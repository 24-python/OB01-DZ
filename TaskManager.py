# Задача: Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты:
# описание задачи, срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач,
# отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task():
    def __init__(self, description, deadline, status):
        self.description = description
        self.deadline = deadline
        self.status = status

    def add_task(self):
        pass

    def mark_as_done(self):
        pass

    def print_tasks(self):
        pass