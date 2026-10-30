from dataclasses import dataclass


@dataclass
class Item:
    name: str
    price: int
    qty: int

    @property
    def total(self) -> int:
        return self.price * self.qty


item = Item("연필", 500, 3)
print(item)
print(item.total)
