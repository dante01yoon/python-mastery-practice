class Student:
    count = 0

    def __init__(self, name: str) -> None:
        self.name = name
        Student.count += 1


a = Student("민지")
b = Student("준호")
print(Student.count, a.count, a.name, b.name)


class Temperature:
    def __init__(self, celsius: float) -> None:
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, f: float) -> "Temperature":
        return cls((f - 32) * 5 / 9)

    @staticmethod
    def is_freezing(celsius: float) -> bool:
        return celsius <= 0


t = Temperature.from_fahrenheit(212)
print(t.celsius)
print(Temperature.is_freezing(-3))
