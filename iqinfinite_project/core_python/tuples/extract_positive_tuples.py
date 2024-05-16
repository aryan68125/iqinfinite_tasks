# Python program to find Tuples with positive elements in List of tuples
'''
Python program to find Tuples with positive elements in List of tuples
Input : test_list = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, -6)] 
Output : [(4, 5, 9)] 
Explanation : Extracted tuples with all positive elements.
'''
# Python program to find Tuples with positive elements in List of tuples : solution
class ExtractPositiveTuples:
    def __init__(self,var_list):
        self.__var_list = var_list
    def get_list(self):
        return self.__var_list
    def extract_positive_tuples(self):
        var_list = self.__var_list
        res = [sub for sub in var_list if all(ele >= 0 for ele in sub)]
        return res