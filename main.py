"""
For learning reason

Another try

Added let's try.
"""

def print_string(x, y):
    for number in range(x, y+1):
        print(str(number) * number)


def print_reverse(number):
    print(' '.join(str(number)[::-1]))


def print_calculation():
    for m in range(1, 11):
        for n in range(1, 11):
            print(m * n, end=' ')
        print()


def return_something(data, deleted_key, nessesary):
    result_nessesary = {value: data[value] for value in nessesary}
    for key in deleted_key:
        del data[key]
    return result_nessesary, data


values = {
    1: 'vienas',
    2: 'du',
    3: 'trys',
    4: 'keturi',
}

deleted_key = [3]
nessesary = [1, 2]

print(return_something(data=values, deleted_key=deleted_key, nessesary=nessesary))
