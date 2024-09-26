class Task():
    def __init__(self, description, time, status):
        self.description = description
        self.time = time
        self.status = status

    def task_status (self):
        if self.status == True:
            print('Выполнено')
        elif self.status == False:
            print('Не выполнено')

    def task_time(self):
        print(f'Времени на выполнение задачи осталось - {self.time}')

    def task_add(self):
        