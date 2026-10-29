def order(drink, size="톨"):
    print(f"{drink} {size} 사이즈 주문")


order("라떼")
order("라떼", "그란데")
order(size="벤티", drink="아메리카노")


def total(*prices):
    return sum(prices)


print(total(1000, 2500, 300))


def profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")


profile(name="지훈", city="서울")


def area(width: float, height: float) -> float:
    """직사각형의 넓이를 돌려준다."""
    return width * height


print(area(3, 4.5))
