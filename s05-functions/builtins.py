names = ["민지", "준호", "서연"]
scores = [90, 75, 88]

for i, name in enumerate(names, start=1):
    print(i, name)

for name, score in zip(names, scores):
    print(name, score)

pairs = list(zip(names, scores))
print(sorted(scores))
print(sorted(pairs, key=lambda p: p[1], reverse=True))

doubled = list(map(lambda s: s * 2, scores))
passed = list(filter(lambda s: s >= 80, scores))
print(doubled, passed)
flags = list(map(lambda s: s >= 80, scores))
print(any(flags), all(flags))
