def shout(text: str) -> str:
    return text.upper()


def whisper(text: str) -> str:
    return text.lower()


say = shout
print(say("hello"))


def apply(func, text: str) -> str:
    return func(text)


print(apply(whisper, "HELLO"))


def make_counter():
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


click = make_counter()
print(click(), click(), click())
