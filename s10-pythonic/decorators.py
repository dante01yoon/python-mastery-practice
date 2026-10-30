import time
from contextlib import contextmanager


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__}: {time.perf_counter() - start:.2f}초")
        return result

    return wrapper


@timer
def slow_add(a: int, b: int) -> int:
    time.sleep(0.5)
    return a + b


print(slow_add(2, 3))


@contextmanager
def section(title: str):
    print(f"--- {title} 시작 ---")
    yield
    print(f"--- {title} 끝 ---")


with section("보고서"):
    print("내용을 정리하는 중")
