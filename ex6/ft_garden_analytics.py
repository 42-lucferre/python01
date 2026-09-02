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
            print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")
        print(f"Growth this week: {round(self._growth_speed * time, 2)}cm")

    @staticmethod
    def check_age(age: int) -> None:
        print(f"Is {age} days more than a year? -> ", end="")
        if age > 365:
            print("True")
        else:
            print("False")

    @classmethod
    def anonymous(cls) -> "Plant":
        return (cls("Unknown plant", 0, 0, 0))


class Flower(Plant):

    def __init__(self, name: str, height: float, age: int,
                 growth_speed: float, color: str) -> None:
        print("=== Flower")
        self.set_color(color)
        self._bloom = 0
        super().__init__(name, height, age, growth_speed)

    def set_color(self, color: str) -> None:
        self._color = color

    def get_color(self) -> str:
        return (self._color)

    def bloom(self) -> None:
        print(f"[asking the {self._name} to bloom]")
        self._bloom = 1

    def show(self) -> None:
        super().show()
        print(f" Color: {self.get_color()}")
        if self._bloom == 0:
            print(f" {self.get_name()} has not bloomed yet")
        else:
            print(f" {self.get_name()} is blooming beautifully!")


class Tree(Plant):

    def __init__(self, name: str, height: float, age: int,
                 growth_speed: float, trunk_diameter: float) -> None:
        print("=== Tree")
        self.set_trunk_diameter(trunk_diameter)
        super().__init__(name, height, age, growth_speed)

    def set_trunk_diameter(self, trunk_diameter: float) -> None:
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree {self._name} now produces a shade of {self._height:.1f}"
              f"cm long and {self._trunk_diameter:.1f} wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):

    def __init__(self, name: str, height: float, age: int,
                 growth_speed: float, harvest_season: str,
                 nutritional_value: int) -> None:
        print("=== Vegetable")
        self._harvest_season = harvest_season
        self.set_nutritional_value(nutritional_value)
        super().__init__(name, height, age, growth_speed)

    def set_nutritional_value(self, nutritional_value: int) -> None:
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

    def grow(self, days: int) -> None:
        print(f"[make {self._name} grow and age for {days} days]")
        if self._height is not None:
            self._height = self._height + (self._growth_speed * days)
        self.age(days)
        self._nutritional_value += days


if __name__ == "__main__":

    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check_age(30)
    Plant.check_age(400)

    print("")

    hibiscus = Flower("Hibiscus striatus", 60, 333, 0.2, "pink")
    hibiscus.bloom()
    hibiscus.show()

    print("")

    arecaceae = Tree("Arecacea", 500, 748, 1.5, 5)
    arecaceae.produce_shade()

    print("")

    brassica = Vegetable("Brassica oleracea", 3, 45, 0.2, "winter", 0)
    brassica.grow(20)
    brassica.show()

    print("")

    print("=== Anonymous")
    unk = Plant.anonymous()

    # erythrina = Plant("Mulungu-do-litoral", 201, 1021, 0.9)

    # ipe = Plant("Handroanthus", 5, 1857, 1.3)

    # fly = Plant("Dionaea", 3, 666, 0.05)
