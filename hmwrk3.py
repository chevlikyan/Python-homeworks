# Task 1

'''
Given three numbers a, b (a ≤ b) and step. Create an list of
evenly spaced elements starting from a to b spaced by step. you
have 3 argument:
Input Output
1 5 1 [1, 2, 3, 4, 5]
10 100 20 [10, 30, 50, 70, 90]
'''

# def three_args(three_nums: list):
#     '''getting the start, end and the step get a new list through a for loop'''
#
#     new_list = []
#     start = three_nums[0]
#     end = three_nums[1]
#     step = three_nums[2]
#
#     if start == end or start > end:
#         return print("End numer must be greater than the start number!!!")
#     else:
#         for i in range(start, end + 1, step):
#             new_list.append(i)
#         return print(new_list)
#
#
# three_args([1, 1, 1])


# Task 2

'''
Imagine you and the computer are playing tennis. write a 
program where you have a sheet where victory points are 
kept and you need to figure out who is the winner.A set is
won by the first side to win 6 games. You should to show
the result of the match. If game win you in list add “a” if
pc “b”.
results=['b','a','a','a','a','a','a','a','a','a','a','a','b','b','b','b','b','b','a','a'
,'a','a', 'a','b','b','b','b','b', 'a','a','a','a','a','a','a','a','a','a','a','a','a','a','a']
'''

# def tenis(lst: list) -> str:
#     a = 0
#     b = 0
#     a1 = 0
#     b1 = 0
#     for i in results:
#         if i == 'a':
#             a += 1
#         else:
#             b += 1
#         if abs(a - b) > 1 and (a > 5 or b > 5):
#             if a > b:
#                 a = 0
#                 b = 0
#                 a1 += 1
#                 print(f"a win {a1}:{b1}")
#             else:
#                 a = 0
#                 b = 0
#                 b1 += 1
#                 print(f"b win {a1}:{b1}")
#
# results = ['b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'a'
#         , 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
# tenis(results)


# binary search without recursion


# def bs_without_recursion(the_list: list, search: int):
#     start = 0
#     end = len(numbers_list) - 1
#     # mid = (start + end) // 2
#     while start <= end:
#         mid = (start + end) // 2
#         if search == the_list[mid]:
#             return mid  # f"searching number is at {mid} index"
#         if search > the_list[mid]:
#             start = mid + 1
#         if search < the_list[mid]:
#             end = mid - 1
#     return False
#
#
# numbers_list = [30, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
# numbers_list.sort()
# result = bs_without_recursion(numbers_list, 80)
# if len(numbers_list) == 0:
#     print("the list is empty!!!")
# if result == False:
#     print("searching number is not in the list!!!")
# else:
#     print(f"searching number is at {result} index")
