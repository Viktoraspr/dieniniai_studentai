from pandas import DataFrame

class Human:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def do_something(self):
        print(f"Do something {self.x}")
        self.x = 15
        self.y = 25
        print(self.x + self.y)

    @classmethod
    def create_new(cls, x=5, y=10):
        return cls(x, y)


human = Human

print(type(human))

_internal_names: list[str] = set([
    "_mgr",
    "_cacher",
    "_item_cache",
    "_cache",
    "_is_copy",
    "_name",
    "_metadata",
    "_flags",
])


_internal_names_set = {"columns", "index"} | _internal_names

print(_internal_names_set)


