import asyncio
import time


async def download(name: str, seconds: float) -> str:
    await asyncio.sleep(seconds)
    return f"{name} 완료"


async def main() -> None:
    async with asyncio.TaskGroup() as tg:
        a = tg.create_task(download("날씨", 1))
        b = tg.create_task(download("환율", 2))
    print(a.result(), b.result())

    try:
        async with asyncio.timeout(1.5):
            await download("느린 서버", 3)
    except TimeoutError:
        print("1.5초 넘게 걸려서 그만뒀어요")

    sem = asyncio.Semaphore(2)
    start = time.perf_counter()
    names = ["1번", "2번", "3번", "4번"]
    await asyncio.gather(*(limited(sem, n) for n in names))
    print(f"두 개씩 네 개: {time.perf_counter() - start:.1f}초")


async def limited(sem: asyncio.Semaphore, name: str) -> str:
    async with sem:
        print(f"{name} 시작")
        return await download(name, 1)


asyncio.run(main())
