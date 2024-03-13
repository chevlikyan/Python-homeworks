# def bdg_decorator(func):
#     def inner():
#         print("Hello BDG, this is before function execution")
#         func()
#         print("This is after function execution")
#
#     return inner
#
#
# def function_to_be_used():
#     print("This is inside the function !")
#
#
# function_to_be_used = bdg_decorator(function_to_be_used)
# function_to_be_used()

# def convert_to_data_type(data_type):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             return data_type(result)
#
#         return wrapper
#
#     return decorator
#
#
# @convert_to_data_type(int)
# def add_numbers(x, y):
#     return x + y
#
#
# result = add_numbers(10, 20)
# print("Result:", result, type(result))
#
#
# @convert_to_data_type(str)
# def concatenate_strings(x, y):
#     return x + y
#
#
# result = concatenate_strings("Python", " Decorator")
# print("Result:", result, type(result))

# Task 1

'''Create a python program which will say which number used more. my_list = [1,
3, 4, 5, 1, 2, 3, 1] output: number 1 - 3 times'''
# my_list = [1, 3, 4, 5, 1, 2, 3, 1]
#
#
# def used_more(numbers: list) -> str:
#     '''
#     From number list choose most used one and return
#     '''
#     item = list({i: numbers.count(i) for i in numbers}.items())
#     max_val = item[0][1]
#     max_key = item[0][0]
#
#     for i in item:
#         if i[1] > max_val:
#             max_val = i[1]
#             max_key = i[0]
#     return (f"number {max_key} - {max_val} times")
#
#
# print(used_more(my_list))

# Task 2
#
# '''Write a Python program to sum all the items in a list. use list comprehension'''
#
# my_list = [1, 3, 4, 5, 1, 2, 3, 1]
#
# lis =

# from typing import Callable
# def create_adder(x: int) -> Callable[[int], int]:
#     def adder(y: int) -> int:
#         return x+y
#     return adder
#
# add_12 = create_adder(12)
# print(type(add_12))
# print(add_12(11))

# task 2
'''Write a Python program to sum all the items in a list. use list comprehension'''
# lst = [1, 3, 5, 6, 9, 10, 25, 7, 2]
#
# count = 0
# new_lst = [count:= count + i  for i in lst]
#
# print(new_lst[-1])


# Task 3

'''Write a Python program to get the largest text from a list'''

# def largest_text(text_list: str) -> str:
#     spl = text_list.split(" ")
#
#     for i in range(len(spl)):
#         max = len(spl[0])
#         txt = spl[0]
#         if len(spl[i]) > max:
#             max = len(spl[i])
#             txt = spl[i]
#
#     return print(txt)
#
#
# largest_text("efscv wd waedv awefdcsveaf")

# Task 4

'''Write a Python program that have two lists and returns True if they have at
least one common member'''

# def common_member(text1: list, text2: list) -> bool:
#     is_common = bool
#     for i in text1:
#         if i in text2:
#             is_common = True
#             break
#         else:
#             is_common = False
#     return is_common
#
#
# text1 = [1, 3, 5, 6, 9, 10, 25, 7, 2]
# text2 = [16, 3, 55, 656, 956, 1056, 255, 74, 25]
#
# print(common_member(text1, text2))


# Task 5

'''Write a Python program to Sort Words in Alphabetic Order'''

# def sorted_words(text: str) -> str:
#     # spl = text.split()
#     return print(sorted([i for i in text.upper().split()]))
#
# sorted_words("Write a Python program to Sort Words in Alphabetic Order")

# Task 6

'''Write a Python program that creates a generator function that generates all
prime numbers between two given numbers'''

# num1 = 9
# num2 = 110
#
#
# def prime_number(num1: int, num2: int) -> int:
'''Using generator and the principe of prime number get the prime numbers between the given 2 numbers'''
#     for i in range(num1, num2 + 1):
#         if i == 1:
#             yield f"{i} is not prime number"
#             i += 1
#         if i > 1:
#             for j in range(2, i):
#                 if (i % j) == 0:
#                     break
#             else:
#                 yield f"{i} is prime number"
#                 i += 1
#
#         else:
#             yield f"{i} is not prime number"
#
#
# counter = prime_number(num1, num2)
# print(next(counter))
# print(next(counter))
# print(next(counter))

# Task 7

'''Create python program which will check if your password is strong or no. if Len 
your password is great than 8 and if your password have 2 numbers and 2 of the 
following special characters ('!', '@', '#', '$', '%', '&', '*') 
Sample Input: Python@$World11
Sample Output: Strong'''

# import string
#
#
# def pass_str(password: str) -> str:
#     '''Check the len then the availability of 2 numbers and 2 symbols'''
#
#     if len(password) < 8:
#         return print("Not strong")
#     numb = 0
#     sym = 0
#     symbols = ['!', '@', '#', '$', '%', '&', '*']
#     numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     for i in password:
#         if i in string.digits:
#             numb += 1
#         if i in symbols:
#             sym += 1
#     if sym == 2 and numb == 2:
#         print("Strong")
#     else:
#         return print("Not strong")
#
#
# pass_str("dzaedbgdeb11*%")


# Task 8
'''Create python program where you want to find id in link if link have id print id.
Sample Input: https://www.youtube.com/watch?v=RRW2aUSw5vU
Sample Output: RRW2aUSw5vU'''

