grades = [1, 4, 3, 5, 2, 3, 3, 2, 4, 5, 5]
print(grades)

print("These are all the grades for the end of this year.")
print("You interact with this list in the following ways: ")

interactions = {1:"add grade", 
                2:"show average grade",
                3:"display all grades", 
                4:"exit"}
print(interactions)

while True:

    user_input = int(input("which one of these actions do you wanna commit?: "))

    if user_input in interactions:
        if user_input == 1:
            added_grade = int(input("which grade from 1-6 do you want to add?: "))
            grades.append(added_grade)
            print(f"{grades} ...these are all the grades including the one you added")


        elif user_input == 3:
            print(grades)


        elif user_input == 2:
            sum_of_grades = sum(grades)
            number_of_grades = len(grades)

            average_grade = sum_of_grades / number_of_grades
            print(average_grade)
        
        elif user_input == 4:
            break

    else:
        print("error")
