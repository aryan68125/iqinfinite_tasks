# find common elements in three lists using sets
'''
Input : ar1 = [1, 5, 10, 20, 40, 80]
        ar2 = [6, 7, 20, 80, 100]
        ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

Output : [80, 20]

Input : ar1 = [1, 5, 5]
        ar2 = [3, 4, 5, 5, 10]
        ar3 = [5, 5, 10, 20]

Output : [5]
'''
# find common elements in three lists using sets : Solution
class CommonInThreeList:
    def __init__(self, var_list_1,var_list_2,var_list_3):
        self.__var_list_1 = var_list_1
        self.__var_list_2 = var_list_2
        self.__var_list_3 = var_list_3
    def get_list_1(self):
        return self.__var_list_1
    def get_list_2(self):
        return self.__var_list_2
    def get_list_3(self):
        return self.__var_list_3
    def find_common_in_three_list(self):
        var_set_1 = set(self.__var_list_1)
        var_set_2 = set(self.__var_list_2)
        var_set_3 = set(self.__var_list_3)
        # Calculates intersection of 
        # sets on s1 and s2
        set1 = var_set_1.intersection(var_set_2)         #[80, 20, 100]
         
        # Calculates intersection of sets
        # on set1 and s3
        result_set = set1.intersection(var_set_3)
         
        # Converts resulting set to list
        final_list = list(result_set)
        return final_list