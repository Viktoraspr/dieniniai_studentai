"""
Sukuriam klasę žmogus (Human), kuris turi:
- varda
- pavarde
- gimimo dieną;
Turi metodus:
- apskaičiuoti šios dienos amžių dienomis arba valandomis

Sukurti klasę studentas, kuris paveldėtų Human klasės savybės ir turėtų papildomą atributą
- mokuosi nuo,

Turi metodą, kuris apsiskaičiuotų kiek laiko žmogus mokosi (dienomis, arba valandomis)
Turi metoda, kuris paskaičiuotų kokia dalį savo gyvenimo jis mokosi (procentais)
"""

from datetime import datetime, timedelta

data = datetime(year=2015, month=3, day=5)
new_data = timedelta(days=90)
print(data, type(data))
print(new_data, type(new_data))


# print(data - 5)
r"""
Traceback (most recent call last):
  File "C:\Users\vpranck\Desktop\Paskaita\dieniniai\dienos_skaiciavimas.py", line 24, in <module>
    print(data - 5)
          ~~~~~^~~
TypeError: unsupported operand type(s) for -: 'datetime.datetime' and 'int'

Traceback (most recent call last):
  File "C:\Users\vpranck\Desktop\Paskaita\dieniniai\dienos_skaiciavimas.py", line 35, in <module>
    print(number-number_1)
          ~~~~~~^~~~~~~~~
TypeError: unsupported operand type(s) for -: 'int' and 'str'
"""
number = 5
number_1 = '5'

print(number-number_1)


# class Person:
#     def __init__(self, name: str, last_name: str, birthday: datetime):
#         self.name = name
#         self.last_name = last_name
#         self.birthday = birthday
#         self.new_variable = None
#
#     @staticmethod
#     def _get_days(since_when) -> int:
#         return (datetime.now() - since_when).days + 1
#
#     @staticmethod
#     def _get_hours(since_when) -> int:
#         now_hour = datetime.now().hour
#         return (datetime.now() - since_when).days * 24 + now_hour
#
#     def get_time_since_birthday(self, days: bool = True):
#         value = self.birthday
#         if days:
#             return self._get_days(value)
#         return self._get_hours(value)
#
#
# class Student(Person):
#     def __init__(self, name, last_name, birthday, study_start):
#         super().__init__(name, last_name, birthday)
#         self.study_start = study_start
#
#     def get_study_time(self, days: bool = True) -> int:
#         value = self.study_start
#         if days:
#             return self._get_days(value)
#         return self._get_hours(value)
#
#     def get_learning_percentage_time(self):
#         living_days = self.get_time_since_birthday()
#         study_days = self.get_study_time()
#         return round(study_days/living_days * 100, 0)
#
#
# student = Student(
#     name='Albinas',
#     last_name='Morka',
#     birthday=datetime(year=1999, month=3, day=17),
#     study_start=datetime(year=2019, month=5, day=1),
# )
#
# print(student.get_time_since_birthday())
# print(student.get_time_since_birthday(days=False))
#
# print(student.get_study_time())
# print(student.get_study_time(days=False))
#
# print(student.get_learning_percentage_time())
#
