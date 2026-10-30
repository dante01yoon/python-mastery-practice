import time


def download(name: str) -> str:
    time.sleep(1)
    return f"{name} 완료"


start = time.perf_counter()
for name in ["날씨", "환율", "뉴스"]:
    print(download(name))
print(f"걸린 시간: {time.perf_counter() - start:.1f}초")
