import string

LETTERS = string.ascii_lowercase


def encrypt(text: str, shift: int) -> str:
    """알파벳을 shift만큼 뒤로 민다. 알파벳이 아닌 글자는 그대로."""
    result = ""
    for ch in text.lower():
        if ch in LETTERS:
            result += LETTERS[(LETTERS.index(ch) + shift) % 26]
        else:
            result += ch
    return result


def decrypt(text: str, shift: int) -> str:
    return encrypt(text, -shift)
