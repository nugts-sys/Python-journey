#user- password data

users = {"James":"pwd123", 
         "Emma":"abc456", 
         "Charles":"xyz789", 
         "Andrew":"lmn111", 
         "Courtney":"rst222"}

username = input("Please enter your username: ")

if username in users:
    password = input("Please enter your password now: ")

    if password == users[username]:
        print("login successful")


    else:
        print("Password incorrect")



else:
    print("username not found")
    
