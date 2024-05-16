'''
INPUT : 
[1, 2, 3, 4, 5]
OUTPUT : 
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''
class GenerateDictionaryFromSingleList:
    def __init__(self,var_list_keys):
        self.__var_list_keys = var_list_keys

    # getters and setters for __var_list_keys
    @property
    def keys(self):
        return self.__var_list_keys
    @keys.setter
    def keys(self, keys):
        self.__var_list_keys = keys
    
    def generate(self):
        keys = self.__var_list_keys
        my_dictionary = {elements: elements*elements for elements in keys}
        return my_dictionary