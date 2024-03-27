# Task 7

'''
Several people are standing in a row and need to be divided into two teams. The first
person goes into team 1, the second goes into team 2, the third goes into team 1
again, the fourth into team 2, and so on.You are given an array of positive integers -
the weights of the people. Return an array of two integers, where the first element is
the total weight of team 1, and the second element is the total weight of team 2 after
the division is complete.
Example For a = [50, 60, 60, 45, 70], the output should be
alternating Sums(a) = [180, 105].
'''

class WeghtOfTeams:
    def __init__(self, the_list: list):
        self.the_list = the_list

    def weight_of_teams(self):
        teams = [0, 0]
        for i in range(len(self.the_list)):
            if i % 2 == 0:
                teams[0] += self.the_list[i]
            else:
                teams[1] += self.the_list[i]
        return teams


w = WeghtOfTeams([50, 60, 60, 45, 70])
print(w.weight_of_teams())