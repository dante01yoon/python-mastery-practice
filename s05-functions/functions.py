def greet(name):
    print(f"안녕하세요, {name}님!")


greet("민지")
greet("지훈")


def add(a, b):
    return a + b


total = add(3, 4)
print(total)
print(add(10, 20) * 2)


def add_print(a, b):
    print(a + b)


result = add_print(1, 2)
print(result)
