# Difference between two lists
'''
Input:
list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35] 
Output: [10, 15, 20, 30]
Explanation: resultant list = list1 - list2
'''
# Difference between two lists : solution

class DifferenceBetweenTwoLists:
    def __init__(self,var_list_1,var_list_2):
        self.__var_list_1 = var_list_1
        self.__var_list_2 = var_list_2
    def get_list_1(self):
        return self.__var_list_1
    def get_list_2(self):
        return self.__var_list_2
    def difference_between_two_lists(self):
        li1 = self.__var_list_1
        li2 = self.__var_list_2
        s = set(li2)
        temp3 = [x for x in li1 if x not in s]
        return temp3
    