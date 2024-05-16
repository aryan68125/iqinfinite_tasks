# Print list in reverse order using a loop
'''

'''
# Print list in reverse order using a loop : Solution
class ReverseList:
    def __init__(self,var_list):
        self.__var_list = var_list
    def get_list(self):
        return self.__var_list
    def revserse_list(self):
        var_list = self.__var_list
        new_list = reversed(var_list)
        for i in new_list:
            print(f"\033[92m{i}\033[97m")
