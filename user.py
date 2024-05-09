from dataclasses import dataclass
from datetime import datetime


@dataclass()
class User:
    name: str = 'Viktoras'
    last_name: str = 'Pranckietis'
    password: str = 'NBibibq2919'
    age: int = 20

    def __post_init__(self):
        if self.age < 18:
            raise ValueError("User can not be created younger than 18 years old")


user_viktoras = User(age=19)
print(user_viktoras.name)
print(user_viktoras.password)
print(user_viktoras.last_name)
print([user_viktoras, user_viktoras])


USER_VIKTORAS = {
    'name': 'Viktoras',
    'last_name': 'Pranckietis',
    'password': 'NBibibq2919'
}


class Database:
    def __init__(self):
        self.user: User = user_viktoras

    def connect_to_db(self):
        print(self.user.name)
        print(self.user.last_name)
        print(self.user.password)
        print(self.user.age)


db = Database()
db.connect_to_db()
