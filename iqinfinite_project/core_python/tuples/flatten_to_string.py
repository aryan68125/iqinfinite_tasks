# Flatten Tuples List to String
'''
The original list : [('1', '4', '6'), ('5', '8'), ('2', '9'), ('1', '10')]
Tuple list converted to String is : 1 4 6 5 8 2 9 1 10
'''
# Flatten Tuples List to String : Solution
class FlattenTuplesToString:
    def __init__(self, var_list_of_tuples):
        self.__var_list_of_tuples = var_list_of_tuples
    def get_list(self):
        return self.__var_list_of_tuples
    def flatten_tuples_to_strings(self):
        var_list_of_tuples = self.__var_list_of_tuples
        res = ' '.join([idx for tup in var_list_of_tuples for idx in tup])
        return res