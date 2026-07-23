#just another prac sesseion nothing new

numbers = [1, 3, 5, 2, 54, 68, 1235, 546, 3 ,6 , 7, 7, 234, 12, 6]

def find_largest(numbers):
    numbers_max = numbers[0]
    for number in numbers:
        if number > numbers_max:
            numbers_max = number
    return numbers_max

largest_number = find_largest(numbers)
print(largest_number)
