# Remove items from Set
'''
Input : set([12, 10, 13, 15, 8, 9])
Output :
{9, 10, 12, 13, 15}
{10, 12, 13, 15}
{12, 13, 15}
{13, 15}
{15}
set()
'''
# Remove items from Set : Solution
class RemoveItemsSets:
    def __init__(self, var_sets):
        self.__var_sets = var_sets
    def get_sets(self):
        return self.__var_sets
    def remove_element(self):
        var_set = self.__var_sets
        initial_set = var_set
        while initial_set:
            initial_set.pop()
            print(f"\033[92m{initial_set}\033[97m")