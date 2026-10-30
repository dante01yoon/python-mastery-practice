"""글자를 다루는 작은 도구 모음."""


def count_words(text: str) -> int:
    """띄어쓰기로 나눈 단어 수."""
    return len(text.split())


def shout(text: str) -> str:
    return text.upper() + "!"


if __name__ == "__main__":
    print(count_words("오늘 회의는 세 시"))
    print(shout("hello"))
