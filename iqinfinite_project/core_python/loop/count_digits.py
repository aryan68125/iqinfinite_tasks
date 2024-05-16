# count digits in a number
'''
For example, the number is 75869, so the output should be 5.
'''
# count digits in a number : solution
class CountDigits:
    def __init__(self,var_number):
        self.__var_number = var_number
    def get_number(self):
        return self.__var_number
    def get_digits_count(self):
        num = self.__var_number
        count = 0
        while num != 0:
            # floor division
            # to reduce the last digit from number
            num = num // 10
        
            # increment counter by 1
            count = count + 1
        return count
    