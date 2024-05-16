'''
convert two lists into a single dictionary
INPUT : 
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]
OUTPUT : 
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
'''
class ListToDictionary:
    def __init__(self,var_list_keys,var_list_values):
        self.__var_list_keys = var_list_keys
        self.__var_list_values = var_list_values
    
    # getters and setters for var_list_keys
    @property
    def keys(self):
        return self.__var_list_keys
    @keys.setter
    def keys(self,var_list_keys):
        self.__var_list_keys = var_list_keys
    
    # getters and setters for var_list_values
    @property
    def values(self):
        return self.__var_list_values
    @values.setter
    def values(self,var_list_values):
        self.__var_list_values = var_list_values
    
    def convert(self):
        keys = self.__var_list_keys
        values = self.__var_list_values
        myDict = { k:v for (k,v) in zip(keys, values)}
        return myDict