#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str, height: float, age: int,
                 growth_speed: float) -> None:
        self.set_name(name)
        self.set_height(height)
        self.set_age(age)
        self.growth_speed = growth_speed
        print("Created: ", end="")
        self.show()

    def set_name(self, name: str) -> None:
        self.name = name

    def set_height(self, height: float) -> None:
        self.height = height

    def set_age(self, age: int) -> None:
        self.age_a = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age_a} days old")

    def age(self, days: int) -> None:
        self.age_a = self.age_a + days

    def grow(self, time: int) -> None:
        print("=== Garden Plant Growth ===")
        print(f"{self.name}: {self.height}cm, {self.age_a} days old")
        for i in range(time):
            self.age(1)
            self.height = round(self.height + self.growth_speed, 2)
            print(f"=== Day {i + 1} ===")
            print(f"{self.name}: {self.height}cm, {self.age_a} days old")
        print(f"Growth this week: {round(self.growth_speed * time, 2)}cm")


if __name__ == "__main__":

    print("=== Plant Factory Output ===")

    monstera = Plant("Monstera deliciosa", 30, 123, 0.2)

    arecaceae = Plant("Arecacea", 500, 748, 1.5)

    erythrina = Plant("Mulungu-do-litoral", 201, 1021, 0.9)

    ipe = Plant("Handroanthus", 5, 1857, 1.3)

    fly = Plant("Dionaea", 3, 666, 0.05)
