#!/usr/bin/env python3

class Plant:

    _height: float | None
    _age: int | None

    def __init__(self, name: str, height: float, age: int,
                 growth_speed: float) -> None:
        self.set_name(name)
        self._height = None
        self.set_height(height)
        self._age = None
        self.set_age(age)
        self._growth_speed = growth_speed
        print("Plant created: ", end="")
        self.show()

    def set_name(self, name: str) -> None:
        self._name = name

    def set_height(self, height: float) -> None:
        if self._height is None:
            if height >= 0:
                self._height = height
            else:
                print("Error, height can't be negative")
                print("Height was set to 0")
                self._height = 0
            self._height = height
        else:
            if height >= 0:
                self._height = height
                print(f"Height updated: {self._height}cm")
            else:
                print(f"{self._name}: Error, height can't be negative")
                print("Height update rejected")

    def set_age(self, age: int) -> None:
        if self._age is None:
            if age >= 0:
                self._age = age
            else:
                print("Error, age can't be negative")
                print("Age was set to 0")
                self._age = 0
            self._age = age
        else:
            if age >= 0:
                self._age = age
                print(f"Age updated: {self._age} days")
            else:
                print(f"{self._name}: Error, age can't be negative")
                print("Age update rejected")

    def get_name(self) -> str:
        return (self._name)

    def get_height(self) -> float | None:
        return (self._height)

    def get_age(self) -> int | None:
        return (self._age)

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def age(self, days: int) -> None:
        if self._age is not None:
            self._age = self._age + days

    def grow(self, time: int) -> None:
        print("=== Garden Plant Growth ===")
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        for i in range(time):
            self.age(1)
            if self._height is not None:
                self._height = round(self._height + self._growth_speed, 2)
            print(f"=== Day {i + 1} ===")
            print(f"{self._name}: {self._height}cm, {self._age} days old")
        print(f"Growth this week: {round(self._growth_speed * time, 2)}cm")


if __name__ == "__main__":

    print("=== Garden Security System ===")

    monstera = Plant("Monstera deliciosa", 30, 123, 0.2)
    print("")

    monstera.set_height(40)
    monstera.set_age(142)
    print("")

    monstera.set_height(-40)
    monstera.set_age(-142)
    print("")

    print(f"Current state: {monstera.get_name()}: "
          f"{monstera.get_height():.1f}cm, {monstera.get_age()} days old")

    # arecaceae = Plant("Arecacea", 500, 748, 1.5)

    # erythrina = Plant("Mulungu-do-litoral", 201, 1021, 0.9)

    # ipe = Plant("Handroanthus", 5, 1857, 1.3)

    # fly = Plant("Dionaea", 3, 666, 0.05)
