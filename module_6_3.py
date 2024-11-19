# Множественное наследование
from random import randint


class Animal:

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def move(self, dx, dy, dz):
        new_cords = [dx, dy, dz]
        i = 0
        for i in range(3):
            self._cords[i] += new_cords[i] * self.speed

        if self._cords[2] < 0:
            self._cords[2] = 0
            print("It's too deep, i can't dive :(")

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f"Here are(is) {randint(1, 4)} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] -= abs(dz) * (self.speed / 2)


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = "Click-click-click"

    def speak(self):
        print(self.sound)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
