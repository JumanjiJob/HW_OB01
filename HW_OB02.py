class User():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.__level = 'user'

    def info(self):
        print(f"ID - {self.id} ")
        print(f"Имя - {self.name} ")

    def get_level(self):
        print(f"У пользователя с именем {self.name} уровень доступа - {self.__level} ")

class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.__level = 'admin'

    def add_user(self, list_users, user):
        return list_users.append(user.name)

    def remove_user(self, list_users, user):
        return list_users.remove(user.name)

    def get_level(self):
        print(f"У пользователя с именем {self.name} уровень доступа - {self.__level} ")

#Список пользователей
users = []

#Экземпляры класса User
user1 = User(123, "Алексей")
user2 = User(146, "Максим")
user3 = User(795, "Матвей")

#Экземпляр класса Admin
admin1 = Admin(483, "Олег")

#Вывод информации по первому пользователю
user1.info()

#Вывод уровня доступа user
user1.get_level()

#Вывод уровня доступа admin
admin1.get_level()

#Вывод пустого списка
print(users)

#Добавим первого пользователя и выведем на дисплей
admin1.add_user(users, user1)
print(users)

#Добавим второго пользователя и выведем на дисплей
admin1.add_user(users, user2)
print(users)

#Добавим третьего пользователя и выведем на дисплей
admin1.add_user(users, user3)
print(users)

#Удалим первого пользователя и выведем на дисплей
admin1.remove_user(users, user1)
print(users)





