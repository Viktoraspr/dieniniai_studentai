from random import choice


def do_something():
    x = 115
    y = 18
    return x + y


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__data = [1, 2, 3, 4]

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'Objektas x={self.x}, y={self.y}'

    def __repr__(self):
        return f'Objektas repr x={self.x}, y={self.y}'

    def __len__(self):
        return len(self.__data)

    def __getitem__(self, item):
        return self.__data[item]

    def generate_random_value(self):
        return choice(self.__data)

    def add_data_value(self):
        pass

    @staticmethod
    def do_something():
        print('do something')

    @staticmethod
    def calculate_constant():
        return 2

    def calculate_something(self):
        return self.x + self.y + self.calculate_constant()


point_a = Point(2, 5)
point_b = Point(2, 5)
point_a.do_something()
Point.do_something()


print(len(point_a))
print(choice(point_a))
print(choice(point_a))
print(choice(point_a))
print(choice(point_a))
print(choice(point_a))
print(choice(point_a))
print(point_a.generate_random_value())
print(point_a.generate_random_value())
print(point_a.generate_random_value())
print(point_a.generate_random_value())
print(point_a.generate_random_value())

print(point_a == point_b)
print(point_b > point_a)
print(point_b + point_a)
point_3 = point_b + point_a


print(point_3)
print(point_3.x)

new_data = (1, 2, 3)
new_data_2 = (1, 1, 30)

print(new_data > new_data_2)
