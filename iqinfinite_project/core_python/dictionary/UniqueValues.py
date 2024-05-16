# Extract Unique values dictionary values
'''
The original dictionary is : {'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5], 'best': [6, 12, 10, 8], 'for': [1, 2, 5]}
The unique values list is : [1, 2, 5, 6, 7, 8, 10, 11, 12]
'''
# Extract Unique values dictionary values : Solution 
class UniqueValues:
    def __init__(self,test_dictionary):
        self.__test_dictionary = test_dictionary
    def get_dictionary(self):
        return self.__test_dictionary
    def unique_values(self):
        test_dict = self.__test_dictionary
        res = list(sorted({ele for val in test_dict.values() for ele in val}))
        return res