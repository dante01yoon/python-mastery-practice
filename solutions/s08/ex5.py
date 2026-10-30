# s08-modules 폴더에서: uv run ../solutions/s08/ex5.py 가 아니라, 이 함수를 cipher/caesar.py에 붙여 넣고 실행
import string

LETTERS = string.ascii_lowercase


def encrypt(text: str, shift: int) -> str:
    return "".join(LETTERS[(LETTERS.index(c) + shift) % 26] if c in LETTERS else c for c in text.lower())


def brute_force(text: str) -> None:
    for shift in range(1, 26):
        print(shift, encrypt(text, -shift))


brute_force("phhw ph dw qrrq")
