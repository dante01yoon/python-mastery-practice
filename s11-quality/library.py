from typing import Literal, TypedDict


class Book(TypedDict):
    title: str
    price: int
    status: Literal["대여 가능", "대여 중"]


def label(book: Book) -> str:
    return f"{book['title']} · {book['price']:,}원 · {book['status']}"


book: Book = {"title": "파이썬 입문", "price": 18000, "status": "대여 가능"}
print(label(book))
