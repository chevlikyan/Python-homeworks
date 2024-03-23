# Task 1
'''
Create a class which given a year, return the century
it is in. The first century spans from the year 1 up to
and including the year 100, the second - from the
year 101 up to and including the year 200, etc.
For year = 1900, the output should be = 19
'''

# class YearToCentury:
#     def __init__(self, year: int):
#         self.year = year
#
#     def the_century(self):
#         century = self.year // 100
#         # century = self.year % 100
#         # if century == 0:
#         #     return
#         # else:
#         #     return self.year // 100 + 1
#         return century if not self.year % 100 else century + 1
#
#
# y = YearToCentury(1900)
# print(y.the_century())


# Task 2

'''
Create a class given the string, check if it is a palindrome.
word should be lowercase and 1 ≤ inputString.length ≤ 105
Example 
For inputString = "aabaa", the output should be true; 
For inputString = "abac", the output should be false; 
For inputString = "a", the output should be true.
'''

# class Palindrome:
#     def __init__(self, word: str):
#         self.word = word
#
#     def validate_word(self):
#         if not (1 <= len(self.word) <= 105 and self.word.islower()):
#             raise ValueError('wrong word')
#
#     def is_palindrome(self) -> bool:
#         return self.word[::-1] == self.word
#
#     def run(self):
#         self.validate_word()
#         return self.is_palindrome()
#
# x = Palindrome("aabaa")
# print(x.run())


# task 3
'''
Create a Class which given an list of integers, find the pair of
adjacent elements that has the largest product and return that
product.
For inputList = [3, 6, -2, -5, 7, 3],
the output should be = 21
'''
# class MaxNumber:
#     def __init__(self,n):
#         self.n = n
#     def maxProduct(self):
#         max_number = self.n[0] * self.n[1]
#         for i in range(len(self.n)-1):
#             if self.n[i]*self.n[i+1] > max_number:
#                 max_number = self.n[i]*self.n[i+1]
#         return max_number
# x= MaxNumber([3,6,-2,-5,7,3])
# print(x.maxProduct())


# Task 4
'''
Create a class which given a list of strings, return another list containing
all of its longest strings.
Example
For inputList = ["aba", "aa", "ad", "vcd", "aba"],
the output should be
 allLongestStrings(inputList) = ["aba", "vcd", "aba"].
'''

# class HighestWord:
#     def __init__(self, the_list: list) -> list:
#         self.the_list = the_list
#
#     def the_longest(self):
#         empty_list = []
#         self.the_list = sorted(self.the_list)
#
#         max_length = len(self.the_list[0])
#
#         for i in range(len(self.the_list)):
#             if len(self.the_list[i]) > max_length:
#                 max_length = len(self.the_list[i])
#         for i in range(len(self.the_list)):
#             if len(self.the_list[i])==max_length:
#                 empty_list.append(self.the_list[i])
#         return empty_list
# x = HighestWord(['a', 'bnaa', "aba", "aa", "ad", "vcd", "aba"])
# print(x.the_longest())


# Task 5
'''Ticket numbers usually consist of an even number of digits.A ticket number is 
considered lucky if the sum of the first half of the digits is equal to the sum of the 
second half.Given a ticket number n, determine if it's lucky or not. Example For n 
= 1230, the output should be 
Lucky(n) = true; 
For n = 239017, 
the output should be Lucky(n) = false'''

# class Lucky:
#     def __init__(self, num: int):
#         self.num=num
#     def lucky_ticket(self):
#         if len(str(self.num))%2!=0:
#            raise ValueError('odd number')
#
#         else:
#             str_num = str(self.num)
#             mid=len(str_num) // 2
#             c = [int(i) for i in str_num]
#             return sum(c[mid:]) == sum(c[:mid])
#
# x=Lucky(23520)
# print(x.lucky_ticket())

# Task 6

'''
Create a class: Some people are standing in a row in a park. There are trees 
between them which cannot be moved. Your task is to rearrange the people by their 
heights in a non-descending order without moving the trees. People can be very tall!
Example
 For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
 sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
'''


class High:
    def __init__(self, the_list):
        self.the_list = the_list

    def list_sort(self):
        new_list = []
        for i in self.the_list:
            if i != -1:
                new_list.append(i)

        new_list.sort()
        print(new_list)
        counter = 0
        for i in range(len(self.the_list)):
            if self.the_list[i] != -1:
                self.the_list[i] = new_list[counter]
                counter += 1

        return self.the_list


x = High([-1, 150, 190, 170, -1, -1, 160, 180])
print(x.list_sort())
