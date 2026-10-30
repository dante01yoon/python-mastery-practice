from typing import Literal, TypedDict


class Order(TypedDict):
    item: str
    qty: int
    status: Literal["주문", "배송 중", "완료"]


order: Order = {"item": "키보드", "qty": 2, "status": "주문"}
# order["status"] = "취소"  ← mypy: incompatible type "Literal['취소']"
order["status"] = "배송 중"
print(f"{order['item']} {order['qty']}개 · {order['status']}")
