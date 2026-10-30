import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

NAMES = ["라면", "계란", "국수", "만두"]


def boil(name: str) -> str:
    time.sleep(0.5)
    return f"{name} 다 됐어요"


async def aboil(name: str) -> str:
    await asyncio.sleep(0.5)
    return f"{name} 다 됐어요"


start = time.perf_counter()
for n in NAMES:
    boil(n)
print(f"순서대로: {time.perf_counter() - start:.1f}초")

start = time.perf_counter()
with ThreadPoolExecutor() as pool:
    list(pool.map(boil, NAMES))
print(f"스레드: {time.perf_counter() - start:.1f}초")


async def main() -> None:
    start = time.perf_counter()
    print(await asyncio.gather(*(aboil(n) for n in NAMES)))
    print(f"asyncio: {time.perf_counter() - start:.1f}초")
    try:
        async with asyncio.timeout(0.3):
            await aboil("느린 냄비")
    except TimeoutError:
        print("시간 초과")


asyncio.run(main())

# 2번 답: 스레드가 적을수록 틈에 끼어드는 일이 줄어 1000에 가까워지지만(2개면 200에 가까움),
# 틈은 그대로라 여전히 틀릴 수 있다. 개수를 줄이는 건 해결이 아니고, Lock이 해결이다.
