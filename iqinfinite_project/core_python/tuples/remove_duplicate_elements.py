# Removing duplicates from tuple
'''
example : -->
The original tuple is : (1, 3, 5, 2, 3, 5, 1, 1, 3)
The tuple after removing duplicates : (1, 3, 5, 2)
'''
# Removing duplicates from tuple : Solutions
class RemoveDuplicateElements:
    def __init__(self,var_tuple):
        self.__var_tuple = var_tuple
    def get_tuple(self):
        return self.__var_tuple
    def remove_duplicate_elements(self):
        var_tuple = self.__var_tuple
        res = tuple(set(var_tuple))
        return res
        
