
def get_valid_amount():
   
    try:
        amount = int(input("you can add the amount of your choice: "))
    except ValueError:
        amount = -1

    while amount <= 0:
        try:
            amount = int(input("you can add the amount of your choice: "))
        except ValueError:
            amount = -1

    return amount

result = get_valid_amount()
print(f"you entered: {result}")