from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self) -> str: ...


class Dog(Animal):
    def speak(self) -> str:
        return "멍멍"


class Cat(Animal):
    def speak(self) -> str:
        return "야옹"


for animal in [Dog(), Cat()]:
    print(type(animal).__name__, animal.speak())
