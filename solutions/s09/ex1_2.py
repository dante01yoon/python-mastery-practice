class Book:
    def __init__(self, title: str, pages: int):
        self.title = title
        self.pages = pages

    def summary(self) -> str:
        return f"{self.title} ({self.pages}쪽)"

    def __str__(self) -> str:
        return self.summary()


book = Book("파이썬 완전정복", 320)
print(book.summary())
print(book)
