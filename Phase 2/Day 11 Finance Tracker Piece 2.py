counter = 0

Interactions = {1:"count up",
                2:"count down",
                3:"reset counter",
                4:"exit"}

print(Interactions)


while True:

    interaction = int(input("which action do you want to do?: "))

    if interaction in Interactions:
        if interaction == 1:
            counter += 1
            print(counter)

    
        elif interaction == 2:
            counter -= 1
            print(counter)

    
        elif interaction == 3:
            counter = 0
            print(counter)


        elif interaction == 4:
            break
    else:
        print("error, invalid iption.")


