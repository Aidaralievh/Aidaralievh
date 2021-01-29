class Animal:

    def __init__(self):
        self.jump = 'jump'
        self.run = 'run'
        self.hunt = "hunt"
        print("run jump hunt")

    def __str__(self):
        return f'{self.jump} {self.run} {self.hunt}'


class Cat(Animal):
    pass


class Dog(Animal):
    pass


dog = Dog()
cat = Cat()
print(cat)
print(dog)
