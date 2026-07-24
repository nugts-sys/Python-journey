#another repetition of loops

numbers = [1, 3, 5, 6, 8, 1, 3, 2, 5, 9, 0, 6, 5, 5, 7, 6, 4, 2, 8]

def count_even(numbers):
    even_numbers = 0
    for evens in numbers:
        if evens % 2 == 0:
            even_numbers += 1
    return even_numbers

total_even = count_even(numbers)
print(total_even)
