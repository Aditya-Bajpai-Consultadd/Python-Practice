#Create a class with private attributes for sensitive data (e.g., user
#passwords) and methods for secure access and modification.

class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password


user = User("admin", "admin")
print(user.get_username())
print(user.get_password())
user.set_username("admin2")
user.set_password("admin2")
print(user.get_username())
print(user.get_password())
