import random

WORDS = ["python", "apple", "music", "tiger"]


def show(word: str, guessed: set) -> str:
    """맞힌 글자만 보이고 나머지는 _로 가린다."""
    shown = ""
    for ch in word:
        if ch in guessed:
            shown += ch + " "
        else:
            shown += "_ "
    return shown


def play(word: str, lives: int = 6) -> None:
    """글자를 하나씩 맞히는 행맨 한 판."""
    guessed = set()
    while lives > 0:
        print(show(word, guessed), f"목숨 {lives}")
        letter = input("글자 하나: ")
        if letter in guessed:
            print("이미 말한 글자예요")
            continue
        guessed.add(letter)
        if letter not in word:
            lives -= 1
        if "_" not in show(word, guessed):
            print(f"정답! {word}")
            return
    print(f"실패... 정답은 {word}")


random.seed(3)
play(random.choice(WORDS))
