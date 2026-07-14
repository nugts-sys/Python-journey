#project 2 of day 7 going on to connecting classes amongst eachother

class Vehicle:
    def __init__ (self, brand, speed):
        self.brand = brand
        self.speed = speed
    
    def describe(self):
        return f"{self.brand}, top speed {self.speed} km/h"
    
class Car(Vehicle):

    def __init__ (self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors

    def describe(self):
        return f"{self.brand}, top speed {self.speed} km/h it has {self.doors} doors"

class Motorcycle(Vehicle):
    pass


car_1 = Car("BMW", 250, 4)
moto_1 = Motorcycle("Kawasaki", 310)

print(moto_1.describe())