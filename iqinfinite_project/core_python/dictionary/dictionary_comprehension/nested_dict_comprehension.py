'''
INPUT : 
l="GFG"
OUTPUT : 
{'G': {'G': 'GG', 'F': 'GF'}, 'F': {'G': 'FG', 'F': 'FF'}}
'''
class NestedDictionary:
    def __init__(self,var_string):
        self.__var_string = var_string

    @property
    def var_string(self):
        return self.__var_string
    @var_string.setter
    def var_string(self,var_string):
        self.__var_string = var_string
    
    def generate(self):
        var_string = self.__var_string
        dic = {
            x: {y: x + y for y in var_string} for x in var_string
        }
        return dic
    