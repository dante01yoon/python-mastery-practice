from abc import ABC, abstractmethod


class Circle:
    def __init__(self, r: float) -> None:
        self.r = r

    def area(self) -> float:
        return 3.14 * self.r ** 2


class Square:
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side ** 2


for shape in [Circle(1), Square(2)]:
    print(type(shape).__name__, shape.area())


class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...


class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height


try:
    Triangle(3, 4)
except TypeError as e:
    print("오류:", e)


class Rect(Shape):
    def __init__(self, w: float, h: float) -> None:
        self.w = w
        self.h = h

    def area(self) -> float:
        return self.w * self.h


print(Rect(2, 3).area())
