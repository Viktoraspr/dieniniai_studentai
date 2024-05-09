
TEXT = """
    Budget Program
1. Enter Income
2. Enter Expenses
3. Show Balance
4. Show Report
5. Quit Finance manager
"""


def print_1():
    print('Cia yra 1 funkcja')


def print_2():
    print('Cia yra 2 funkcja')


def print_3():
    print('Cia yra 3 funkcja')


commands_map = {
    1: print_1,
    2: print_2,
    3: print_3,
}


value = int(input('Ivesk skaiciu: '))
commands_map[value]()
