#Day 5. working on the grade manager of day 4 and upgrading it using functions


grades = [1, 4, 3, 5, 2, 3, 3, 2, 4, 5, 5]
print(grades)

print("These are all the grades for the end of this year.")
print("You interact with this list in the following ways: ")

interactions = {1:"add grade", 
                2:"show average grade",
                3:"display all grades", 
                4:"exit"}

print(interactions)

def add_grade(grades):
    added_grade = int(input("which grade from 1-6 do you want to add?: "))
    while added_grade < 1 or added_grade > 6:
        print("grades can only be between 1 and 6")
        added_grade = int(input("which grade from 1-6 do you want to add?: "))
         
    grades.append(added_grade)
    return grades


def show_average(grades):
    sum_of_grades = sum(grades)
    number_of_grades = len(grades)
    show_average = sum_of_grades / number_of_grades
    return show_average

def display_all_grades(grades):
    return grades


while True:

    user_input = int(input("Which of these actions do you want to commit?: "))


    if user_input == 1:
        grades = add_grade(grades)
        print(grades)


    elif user_input == 2:
        print(show_average(grades))

    elif user_input == 3:
        print(display_all_grades(grades))

    elif user_input == 4:
        break
    
#now each interaction from the beginning that i first only used if and else for has a own function
#i had problems with integrating a sort of error that doesnt let users put in grades outside of the range between 1-6
