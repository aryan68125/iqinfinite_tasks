# PRINT times table of a given number
# PRINT times table of a given number : solution
class TimesTable:
    def __init__(self,var_number,var_size):
        self.__var_number = var_number
        self.__var_size = var_size
    def get_number(self):
        return self.__var_number
    def get_size(self):
        return self.__var_size
    def times_table(self):
        number = self.__var_number
        size = self.__var_size
        for i  in range(1,size+1):
            mul = number * i
            print(f"\033[92m{number} X {i} = {mul}\033[97m")
