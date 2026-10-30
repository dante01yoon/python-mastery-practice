files = ["a.txt", "b.xlsx", "c.txt"]
print([f.upper() for f in files if f.endswith(".txt")])


def evens(n: int):
    for i in range(2, n + 1, 2):
        yield i


print(list(evens(10)))


def double(x: int) -> int:
    return x * 2


def square(x: int) -> int:
    return x * x


for func in [double, square]:
    print(func.__name__, func(7))