# def id_search(link: str) -> str:
#     '''
#     checking the link Spliting by =
#     '''
#
#     spl = link.split("=")
#     if len(spl) < 2:
#         return "The link dont have an id: "
#     else:
#         return spl[1]
#
#
# print(id_search("https://www.youtube.com/watch?v=RRW2aUSw5vU"))

# Task 9

'''Write a Python program that implements a decorator to validate function arguments
based on a given condition'''

# Task 1
"""
Write a Python program which will
remove all zeros from an IP
address.
ip = "216.008.094.196"
"""

# def replacer(ip: str) -> str:
#     spl = ip.split(".")
#     ip_list = []
#     for i in range(len(spl)):
#         ip_list.append(spl[i].replace("0", ""))
#     ip = ".".join(ip_list)
#     return print(ip)
#
#
# replacer("216.008.094.196")

# Task 2

'''Given an list of numbers.
Find the maximum element in 
list.Without use max 
function'''

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
# def max_num(the_list: list) -> int:
#     max_n = the_list[0]
#     for i in the_list:
#         if i > max_n:
#             max_n = i
#     return print(max_n)
#
#
# max_num(nums)


# Task 3

'''Write a Python program that validates passwords based on the following
criteria:
● The password must be at least 8 characters long.
● The password must contain at least one uppercase letter.
● The password must contain at least one lowercase letter.
● The password must contain at least one digit (0-9).
● The password must contain at least one special character (e.g., @, #, $,
etc.)'''

# import string
#
# def pass_validation(password: str) -> str:
#     upps = 0
#     lows = 0
#     ints = 0
#     specs = 0
#     for i in password:
#         if len(password) < 8:
#             print("less characters")
#             break
#         if i.isupper():
#             upps += 1
#         if i.islower():
#             lows += 1
#         if isinstance(i, int):
#             ints += 1
#         if i in string.punctuation:
#             specs += 1
#
#     if upps >= 1 and lows >= 1 and ints >= 1 and specs >= 1:
#         return print(f"Your {password} password is valid")
#     else:
#         return print(f"Your {password} password is not valid!!!")
#
# pass_validation("Hello16World&$")

# Task 4

'''Write a program that takes in a string as input, counts and outputs the number of vowels.
For example:
input: test
output: 1'''

'''didn't understand'''

# Task 5

'''Write a function. Create the list which elements are
products between two neighbours.
 Input                        Output
 input : [3, 7, 12, 5, 20, 0] output: [21, 84, 60, 100, 0]
 input : [1, 1, 4, 32, 6]     output: [1, 4, 128, 192 ]'''

# def neighbours_prod(lst: list) -> list:
#     prod = []
#     for i in range(len(lst)-1):
#         prod.append(lst[i] * lst[i+1])
#
#     return print(prod)
#
# neighbours_prod([3, 7, 12, 5, 20, 0])

# Task 6

'''Given a sentence with missing words and an array of words. Replace all _ in a sentence with the words from
the array.
Input “_ we have a _.”
[“Ashot”, “problem”]
Output: “Ashot we have a problem'''

# def replacer(txt: str, wrds: list) -> str:
#     spl = txt.split()
#     q = 0
#     for i in range(len(spl)):
#         if spl[i] == "_":
#             spl[i] = wrds[q]
#             q += 1
#
#     print(" ".join(spl))
#
# replacer("_ we have a _ .", ["Ashot", "problem"])

# Task 7

'''Given a list of strings. Find the strings with maximum
and minimum lengths in array. Print the sum of their
lengths.
Input: [“anymore”, “raven”, “me”, “communicate”]
Output: 13'''

# def sum_of_lenghts(lst: list) -> int:
#     max_len = len(lst[0])
#     min_len = len(lst[0])
#     for i in lst:
#         if len(i) > max_len:
#             max_len = len(i)
#         if len(i) < min_len:
#             min_len = len(i)
#
#     print(min_len + max_len)
#
#
# sum_of_lenghts(["anymore", "raven", "me", "communicate"])

# Task 8

'''Given a list of numbers and a number. Find the index
of a first element which is equal to that number. If there is
not such a number, that find the index of the first element
which is the closest to it. Input Output [21, -9, 15, 2116, -71, 33], -71 4
[ 36, -12, 47, -58, 148, -55, -19, 10], -56 5'''


# def index_finder(lst: list, num: int) -> int:
#     plus = 0
#     minus = 0
#     if num in lst:
#         print(lst.index(num))
#     # if num not in lst:
#     #     for i in lst:
#     #         if abs(num) - i < minus:
#     #             minus = (abs(num) - i)
#     """couldn't do the second part of the task"""
#
# index_finder([21, -9, 15, 2116, -71, 33], -71)

# Task 9

'''Given an dict. Invert it (keys become values and values
become keys). If there is more than key for that given
value create an list.Input
{ "a": 1, "b": 2, "c": 2 }
Output
{ 1: "a", 2: ["b", "c"] }
{a:1, b:2}'''

# Task 10

'''Define a function which can generate a dictionary
where the keys are numbers between 1 and N (both
included) and the values are square of keys. The function
should print the dict.Example :
N = 5
{1: 1, 2:4, 3:9, 4:16, 5:25}'''

# def nums_square(n: int) ->dict:
#     print({i: i*i for i in range(1, n+1)})
#
# nums_square(5)