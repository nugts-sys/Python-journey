import requests #still no idea why this is underlined yellow but worked anyways

api_data = requests.get("https://jsonplaceholder.typicode.com/todos/1") #get the api data and save it in a variable
data = api_data.json() #make the api data a json and save the converted one in a new variable
print(data)             #print the json data fully
print(data["title"])    #print only a selected part of the data which here is the title