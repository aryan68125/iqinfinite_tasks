#  Count tuples occurrence in list of tuples
'''
Input = [[('hi', 'bye')], [('Geeks', 'forGeeks')],
         [('a', 'b')], [('hi', 'bye')], [('a', 'b')]]
defaultdict(<class 'int'>, {('Geeks', 'forGeeks'): 1, ('hi', 'bye'): 2, ('a', 'b'): 2})
'''
# Count tuples occurrence in list of tuples : solution
import collections 

class TupleOccurances:
    def __init__(self,var_list):
        self.__var_list = var_list
    def get_list(self):
        return self.__var_list
    def tuples_occurrence_in_list_of_tuples(self):
        Output = collections.defaultdict(int)
        var_list = self.__var_list
        for elem in var_list:
           Output[elem[0]] += 1
        return Output