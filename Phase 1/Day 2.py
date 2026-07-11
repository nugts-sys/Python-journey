#Einkaufsliste Übung zu listen 1

# shop_list = ["milk", "bread", "orange", "eggs", "flower"]

# print("Hello, what do like to change about your shopping list?")
# print(shop_list)



# new_item = input("Type in the items you want to add here first: ")
# shop_list.append(new_item)

# remove_item = input("Now type in whatever item you want to remove from your list: ")
# shop_list.remove(remove_item)



# print(shop_list)




#Übung zwei Notenverwaltung liste 2

noten = [2, 4, 3, 1, 6, 2, 1, 5, 6, 3, 2, 4 ,5]

# schlechteste = noten[0]
# print(schlechteste)

# for note in noten:
#     if note > schlechteste:
#         schlechteste = note


# print(schlechteste)


# beste = noten[0]
# print(beste)

# for note in noten:
#     if note < beste:
#         beste = note

# print(beste)

# print(max(noten))
# print(min(noten))

# print(noten[10:13])
# print(noten[0:3])
# print(noten[::2])

for x in range(1, 11):
    if x % 2 == 0:
        print(f"{x} is even")
    
    else:
        print(f"{x} is not even")
