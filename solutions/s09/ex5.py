class Book:
    count = 0

    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
        Book.count += 1

    @classmethod
    def from_text(cls, text: str) -> "Book":
        title, author = text.split("/")
        return cls(title, author)


b = Book.from_text("데미안/헤세")
print(b.title, b.author, Book.count)
