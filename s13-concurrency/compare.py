import asyncio
import time
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor

SITES = {"날씨": 0.8, "환율": 0.5, "뉴스": 1.0, "지도": 0.7, "주식": 0.6}


def fetch(name: str) -> str:
    time.sleep(SITES[name])
    return name


async def afetch(name: str) -> str:
    await asyncio.sleep(SITES[name])
    return name


def one_by_one() -> None:
    for name in SITES:
        fetch(name)


def with_threads() -> None:
    with ThreadPoolExecutor() as pool:
        list(pool.map(fetch, SITES))


def with_asyncio() -> None:
    async def main() -> None:
        await asyncio.gather(*(afetch(n) for n in SITES))

    asyncio.run(main())


def timed(label: str, work: Callable[[], None]) -> None:
    start = time.perf_counter()
    work()
    seconds = time.perf_counter() - start
    print(f"{seconds:.1f}초 " + "■" * round(seconds * 10) + f" {label}")


for label, work in [
    ("순서대로", one_by_one),
    ("스레드", with_threads),
    ("asyncio", with_asyncio),
]:
    timed(label, work)
