import random
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"걸린 시간: {time.perf_counter() - start:.1f}초")
        return result

    return wrapper


def problems(count: int):
    """덧셈·곱셈 문제를 하나씩 만들어 낸다."""
    for _ in range(count):
        a, b = random.randint(2, 9), random.randint(2, 9)
        op = random.choice(["+", "*"])
        answer = a + b if op == "+" else a * b
        yield f"{a} {op} {b}", answer


@timer
def play(count: int = 3) -> list[bool]:
    results = []
    for question, answer in problems(count):
        reply = input(f"{question} = ")
        results.append(reply.strip() == str(answer))
    return results


random.seed(1)
results = play()
correct = sum(results)
print(f"{len(results)}문제 중 {correct}개 정답")
print(["O" if r else "X" for r in results])
