from datetime import datetime

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"

# Список для хранения задач
tasks = []

# Функция для добавления задачи
def add_task(description, deadline):
    task = Task(description, deadline)
    tasks.append(task)

# Функция для отметки задачи выполненной
def mark_task_completed(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index].mark_completed()
    else:
        print("Некорректный индекс задачи")

# Функция для получения списка невыполненных задач
def get_incomplete_tasks():
    incomplete_tasks = [task for task in tasks if not task.completed]
    return incomplete_tasks

# Функция для вывода всех задач
def show_tasks():
    if not tasks:
        print("Нет задач")
    else:
        for index, task in enumerate(tasks):
            print(f"{index}. {task}")

# Пример использования:
add_task("Сделать домашнее задание", "2024-09-30")
add_task("Купить продукты", "2024-09-26")

print("Список задач:")
show_tasks()

print("\nОтметим задачу выполненной:")
mark_task_completed(0)

print("\nТекущие задачи (не выполненные):")
for task in get_incomplete_tasks():
    print(task)
