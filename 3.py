class Task():
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
       self.tasks.append({'description': description, 'deadline': deadline, 'status': 'не выполнено'})

    def complite_task(self, description):
        for task in self.tasks:
            if task['description'] == description:
                task['status'] = 'выполнено'
                print(f'Задача {description} выполнена')
            else:
                print('Такой задачи нет')
    def show_task(self):
        print('Список задач: ')
        for task in self.tasks:
            if task['status'] == 'не выполнено':
                print(f'{task["description"]} (до: {task["deadline"]})')

    def del_complite_task(self):
        for task in self.tasks:
            if task['status'] == 'выполнено':
                self.tasks.remove(task)

t = Task()
t.add_task('Сделать домашку', '2023-10-01')
t.add_task('Прочитать книгу', '2023-10-02')
t.add_task('Пробежать марафон', '2023-10-10')

t.show_task()

t.complite_task('Сделать домашку')

t.del_complite_task()

t.show_task(

)






