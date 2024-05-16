# 7 Keys associated with Values in Dictionary
'''
Keys associated with Values in Dictionary
The original dictionary is : {'is': [1, 4], 'gfg': [1, 2, 3], 'best': [4, 2]}
The values associated dictionary : {1: ['is', 'gfg'], 2: ['gfg', 'best'], 3: ['gfg'], 4: ['is', 'best']}
'''
# 7 Keys associated with Values in Dictionary : solution
from collections import defaultdict
# printing result  
class KeyAssociatedWithValuesInDictionary:
    def __init__(self, test_dict):
        self.__test_dict = test_dict
    def get_dictionary(self):
        return self.__test_dict
    def key_associated_with_values_in_dictionary(self):
        test_dict = self.__test_dict
        res = defaultdict(list)
        for key, val in test_dict.items():
            for ele in val:
                res[ele].append(key)
        return res