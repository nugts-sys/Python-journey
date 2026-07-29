class Animal2:
    def __init__ (self, animal, name, age):
        self.animal = animal
        self.name = name
        self.age = age

    def is_baby(self):
        if self.age <= 2:
            return True

        else:
            return False

animal_1 = Animal2("Lion", "Bob", 2)
animal_2 = Animal2("Eagle", "Scar", 9)

print(animal_1.is_baby())
print(animal_2.is_baby())
