import time
from contextlib import contextmanager


def count_calls(func):
    calls = 0

    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        print(f"{func.__name__} {calls}번째 호출")
        return func(*args, **kwargs)

    return wrapper


@count_calls
def hello() -> None:
    print("안녕")


hello()
hello()


@contextmanager
def timer_block(name: str):
    start = time.perf_counter()
    yield
    print(f"{name}: {time.perf_counter() - start:.2f}초")


with timer_block("정리"):
    time.sleep(0.3)
