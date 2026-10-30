import asyncio
import time


async def download(name: str) -> str:
    await asyncio.sleep(1)
    return f"{name} 완료"


async def main() -> None:
    start = time.perf_counter()
    results = await asyncio.gather(download("날씨"), download("환율"), download("뉴스"))
    print(results)
    print(f"gather: {time.perf_counter() - start:.1f}초")


asyncio.run(main())
