# calculate sum of numbers in a series
'''
Enter number 10
Sum is:  55
'''
# calculate sum of numbers in a series : solution
class Sumission:
    def __init__(self,var_last_number):
        self.__var_last_number = var_last_number
    def get_last_number(self):
        return self.__var_last_number
    def sumission(self):
        var_last_number = self.__var_last_number
        sum=0
        for i in range(1,var_last_number+1):
            sum += i
            print(i)
        return sum