# Print all Possible Combinations from the three Digits
'''
Input: [1, 2, 3]
Output:
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
'''
# Print all Possible Combinations from the three Digits : Solution
from itertools import permutations
class PossibleComboThreeDigits:
    def __init__(self, var_digits_list):
        self.__var_digits_list = var_digits_list
    def get_list(self):
        return self.__var_digits_list
    def possible_combo(self):
        var_didigts_list = self.__var_digits_list
        combos = permutations(var_didigts_list,3)
        return combos