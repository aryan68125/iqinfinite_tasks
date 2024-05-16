# Swapping Hierarchy in Nested Dictionaries
'''
Input : test_dict = {‘Gfg’: { ‘a’ : [1, 3, 7, 8], ‘b’ : [4, 9], ‘c’ : [0, 7]}} 
Output : {‘c’: {‘Gfg’: [0, 7]}, ‘b’: {‘Gfg’: [4, 9]}, ‘a’: {‘Gfg’: [1, 3, 7, 8]}}
Input : test_dict = {‘Gfg’: {‘best’ : [1, 3, 4]}} 
Output : {‘best’: {‘Gfg’: [1, 3, 4]}} 
'''
# Swapping Hierarchy in Nested Dictionaries : Solution
class SwapNestedDictionary:
    def __init__(self,var_dictionary):
        self.__var_dictionary = var_dictionary
    def get_dictionary(self):
        return self.__var_dictionary
    def swapping_hierarchy(self):
        res = dict()
        test_dict = self.__var_dictionary
        for key, val in test_dict.items():
            for key_in, val_in in val.items():
                if key_in not in res:
                    temp = dict()
                else:
                    temp = res[key_in]
                temp[key] = val_in
                res[key_in] = temp
         
        # printing result 
        return str(res)