def number_validation(number):
    """get the number and check if it starts with 0 or +374,
     if the len of number is correct and if the operator is correct"""
    operators = ["77", "55", "44", "98", "94", "43", "33", "10", "60", "11", "96"]

    def wrapper():

        cheked_number = number.strip()

        if cheked_number.startswith("0"):
            cheked_number = "+374" + cheked_number[1:]
        if not cheked_number.startswith("+374"):
            raise TypeError("the number doesn't start with +374")
        if not len(cheked_number) == 12:
            raise ValueError("invalid number")
        if not cheked_number[4:6] in operators:
            raise Exception("no operators")
        return f"{cheked_number} is valid"

    return wrapper


phone = input("Enter the phone number: ")
the_number = number_validation(phone)
print(the_number())


# extra_task
"""
Consider an array of integers with starting index of 1, numbers, that is sorted in ascending order. Your task is
to identify two distinct elements, numbers[i] and numbers[j], such that their sum equals a predetermined target value.
Here, the constraints are 1 <= i < j <= length(numbers).

Your output should be an integer array of length 2, [i, j],
representing the indices of the two numbers incremented by one.
"""


def array(the_list: list, target: int) -> list:
"""using for loop check the sum of two numbers if its equal to target return the indexes of those two numbers"""
    for i in range(len(the_list)):
        for j in range(len(the_list)):
            sum = the_list[i] + the_list[j]
            if sum == target:
                return [i + 1, j + 1]


print(array([1, 4, 5], 9))

def array(the_list: list, target: int) -> list:
"""using for loop check the sum of two numbers if its equal to target return the indexes of those two numbers"""
    count1 = 0
    count2 = 1
    length = len(the_list)
    while True:

        if the_list[count1] + the_list[count2] == target:
            return [count1, count2]
        if the_list[count1] + the_list[count2] != target:
            count2 += 1
        if count2 == length:
            count1 += 1
            count2 = count1 + 1


print(array([2, 7, 11, 15], 9))
