names = ["민지", "준호", "서연"]
ages = [29, 34, 21]
for name, age in sorted(zip(names, ages), key=lambda p: p[1]):
    print(name, age)
