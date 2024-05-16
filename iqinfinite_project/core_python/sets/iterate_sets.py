# Iterate over a set in Python
'''
test_set = set("geEks")
outputs : 
k
s
e
g
E
'''
# Iterate over a set in Python : Solution
class IterateSetsElements:
    def __init__(self,var_strings):
        self.__var_strings = var_strings
    def get_strings(self):
        return self.__var_strings
    def interate_sets_elements(self):
        var_strings = self.__var_strings
        test_set = set(var_strings)
        for val in test_set:
            print(f"\033[92m{val}\033[97m")