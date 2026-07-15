from abc import ABC, abstractmethod

class animal(ABC):
    def sound(self):
        print("Animal sound")

class dog(animal):
    def sound(self):
        print("bark")

class cat(dog):
    def sound(self):
        print("Meow")

ob = cat()
ob.sound()