# Display numbers from a list using loop
'''
INPUT : numbers = [12, 75, 150, 180, 145, 525, 50]
OUTPUT : 
75
150
145
'''
# Display numbers from a list using loop : solution
class ExtractNumberFromList : 
    def __init__(self,var_list):
        self.__var_list = var_list
    def get_list(self):
        return self.__var_list
    def extract(self):
        var_list = self.__var_list
        for element in var_list:
            if element%5 == 0:
                if not element >= 500:
                    print(f"\033[92m{element}\033[97m")
                else:
                    break
