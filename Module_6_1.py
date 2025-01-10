class Animal:

    def __init__(self, name, alive=True, fed=False):
        self.name = name
        self.alive = alive
        self.fed = fed

    def eat(self, food):
        self.food = food
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Plant:

    def __init__(self, name, edible=False):
        self.name = name
        self.edible = edible


class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):

    def __init__(self, name, edible=True):
        super().__init__(name, edible)
        self.edible = edible


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')

p1 = Flower('Цветик Семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a2.name)
print(p2.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)
