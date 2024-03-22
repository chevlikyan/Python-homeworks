# Task 1

'''
Write a python class to find max, min num and
sum in your list:
don’t use max sum and min function
'''


class lis:
    def __init__(self, the_list):
        self.the_list = sorted(the_list)

    def minimum(self):
        return self.the_list[-1]

    def maximum(self):
        return self.the_list[0]

    def the_sum(self):
        summary = 0
        for num in self.the_list:
            summary += num
        return summary


the_list = [1, 2, 3, 4, 5]
options = lis(the_list)
print(options.minimum())
print(options.maximum())
print(options.the_sum())

# Task 2

'''
Write a python class to find two highest values in your 
dict
'''


class two_highests:
    def __init__(self, the_list):
        self.the_list = sorted(the_list)

    def highests(self):
        return self.the_list[-1], self.the_list[-2]


the_list = [1, 2, 3, 4, 5]
high = two_highests(the_list)
print(high.highests())

# Task 3

'''
Write a python class where your child class takes all 
methods in parent class and print them
'''


class Parent:
    def parent(self):
        print("parent class")


class Child(Parent):
    def child(self):
        super().parent()
        print("child class")


child_parent = Child()
child_parent.child()

# Task 4

'''
Write a Python class named Rectangle constructed by
a length and width and a method which will compute the
area of a rectangle.
'''


class Rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def area(self):
        a = self.width * self.lenght
        return a


rec = Rectangle(3, 5)
print(rec.area())

# Task 5

'''
Write a python class where we use polymorphism:
Example:
a.country() - Erevan
b.country() - Paris
'''


class Poly:
    def method(self):
        print("Thank you")


class Polymor:
    def method(self):
        print("my dear")


p = Poly()
po = Polymor()
p.method()
po.method()

# Task 6

'''
Create a class Change:You have 3 
methods in your class:
Usd --- Eur
Usd --- Amd
Usd --- Ru
'''


class Change:
    def __init__(self, sum):
        self.sum = sum

    def usd_to_eur(self):
        return self.sum * 0.93

    def usd_to_amd(self):
        return self.sum * 398.28

    def usd_to_ru(self):
        return self.sum * 92.29


change = Change(100)
print(f"100 usd is {change.usd_to_eur()} eur")
print(f"100 usd is {change.usd_to_amd()} amd")
print(f"100 usd is {change.usd_to_ru()} ru")