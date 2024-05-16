'''
this class will inherit all the functionalities 
This class accepts fraction object and will return a fraction object as a result
'''
from .fraction import Fraction_class
class FractionCalculator:
    
    def __init__(self,var_numerator1=0,var_denominator1=0,var_numerator2=0,var_denominator2=0):
        self.__var_fraction1 = Fraction_class(var_numerator1,var_denominator1)
        self.__var_fraction2 = Fraction_class(var_numerator2,var_denominator2)
    
    #getter and setter for fraction_1
    def get_fraction_1(self):
        return self.__var_fraction1
    def set_fraction_1(self,var_numerator1,var_denominator1):
        self.__var_fraction1 = Fraction_class(var_numerator1,var_denominator1)

    #getter and setter for fraction 2
    def get_fraction_2(self):
        return self.__var_fraction2
    def set_fraction_2(self,var_numerator2,var_denominator2):
        self.__var_fraction2 = Fraction_class(var_numerator2,var_denominator2)

    # getter and setter for operator
    def get_var_operator(self):
        return self.__operator
    def set_var_operator(self,operator):
        self.__operator = operator
    
    def menu(self):
        menu_msg = """
-----------------------------------------------------------------------------------------
|                                                                                       |
|                               >>>FRACTION CALCULATOR<<<                               |
|  1.  + --> Addition                                                                   |
|  2.  - --> Subtraction                                                                |
|  3.  * --> Multiplication                                                             |
|  4.  / --> Division                                                                   |
|                                                                                       |
-----------------------------------------------------------------------------------------

               \033[91m
-----------------------------------------------------------------------------------------
|                                                                                       |
|                              >>> TYPE 0 TO EXIT <<<                                   |
|                                                                                       |
-----------------------------------------------------------------------------------------
               \033[97m
        """
        print(menu_msg)

    def calculate(self):
        a = self.__var_fraction1
        b = self.__var_fraction2
        operator = self.__operator
        if operator == '+':
            return a+b
        elif operator == '-':
            return a-b
        elif operator == '*':
            return a*b
        elif operator == '/':
            if not b == 0:
                return a/b
            else:
                print("\033[91m!!! Divide by zero error !!!\033[97m")