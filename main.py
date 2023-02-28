"""
Write a program that takes a list of numbers and returns the largest number in the list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""


def largest_number(numbers):
    return max(numbers)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(largest_number(numbers))


"""
Write a program that takes a string and returns the number of vowels in the string.
string = "Hello, world!"
"""


def count_vowels(string):
    count = 0
    for char in string:
        if char in "aeiou":
            count += 1
    return count


string = "Tom Loves me"
print(count_vowels(string))