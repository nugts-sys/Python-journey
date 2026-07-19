#Numbers from 1-100 using for- loop.

#credit_card = "1234-5678-9012-345-678"

#for x in credit_card:
    #print(x)
#print("This is your cc- number if you forgot it!")

for x in range(1, 51):                  #range of the whole interval that i wanna check
    if x > 1:                           #if x is greater than 1 do for loop

        for t in range(2, x):           #range of numbers to divide every number of the first range with
            if x%t == 0:                #if the rest of x divided by any number other than 1 and itself is 0 its a prime
                break                   #stop if you land on a prime
        
        else:                           #print prime when stopped at one
            print(x)                    


