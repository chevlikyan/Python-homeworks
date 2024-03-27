import math
import random

# Task 1

"""
Create a class that accepts a number of your body temperature by Celsius and duplicate
with the number of pi and rounded up to the nearest whole number
"""


class Covid:
    def __init__(self) -> None:
        """get input in this method"""
        self.temp = float(input("Enter your temperature: "))

    def temperature(self) -> str:
        """make the input as an integer multiply it with pi and check if the patient is ill or no"""
        int_temp = int(self.temp)
        the_temp_pi = int_temp * math.pi
        if the_temp_pi > 120 and the_temp_pi < 128:
            return "You have coronavirus"
        if the_temp_pi > 128:
            return "Game Over "
        else:
            return "Every thing is okay"


c = Covid()
print(c.temperature())

# Task 2


"""
Create a class that accepts a string of your name and it will tell the number of your name
will tell if it is widespread or not .
"""


class Name:
    def __init__(self) -> None:
        """Enter the name"""
        self.name = str(input("Enter your name: "))
        self.counter = 0

    def the_name(self) -> int:
        """checks the corresponding number of every letter in the given name and add them"""
        letters = {
            1: ["a", "j", "s"], 2: ["b", "k", "t"], 3: ["c", "l", "u"],
            4: ["d", "m", "v"], 5: ["e", "n", "w"], 6: ["f", "o", "x"],
            7: ["g", "p", "y"], 8: ["h", "q", "z"], 9: ["i", "r"]
        }
        low_name = self.name.lower()
        for letter in low_name:
            for k, v in letters.items():
                if letter in v:
                    self.counter += k
        return self.counter

    def do_sqrt(self) -> str:
        """check if the name is widespread or no"""
        if math.sqrt(self.counter) < 5:
            return "Yes"
        else:
            return "No"


n = Name()
print(n.the_name(), n.do_sqrt())

# Task 3

"""
Create a class that accepts three string through which you will try to guess the random
magic word of the Lord Voldemort.
"""


class HarryPotter:
    def __init__(self) -> None:
        """Enter the list of magic words"""
        self.the_magic_words = ["Avada Kedavra", "Crucio", "Imperio"]

    def corresponding(self) -> str:
        """get the magic word from the user and check with the chosen magic word. Tell if the user wins or no"""
        counter = 0
        for i in range(3):
            magic_word = input("Your magic word is: ")
            choosen_word = random.choice(self.the_magic_words)
            if magic_word.lower() == choosen_word.lower():
                counter += 1
            else:
                counter -= 1
        if counter < 1:
            return "You lose"
        else:
            return "You win"


hp = HarryPotter()
print(hp.corresponding())

