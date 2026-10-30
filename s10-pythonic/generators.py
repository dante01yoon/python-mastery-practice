nums = [10, 20, 30]
it = iter(nums)
print(next(it))
print(next(it))


def countdown(n: int):
    while n > 0:
        yield n
        n -= 1


for x in countdown(3):
    print(x)

gen = countdown(2)
print(next(gen), next(gen))

total = sum(n * n for n in range(1, 1_000_001))
print(total)
