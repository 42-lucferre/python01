#!/usr/bin/env python3

class Plant:

    def set_name(self, name: str) -> None:
        self.name = name

    def set_height(self, height: int) -> None:
        self.height = height

    def set_age(self, age: int) -> None:
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":

    print("=== Garden Plant Registry ===")

    samambaia = Plant()
    samambaia.set_name("Monstera deliciosa")
    samambaia.set_height(30)
    samambaia.set_age(123)

    arecaceae = Plant()
    arecaceae.set_name("Arecacea")
    arecaceae.set_height(500)
    arecaceae.set_age(748)

    mulungu = Plant()
    mulungu.set_name("Mulungu-do-litoral")
    mulungu.set_height(201)
    mulungu.set_age(1021)

    samambaia.show()
    arecaceae.show()
    mulungu.show()
