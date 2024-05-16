# List product excluding duplicates
'''
The original list is : [1, 3, 5, 6, 3, 5, 6, 1]
Duplication removal list product : 90
'''
# List product excluding duplicates : duplicates

import functools
def prod(val):
    res = 1
    for ele in val:
        res *= ele
    return res
class ListProductExcludingDuplicates:
    def __init__(self, input_list):
        self.__var_list = input_list
    def get_list(self):
        return self.__var_list
    def list_product_excluding_duplicates(self):
        input_list = self.__var_list
        res = []
        [res.append(x) for x in input_list if x not in res]
        res = prod(res)
        result = res
        return result
        
