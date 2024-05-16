import pyfiglet

#imports related to loops
from loop.patterns import *
from loop.summision import *
from loop.times_table import *
from loop.extract_num_list import *
from loop.count_digits import *
from loop.reverse_list import *
from loop.display_negative_10_to_negative_1 import *

class DriverLoops:
    def driver_loops(self):
        for i in range (0,9999):
            T = "loops"
            ASCII_art_1 = pyfiglet.figlet_format(T,font="doh")
            print(f"\033[95m{ASCII_art_1}\033[97m")
            print("""
-----------------------------------------------------------------------------------------
|                                                                                       |
|                               >>> LOOP SECTION <<<                                    |
|  1.  Print Left right angle triangle                                                  |
|  2.  Print Left right angle triangle                                                  |
|  3.  Print Full pyramid triangle                                                      |
|  4.  Print Inverted Full pyramid triangle                                             |
|  5.  Sumission of numbers in a number series                                          |
|  6.  Times Table                                                                      |
|  7.  Extract numbers from list                                                        |
|  8.  Count digits in a number                                                         |
|  9.  Print elements in a list in reverse order                                        |
|  10. Display numbers from -10 to -1 using for loop                                    |
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
            choice_loops = input("Enter your choice: ")
            if choice_loops =='0':
                T = "Exit"
                ASCII_art_exit = pyfiglet.figlet_format(T,font="doh")
                print(f"\033[91m{ASCII_art_exit}\033[97m")
                break

            elif choice_loops == '1':
                print(f"\033[94mOption 1 Print Left right angle triangle\033[97m")
                size = int(input("Enter number of rows : "))
                p = Pattern(size)
                print(f"Entered number of rows : \033[93m{p.get_rows()}\033[97m")
                print(f"\033[92mResult : \033[97m")
                p.left_right_angle_triangle()

            elif choice_loops == '2':
                print(f"\033[94mOption 2 Print Right right angle triangle\033[97m")
                size = int(input("Enter number of rows : "))
                p = Pattern(size)
                print(f"Entered number of rows : \033[93m{p.get_rows()}\033[97m")
                print(f"\033[92mResult : \033[97m")
                p.right_right_angle_triangle()

            elif choice_loops == '3':
                print(f"\033[94mOption 3 Print Full pyramid triangle\033[97m")
                size = int(input("Enter number of rows : "))
                p = Pattern(size)
                print(f"Entered number of rows : \033[93m{p.get_rows()}\033[97m")
                print(f"\033[92mResult : \033[97m")
                p.full_pyramid()

            elif choice_loops == '4':
                print(f"\033[94mOption 4 Print Inverted Full pyramid triangle\033[97m")
                size = int(input("Enter number of rows : "))
                p = Pattern(size)
                print(f"Entered number of rows : \033[93m{p.get_rows()}\033[97m")
                print(f"\033[92mResult : \033[97m")
                p.inverted_full_pyramid()

            elif choice_loops == '5':
                print(f"\033[94mOption 5 Sumission of numbers in a number series\033[97m")                
                size = int(input("Enter last number : "))
                s = Sumission(size)
                print(f"Entered last number : \033[93m{s.get_last_number()}\033[97m")
                result = s.sumission()
                print(f"\033[92mSumission : {result}\033[97m")

            elif choice_loops == '6':
                print(f"\033[94mOption 6 Times Table\033[97m") 
                number = int(input("Enter the number : "))
                size = int(input("Enter the size of the table : "))
                tt = TimesTable(number,size)
                print(f"Entered last number : \033[93m{tt.get_number()}\033[97m")
                print(f"Entered last number : \033[93m{tt.get_size()}\033[97m") 
                tt.times_table()               

            elif choice_loops == '7':
                print(f"\033[94mOption 7 Extract numbers from list\033[97m") 
                '''numbers = [12, 75, 150, 180, 145, 525, 50]'''
                size = int(input("Enter the size of the list : "))
                numbers=[]
                print("Enter elements in the list :")
                for i in range(0,size):
                    elements = int(input("Enter elements : "))
                    numbers.append(elements)
                enfl = ExtractNumberFromList(numbers)
                print(f"Entered list : \033[93m{enfl.get_list()}\033[97m")
                print(f"\033[92mExtracted numbers : \033[97m")   
                enfl.extract()

            elif choice_loops == '8':
                print(f"\033[94mOption 8 Count digits in a number\033[97m")    
                '''For example, the number is 75869, so the output should be 5.'''                          
                number = int(input("Enter number : "))
                cd = CountDigits(number)
                print(f"Entered number : \033[93m{cd.get_number()}\033[97m") 
                result = cd.get_digits_count()
                print(f"\033[92mNumber of digits in a number is : {result}\033[97m")                

            elif choice_loops == '9':
                print(f"\033[94mOption 9 Print elements in a list in reverse order\033[97m") 
                size = int(input("Enter the size of the list : "))
                l = []
                print("Enter elements in the list : ")
                for i in range(0,size):
                    elements = input("Enter elements : ")
                    l.append(elements)
                rl = ReverseList(l)
                print(f"Entered number : \033[93m{rl.get_list()}\033[97m") 
                print(f"\033[92mPrinting elements of the list in reverse : \033[97m")  
                rl.revserse_list()             

            elif choice_loops == '10':
                print(f"\033[94mOption 10 Display numbers from -10 to -1 using for loop\033[97m") 
                dnttno = DisplayNegativeTenToNegativeOne()
                print("\033[92mPrinting elements from -10 to -1 : \033[97m")
                dnttno.display_negative_ten_to_negative_one()
                
            else:
                print("\033[91m!!! Wrong choice !!!\033[97m")
                print("\n")