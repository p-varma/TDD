from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        print("This is abstract class")
        pass


class Human(Animal):
    def move(self):
        print("I can walk and run")


class Snake(Animal):
    def move(self):
        super().move()
        print("I can crawl")


class Dog(Animal):
    def move(self):
        print("I can bark")


class Lion(Animal):
    def move(self):
        print("I can roar")

h = Human()
s = Snake()

#c = Animal()