count = 0


def add_one():
    count = 1
    print("안에서:", count)


add_one()
print("밖에서:", count)

fruits = ["파인애플", "귤", "바나나", "키위"]
print(sorted(fruits))
print(sorted(fruits, key=lambda f: len(f)))


def countdown(n):
    if n == 0:
        print("발사!")
        return
    print(n)
    countdown(n - 1)


countdown(3)
