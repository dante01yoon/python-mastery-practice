import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def heavy(n: int) -> int:
    return sum(i * i for i in range(n))


if __name__ == "__main__":
    jobs = [20_000_000] * 4

    start = time.perf_counter()
    for n in jobs:
        heavy(n)
    print(f"순서대로: {time.perf_counter() - start:.1f}초")

    start = time.perf_counter()
    with ThreadPoolExecutor() as pool:
        list(pool.map(heavy, jobs))
    print(f"스레드: {time.perf_counter() - start:.1f}초")

    start = time.perf_counter()
    with ProcessPoolExecutor() as pool:
        list(pool.map(heavy, jobs))
    print(f"프로세스: {time.perf_counter() - start:.1f}초")
