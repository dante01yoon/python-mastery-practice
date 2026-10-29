# 연습용: 비밀번호를 암호화하지 않고 그대로 저장한다. 실제 비밀번호는 넣지 말 것.
import json
import random
from pathlib import Path

VAULT = Path("vault.json")
CHARS = "abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789"


def load() -> dict:
    """저장 파일을 읽는다. 없거나 깨졌으면 빈 딕셔너리."""
    try:
        return json.loads(VAULT.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("저장 파일이 깨져 있어 새로 시작해요")
        return {}


def save(data: dict) -> None:
    VAULT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def make_password(length: int = 12) -> str:
    return "".join(random.choice(CHARS) for _ in range(length))


data = load()
while True:
    menu = input("1 추가  2 찾기  3 목록  4 끝: ")
    if menu == "1":
        site = input("사이트: ")
        password = make_password()
        data[site] = password
        save(data)
        print(f"{site} 비밀번호를 만들어 저장했어요: {password}")
    elif menu == "2":
        site = input("사이트: ")
        if site in data:
            print(f"{site}: {data[site]}")
        else:
            print("저장된 사이트가 아니에요")
    elif menu == "3":
        for site in data:
            print("-", site)
    elif menu == "4":
        break
