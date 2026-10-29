def average(scores):
    return sum(scores) / len(scores)


def report(name, scores):
    print(f"{name} 평균: {average(scores)}")


report("민지", [80, 90, 100])
report("지훈", [])
