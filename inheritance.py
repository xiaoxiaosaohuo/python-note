# single

class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print('Animal is eating....')

class Dog(Animal):
    def bark(self):
        print('dog is barking...')


d = Dog('Tom')
print(d.name)
d.eat()
d.bark()

# multiple

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("Animal is eating...")


class Flyable:
    def fly(self):
        print("I can fly...")


class Bird(Animal, Flyable):
    def chirp(self):
        print("Bird is chirping...")


b = Bird("Sparrow")
print(b.name)  # 输出 Sparrow
b.eat()  # 输出 Animal is eating...
b.fly()  # 输出 I can fly...
b.chirp()  # 输出 Bird is chirping...


# multiple level

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("Animal is eating...")


class Mammal(Animal):
    def run(self):
        print(self.name,"Mammal is running...")


class Dog(Mammal):
    def bark(self):
        print("Dog is barking...")


d = Dog("Tom")
print(d.name)  # 输出 Tom
d.eat()  # 输出 Animal is eating...
d.run()  # 输出 Mammal is running...
d.bark()  # 输出 Dog is barking...
