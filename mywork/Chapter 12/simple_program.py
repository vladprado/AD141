def sum_args(*args):
    total = 0
    for value in args:
        total += value
    return total


def main():
    a = 5
    b = 3
    result = sum_args(a, b)
    print(result)