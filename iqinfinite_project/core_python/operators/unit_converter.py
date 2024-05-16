# Unit converter 
'''
Unit converter : 
1. Length
2. Area
3. Power
4. weight
'''
# Unit converter : Solution
import pyfiglet
class UnitConverter:
    def __init__(self,var_number=0,ch="",inner_ch = ""):
        self.__var_number = var_number
        self.__choice = ch
        self.__inner_ch = inner_ch

    # getter and setter for var_num1
    def get_var_num1(self):
        return self.__var_number
    def set_var_num1(self,var_num):
        self.__var_number = var_num
    
    # getter and setter for outer menu choice
    def get_var_choice(self):
        return self.__choice
    def set_var_choice(self,choice):
        self.__choice = choice

    # getter and setter for inner menu choice
    def get_var_inner_choice(self):
        return self.__inner_ch
    def set_var_inner_choice(self,choice):
        self.__inner_ch = choice

    def menu(self):
        menu_msg = """
-----------------------------------------------------------------------------------------
|                                                                                       |
|                               >>>  UNIT CONVERTER  <<<                                |
|  1.  Length                                                                           |
|      1.  Km to meters                                                                 |
|      2.  inch to cm                                                                   |
|      3.  mm to cm                                                                     |
|      4.  miles to km                                                                  |
|  2.  Power                                                                            |
|      1.  HP to kwh                                                                    |
|      2.  kwh to hp                                                                    |
|  3.  Weight                                                                           |
|      1.  kg to pound                                                                  |
|      2.  gram to ounce                                                                |
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

    def __inner_weight_menu(self):
        menu_msg = """
-----------------------------------------------------------------------------------------
|                                                                                       |
|                               >>>      WEIGHT      <<<                                |

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
        a = self.__var_number
        ch = self.__choice # for outer menu
        inner_ch = self.__inner_ch
        '''
        Length
        '''
        if ch == 1: 
            if inner_ch == 1:
                print(f"\033[94mKm to meters\033[97m")
                r = a * 1000
                return r
            elif inner_ch == 2:
                print(f"\033[94minch to cm\033[97m")
                r = a * 2.54
                return r
            elif inner_ch == 3:
                print(f"\033[94mmm to cm\033[97m")
                r = a * 0.1
                return r
            elif inner_ch == 4:
                print(f"\033[94mmiles to km\033[97m")
                r = a * 1.609344
                return r
            else:
                print(f"\033[91m!!! Wrong choice !!!\033[97m")

        elif ch == 2: 
            if inner_ch == 1:
                print(f"\033[94mHP to kwh\033[97m")
                r = a * 0.7457
                return r
            elif inner_ch == 2:
                print(f"\033[94mkwh to hp\033[97m")
                r = a * 1.34
                return r
            else:
                print(f"\033[91m!!! Wrong choice !!!\033[97m")

        elif ch == 3:
            if inner_ch == 1:
                print(f"\033[94mkg to pound\033[97m")
                return a * 2.2
            elif inner_ch == 2:
                print(f"\033[94mgram to ounce\033[97m")
                return a * 0.035274
            else:
                print(f"\033[91m!!! Wrong choice !!!\033[97m")
                