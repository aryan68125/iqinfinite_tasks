# Find all the Combinations in the list with the given condition
'''
Input: test_list = ["GFG", [5, 4], "is", ["best", "good", "better", "average"]]
Output: 
Combination 1 :  ('GFG', [5, 4])
Combination 2 :  ('GFG', 'is')
Combination 3 :  ('GFG', ['best', 'good', 'better', 'average'])
Combination 4 :  ([5, 4], 'is')
Combination 5 :  ([5, 4], ['best', 'good', 'better', 'average'])
Combination 6 :  ('is', ['best', 'good', 'better', 'average'])
'''
# Find all the Combinations in the list with the given condition : Solution

from itertools import combinations_with_replacement

class CombinationWithConditions:
    def __init__(self,var_list):
        self.__var_list = var_list
    def get_list(self):
        return self.__var_list
    def combination_with_list(self):
        test_list = self.__var_list
        temp = combinations_with_replacement(test_list, 2)
        idx=0
        for i in list(temp):
            idx = idx+1
            print (f"\033[92mCombination {idx} : {i}\033[97m")