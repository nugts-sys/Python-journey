#loops again to understand better

# for x in range(1, 21):
#     if x % 3 == 0:
#         print(f"{x} is able to be divided by 3 without remain")

    
#Dictionaries and sets day 3:


translation = {"Teller":"Plate", 
                "Bildschirm":"Screen", 
                "Maus":"Mouse", 
                "Baum":"Tree", 
                "Flasche":"Bottle"}

german_words = ["Teller", "Bildschirm", "Maus", "Baum", "Flasche"]

print(german_words)

deutsch = input("Which of these german words do you want to translate to english? ")

print(translation.get(deutsch))
