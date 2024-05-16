'''
    def __str__(self):
        return "hello"
    This is magic method that gets executed when you put the object of your class inside a print function

    How to use this class
    # Create instances of Fraction_class
    fraction1 = Fraction_class(1, 2)
    fraction2 = Fraction_class(1, 3)
    
    # Perform arithmetic operations
    addition_result = fraction1 + fraction2
    subtraction_result = fraction1 - fraction2
    multiplication_result = fraction1 * fraction2
    division_result = fraction1 / fraction2
    
    # Output the results
    print("Addition:", addition_result)             # Output: 5/6
    print("Subtraction:", subtraction_result)       # Output: 1/6
    print("Multiplication:", multiplication_result) # Output: 1/6
    print("Division:", division_result) 

    some explaination :
'''
class Fraction_class:
    def __init__(self,n,d):
        self.__numerator = n
        self.__denominator = d
    
    def __str__(self):
        return "{}/{}".format(self.__numerator,self.__denominator)
    def __add__(self,other):
        temp_num = (self.__numerator * other.__denominator) + (other.__numerator * self.__denominator)
        temp_den = self.__denominator * other.__denominator
        return "{}/{}".format(temp_num,temp_den)
    def __sub__(self,other):
        temp_num = (self.__numerator * other.__denominator) - (other.__numerator * self.__denominator)
        temp_den = self.__denominator * other.__denominator
        return "{}/{}".format(temp_num,temp_den)
    def __mul__(self,other):
        temp_num = self.__numerator * other.__numerator
        temp_den = self.__denominator * other.__denominator
        return "{}/{}".format(temp_num,temp_den)
    def __truediv__(self,other):
        temp_num = self.__numerator * other.__denominator
        temp_den = self.__denominator * other.__numerator
        return "{}/{}".format(temp_num,temp_den)