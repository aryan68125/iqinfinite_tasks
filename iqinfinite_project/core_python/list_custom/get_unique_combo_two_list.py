# Get all unique combinations of two Lists
'''
List_1 = ["a","b"]
List_2 = [1,2]
Unique_combination = [[('a',1),('b',2)],[('a',2),('b',1)]] 
'''
# Get all unique combinations of two Lists : Solution
import itertools
from itertools import permutations 
class GetUniqueCombinationTwoList:
    def __init__(self, list_one,list_two):
        self.__var_list_one = list_one
        self.__var_list_two = list_two
    def get_list_one(self):
        return self.__var_list_one
    def get_list_two(self):
        return self.__var_list_two
    def get_unique_combination_two_list(self):
        var_list_one = self.__var_list_one
        var_list_two = self.__var_list_two
        # create empty list to store the
        # combinations
        unique_combinations = []
        # Getting all permutations of list_1 
        # with length of list_2
        permut = itertools.permutations(var_list_one, len(var_list_two))
         
        # zip() is called to pair each permutation
        # and shorter list element into combination
        for comb in permut:
            zipped = zip(comb, var_list_two)
            unique_combinations.append(list(zipped))
         
        # printing unique_combination list 
        return unique_combinations