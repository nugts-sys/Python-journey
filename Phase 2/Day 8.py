# with open("notes.txt", "w") as f:
#     f.write("Hello, this is my second file!")

# with open("notes.txt", "a") as f:
#     f.write("\nThis is a new line, appended!").     #all of this here was just copied from claude it was to understand scripting and dumps(loads)

#     import json

# data = {"name": "Jonas", "grade": 2}

# with open("data.json", "w") as f:
#     json.dump(data, f)

#FIRST OWN PROJECT:


import json


expenses = [{"item": "coffee", "amount": 3, "cost": 9}, {"item": "socks", "amount": 2, "cost": 10}]

with open("expenses.json", "w") as f:
    json.dump(expenses, f)

with open("expenses.json", "r") as f:
    loaded_data = json.load (f)

for expense in loaded_data:
    print(f"of:{expense["item"]} you need: {expense["amount"]}, which will cost: {expense["cost"]}$")