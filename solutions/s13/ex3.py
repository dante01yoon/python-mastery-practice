import time
from concurrent.futures import ProcessPoolExecutor


def count_primes(n: int) -> int:
    count = 0
    for k in range(2, n + 1):
        if all(k % d for d in range(2, int(k**0.5) + 1)):
            count += 1
    return count


if __name__ == "__main__":
    jobs = [200_000] * 4

    start = time.perf_counter()
    print([count_primes(n) for n in jobs])
    print(f"순서대로: {time.perf_counter() - start:.1f}초")

    start = time.perf_counter()
    with ProcessPoolExecutor() as pool:
        print(list(pool.map(count_primes, jobs)))
    print(f"프로세스: {time.perf_counter() - start:.1f}초")
