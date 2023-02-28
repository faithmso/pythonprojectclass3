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


"""
Write a program that takes a list of strings and returns a new list that contains only the strings that start with the 
letter 'a'.strings = ["apple", "banana", "cherry", "date"]
"""


def starts_with_a(strings):
    list = []
    for char in strings:
        if char.startswith("a"):
            list.append(char)

    return list


strings = ["apple", "banana", "cherry", "date"]
print(starts_with_a(strings))


"""
Write a program that takes a sentence (string) and returns a dictionary with the count of each word in the sentence.
sentence = "this is a test sentence
"""


def word_count(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


sentence = "this is a test sentence"
print(word_count(sentence))


"""
Write a program that takes two lists of numbers and returns a new list that contains only the numbers that are common 
to both lists. 
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [2, 4, 6, 8, 10, 12, 14, 16, 18]
"""


def common_numbers(list1, list2):
    list = []
    for num in list1:
        if num in list2:
            list.append(num)
    return list


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [2, 4, 6, 8, 10, 12, 14, 16, 18]
print(common_numbers(list1, list2))


"""

Write a program that takes a list of integers and returns a new list that contains only the prime numbers from the 
original list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
"""


def prime_numbers(numbers):
    list = []
    for num in numbers:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                list.append(num)
    return list


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(prime_numbers(numbers))


"""
Write a program that takes a string and returns the number of words in the string.
string = "Write a program that takes a string"
"""


def count_words(string):
    words = string.split()
    return len(words)


string = "Write a program that takes a string"
print(count_words(string))


"""
Write a program that takes a list of strings and returns a new list that contains only the strings that are palindrome.
strings = ["madam", "level", "civic"]
"""


def palindrome(strings):
    list = []
    for word in strings:
        if word == word[::-1]:
            list.append(word)
    return list


strings = ["madam", "level", "civic"]
print(palindrome(strings))


"""
Write a program that takes a sentence (string) and returns a tuple of the most frequent word and its frequency.
sentence = "this is a test sentence to test the test"
"""


def most_frequent_word(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return max(word_count, key=word_count.get), max(word_count.values())


sentence = "this is a test sentence to test the test"
print(most_frequent_word(sentence))

