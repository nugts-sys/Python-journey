#try and except to not make code crash if a user input is not compatible with the code

try:
    x = int(input("enter any number: "))
    print(10 / x)

except ValueError:
    print("oops, that is not a valid number: ")

except ZeroDivisionError:
    print("Can't divide by zero!")