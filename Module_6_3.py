import random

class Animal:

    live = True
    Sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self.speed = speed
        self._cords = [0, 0, 0]

    def move(self, dx, dy, dz):
        dx1 = self._cords[0] + dx * self.speed
        dy1 = self._cords[1] + dy * self.speed
        dz1 = self._cords[2] + dz * self.speed
        if dz1 < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords = [dx1, dy1, dz1]

    def get_cords(self):
         print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful")
        else:
            print("Be careful, I'm attacking you 0_0")

    def speak(self):
        print(f"{self.Sound}")


class Bird(Animal):

    beak = True

    def lay_eggs(self):
        print(f"Here is(are) {random.randint(1, 4)} egg(s) for you")


class AquaticAnimal(Animal):

    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self.dz2 = self._cords[2]  - abs(dz)  * (self.speed/2)
        self._cords[2] = max(self.dz2, 0)


class PoisonousAnimal(Animal):

    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):

    Sound = "Click-click-click"


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