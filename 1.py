from datetime import datetime

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.is_completed = False

    def mark_as_completed(self):
        self.is_completed = True

    def __str__(self):
        status = 'Выполнено' if self.is_completed else 'Не выполнено'
        return f"{self.description} (До: {self.deadline}) - {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_completed()
        else:
            raise IndexError("Некорректный индекс задачи")

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.is_completed]

    def display_pending_tasks(self):
        pending_tasks = self.get_pending_tasks()
        if not pending_tasks:
            print("Все задачи выполнены!")
        else:
            for task in pending_tasks:
                print(task)


# Пример использования
task_manager = TaskManager()

# Добавление задач
task_manager.add_task("Купить продукты", "2023-10-15")
task_manager.add_task("Закончить отчет", "2023-10-10")

# Отметка выполнения задачи
task_manager.mark_task_as_completed(1)

# Вывод текущих (не выполненных) задач
task_manager.display_pending_tasks()