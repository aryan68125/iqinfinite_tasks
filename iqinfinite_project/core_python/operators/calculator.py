# Calculator teminal application to demonstrate uses of operators
'''
demonstration of 
 uses of decimals and integer numbers
 + --> Addition
 - --> Subtraction
 * --> Multiplication
 / --> Division
 // --> Floor division
'''
# Calculator teminal application to demonstrate uses of operators : Solution
class Calculator:
    def __init__(self,var_num1=0,var_num2=0,operator=''):
        self.__var_num1 = var_num1
        self.__var_num2 = var_num2
        self.__operator = operator
    # getter and setter for var_num1
    def get_var_num1(self):
        return self.__var_num1
    def set_var_num1(self,var_num1):
        self.__var_num1 = var_num1
    
    #getter and setter for var_num2
    def get_var_num2(self):
        return self.__var_num2
    def set_var_num2(self,var_num2):
        self.__var_num2 = var_num2
    
    # getter and setter for operator
    def get_var_operator(self):
        return self.__operator
    def set_var_operator(self,operator):
        self.__operator = operator

    def menu(self):
        menu_msg = """
-----------------------------------------------------------------------------------------
|                                                                                       |
|                               >>>    CALCULATOR    <<<                                |
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
        a = self.__var_num1
        b = self.__var_num2
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
        elif operator == '//':
            print("""
                  \033[95m
Explaination of floor division using an example : 
Example:
10 // 3 = 3
Here, the quotient is 3.33, but since we are using floor division, the result is rounded down to the nearest integer, 3. 
                  \033[97m
            """)
            if not b == 0:
                return a//b
            else:
                print("\033[91m!!! Divide by zero error !!!\033[97m")