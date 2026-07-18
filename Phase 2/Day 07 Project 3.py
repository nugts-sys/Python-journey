#this is just cause im so unsure when it comes to classes i just wanna do one more exercise today

class Animal:
    def __init__ (self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.sound} says the {self.name}!"
    
    
class Dog(Animal):
    pass

class Cat(Animal):
    pass

animal_1 = Dog("Dog", "WOOF")
animal_2 = Cat("Cat", "MEOW")

print(animal_1.make_sound())
print(animal_2.make_sound())