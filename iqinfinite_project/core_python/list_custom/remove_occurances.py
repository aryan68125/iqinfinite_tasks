# Remove all the occurrences of an element from a list in Python
'''
Input1: 1 1 2 3 4 5 1 2 1 
Output1: 2 3 4 5 2 
Explanation : The input list is [1, 1, 2, 3, 4, 5, 1, 2] and the item to be removed is 1. 
              After removing the item, the output list is [2, 3, 4, 5, 2]
'''

# Remove all the occurrences of an element from a list in Python : solution
class RemoveAllOccurancesInList:
    def __init__(self,var_list):
        self.__var_list = var_list
    def get_list(self):
        return self.__var_list
    def remove_all_occurances_in_list(self,ele):
        var_list = self.__var_list
        test_list = var_list
        x=[j for i,j in enumerate(test_list) if j!=ele]
        return x
