from dataclasses import dataclass


@dataclass
class Item:
    name: str
    price: int
    qty: int

    @property
    def total(self) -> int:
        return self.price * self.qty


item = Item("공책", 1500, 3)
print(item, item.total)
