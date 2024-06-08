class Task:
    def __init__(self, description, deadline, status=False):
        self.description = description
        self.deadline = deadline
        self.status = status

    def __str__(self):
        status = "Завершено" if self.status else "Не завершено"
        return f"Task(description='{self.description}', deadline='{self.deadline}', status='{status}')"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        new_task = Task(description, deadline)
        self.tasks.append(new_task)

    def mark_as_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].status = True
        else:
            print("Неверный номер задачи")

    def print_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

# Пример использования
task_manager = TaskManager()
task_manager.add_task("Сделать домашку", "2023-10-01")
task_manager.add_task("Купить продукты", "2023-10-02")

print("Tasks before marking as done:")
task_manager.print_tasks()

task_manager.mark_as_done(0)

print("\nTasks after marking first task as done:")
task_manager.print_tasks()