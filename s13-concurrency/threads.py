import threading
import time
from concurrent.futures import ThreadPoolExecutor


def download(name: str) -> str:
    time.sleep(1)
    return f"{name} 완료"


names = ["날씨", "환율", "뉴스"]
start = time.perf_counter()
workers = [threading.Thread(target=download, args=(n,)) for n in names]
for w in workers:
    w.start()
for w in workers:
    w.join()
print(f"스레드 세 개: {time.perf_counter() - start:.1f}초")

start = time.perf_counter()
with ThreadPoolExecutor(max_workers=3) as pool:
    for result in pool.map(download, names):
        print(result)
print(f"스레드 풀: {time.perf_counter() - start:.1f}초")
