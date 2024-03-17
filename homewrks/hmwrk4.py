# Task 1

'''
Write a recursive function to determine whether
all digits of the number are odd or not.
Input      Output
4211133    False
7791       True
5          True
'''

# number = 1357
#
#
# def numbers(nums: int) -> bool:
'''checking every number using bools return True or False'''
#     tens = nums % 10
#     if tens == 0:
#         return True
#     if tens % 2 == 0:
#         return False
#     else:
#         return numbers(nums // 10)
#
#
# print(numbers(number))


# Task 2

'''
Write a python function all even number 
in 10.000 use threading and print time
'''

# import threading
# import time
#
# def evens(start: int, end: int):
'''using threads and for loop separate even numbers '''
#     for i in range(start, end, 2):
#         with open("even_nums.txt", "a") as f:
#             f.write(f"{i}\n")
#
#
# starting = time.time()
# t1 = threading.Thread(target=evens, args=(2, 2500))
# t2 = threading.Thread(target=evens, args=(2500, 5000))
# t3 = threading.Thread(target=evens, args=(5000, 7500))
# t4 = threading.Thread(target=evens, args=(7500, 10001))
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t1.join()
# t2.join()
# t3.join()
# t4.join()
# ending = time.time()
# print(ending - starting)

# Task 3

'''
Given N number. Write a recursive function 
that should print from 1 to N numbers.
Input Output 
5 1, 2, 3, 4, 5
'''

# number = 6
#
#
# def nums(n) -> int:
#     global number
#
#     if n == 0:
#         return
#     else:
#         nums(n - 1)
#         if n == number:
#             print(n)
#         else:
#             print(n, end=", ")
#
#
# nums(number)

# Task 4

'''
Write a python program to find the longest word from the file content.Need
to use <try-except> block in the file reading process and print time. example:
1. try:
2.     with open("filename.txt") as file:
3.     some code
4. except:
5.     do something
6. Function call: find_long_word("filename.txt")
7. Function output: "LongestWord
'''

# file = "words.txt"
#
#
# def longest(file):
#     try:
#         with open(file) as f:
#             for line in f.readlines():
#                 word = line[:-1].split(" ")
#
#             print(max(word, key=len))
#     except NameError:
#         print("name 'file' is not defined!!!")
#     except SyntaxError:
#         print("be carefull")
#
#
# longest(file)

# Task with lyrics

# def lyrics(file_name):
#     with open(file_name) as f:
#         lyric = {}
#         for line in f.readlines():
#             words = line[:-1].split(" ")
#             for word in words:
#                 if lyric.get(word):
#                     lyric[word] += 1
#                 else:
#                     lyric[word] = 1
#
#     print(lyric)
#
# lyrics("lyrics.txt")


# task about lyrics
'''
word counts in lyrics
'''

# def lyrics(file_name):
'''using readlines import every line into list and count every word then add it into dictionary(word: key)'''
#     with open(file_name) as f:
#         lyric = {}
#         for line in f.readlines():
#             words = line[:-1].split(" ")
#             for word in words:
#                 if lyric.get(word):
#                     lyric[word] += 1
#                 else:
#                     lyric[word] = 1
#
#     print(lyric)
#
# lyrics("lyrics.txt")