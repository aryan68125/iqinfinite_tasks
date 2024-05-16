import pyfiglet
# operators related imports
from operators.calculator import *
from operators.fraction_calculator import *

class DriverOperator:
    def driver_operator(self):
        for i in range (0,9999):
            T = "operator"
            ASCII_art_1 = pyfiglet.figlet_format(T,font="doh")
            print(f"\033[95m{ASCII_art_1}\033[97m")
            print("""
-----------------------------------------------------------------------------------------
|                                                                                       |
|                               >>> OPERATOR SECTION <<<                                |
|  1.  Calculator                                                                       |
|  2.  Fraction Calculator                                                              |
|                                                                                       |
-----------------------------------------------------------------------------------------

               \033[91m
-----------------------------------------------------------------------------------------
|                                                                                       |
|                              >>> TYPE 0 TO EXIT <<<                                   |
|                                                                                       |
-----------------------------------------------------------------------------------------
               \033[97m
            """)
            choice_sets = input("Enter your choice: ")
            if choice_sets =='0':
                T = "Exit"
                ASCII_art_exit = pyfiglet.figlet_format(T,font="doh")
                print(f"\033[91m{ASCII_art_exit}\033[97m")
                break

            elif choice_sets == '1':
                print(f"\033[94mOption 1 Calculator\033[97m")
                c = Calculator()
                for i in range(0,9999):
                    ch = input("Enter 'y' to continue : ")
                    if ch.lower() == 'y':
                        c.menu()
                        num1 = float(input("Enter first number : "))
                        operator = input("Enter the operator : ")
                        num2 = float(input("Enter second number : "))
                        c.set_var_num1(num1)
                        c.set_var_operator(operator)
                        c.set_var_num2(num2)
                        result = c.calculate()
                        print(f"\033[93m{c.get_var_num1()} {c.get_var_operator()} {c.get_var_num2()}\033[97m = \033[92m{result}\033[97m")
                    else:
                        print ("\033[91m!!! Program Terminated !!!\033[97m")
                        break

            elif choice_sets == '2':
                print(f"\033[94mOption 2 Fraction Calculator\033[97m")
                fc = FractionCalculator()
                for i in range(0,9999):
                    ch = input("Enter 'y' to continue : ")
                    if ch.lower() == 'y':
                        fc.menu()
                        print("Enter the numerators and denominators for the \033[95mfirst fraction\033[97m")
                        numerator1 = int(input("Enter numerator : "))
                        denominator1 = int(input("Enter denominator : "))
                        fc.set_fraction_1(numerator1,denominator1)
                        operator = input("Enter the operator : ")
                        fc.set_var_operator(operator)
                        print("Enter the numerators and denominators for the \033[95msecond fraction\033[97m")
                        numerator2 = int(input("Enter numerator : "))
                        denominator2 = int(input("Enter denominator : "))
                        fc.set_fraction_2(numerator2,denominator2)
                        result = fc.calculate()
                        print(f"\033[93m{fc.get_fraction_1()} {fc.get_var_operator()} {fc.get_fraction_2()}\033[97m = \033[92m{result}\033[97m")
                    else:
                        print ("\033[91m!!! Program Terminated !!!\033[97m")
                        break

            else:
                print("\033[91m!!! Wrong choice !!!\033[97m")
                print("\n")