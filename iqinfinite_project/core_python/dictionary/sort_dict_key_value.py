# Sort Dictionary key and values List
'''
    Input : test_dict = {‘c’: [3], ‘b’: [12, 10], ‘a’: [19, 4]} 
    Output : {‘a’: [4, 19], ‘b’: [10, 12], ‘c’: [3]} 

    Input : test_dict = {‘c’: [10, 34, 3]} 
    Output : {‘c’: [3, 10, 34]}

    test_dict = {'gfg': [7, 6, 3], 
                 'is': [2, 10, 3], 
                 'best': [19, 4]}
'''
# Sort Dictionary key and values List : Solution

class SortDictionary:
    def __init__(self,test_dict):
        self.__test_tict = test_dict
    def get_dictionary(self):
        return self.__test_tict
    def sort(self):
        test_dict = self.__test_tict
        res = dict()
        for key in sorted(test_dict):
            res[key] = sorted(test_dict[key])
        return res