import json

finance = [{"item": "coffee", "amount": 3}, {"item": "Book", "amount":15}]

with open("finance.json", "w") as f:
    json.dump(finance, f)

with open("finance.json", "r") as f:
    loaded_finance = json.load(f)

print(loaded_finance)

for entry in loaded_finance:
    print(f"{entry["item"]}: {entry["amount"]}$")