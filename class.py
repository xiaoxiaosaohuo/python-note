class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def say_hello(self):
        print("Hello, my name is {} and I am {} years old.".format(self.name,self.age))

person = Person("John",36)
person.say_hello()

class Student(Person):
    def __init__(self,name,age,major):
        super().__init__(name,age)
        self.major = major
    def say_hello(self):
        print("Hello, my name is {} and I am {} years old. My major is {}".format(self.name,self.age,self.major))

# private properties and methods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def say_hello(self):
        print("Hello, my name is {} and I am {} years old.".format(
            self.name, self.age))

    def __say_hello(self):
        print("Hello, my name is {} and I am {} years old.".format(
            self.name, self.age))

# abstraction

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

# interface

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)