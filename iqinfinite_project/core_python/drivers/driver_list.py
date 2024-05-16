import pyfiglet

#list related imports
from list_custom.unique_val import *
from list_custom.list_product_excluding_duplicates import *
from list_custom.extract import *
from list_custom.element_in_range import *
from list_custom.three_consicutive_occurances import *
from list_custom.possible_combo_three_digits import *
from list_custom.possible_combo_with_condition import *
from list_custom.get_unique_combo_two_list import *
from list_custom.remove_occurances import *
from list_custom.replace_index_elements import *

class DriverList:
    def driver_list(self):
        for i in range (0,9999):
            list_welcome_message = """
            \033[95m
**             **  ************  *****************                     
**             **  ************  *****************                     
**             **  **                   **
**             **  **                   **
**             **  ************         **                     
**             **  ************         **                     
**             **            **         **  
**             **            **         **  
*************  **  ************         **                        
*************  **  ************         **                        
\033[97m
         """
            print(list_welcome_message)
            print("""
-----------------------------------------------------------------------------------------
|                                                                                       |
|                              >>> LIST SECTION <<<                                     |
|  1.  How to count unique values inside a list                                         |
|  2.  List product excluding duplicates                                                |
|  3.  Extract elements with Frequency greater than K                                   |
|  4.  Test if List contains elements in Range                                          |
|  5.  Check if the list contains three consecutive common numbers in Python            |
|  6.  Print all Possible Combinations from the three Digits                            |
|  7.  Find all the Combinations in the list with the given condition                   |
|  8.  Get all unique combinations of two lists                                         |
|  9.  Remove all the occurrences of an element from a list in Python                   |
|  10. Replace index elements with elements in Other List                               |
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
            choice_list = input("Enter your choice: ")
            if choice_list =='0':
                T = "Exit"
                ASCII_art_exit = pyfiglet.figlet_format(T,font="doh")
                print(f"\033[91m{ASCII_art_exit}\033[97m")
                break

            elif choice_list == '1':
                print(f"\033[94mOption 1 How to count unique values inside a list\033[97m")
                try:
                    list_size = int(input("Enter the size of the list : "))
                    l = []
                    for i in range(0,list_size):
                        elements = input("Enter elements in the list : ")
                        l.append(elements)
                    uil = UniqueItemsList(l)
                    print(f"Entered List : \033[93m{uil.get_list()}\033[97m")
                    result = uil.get_unique_elements_count()
                    print(f"\033[93mThe unique elements count : {result['unique_element_count']}\033[97m")
                    print(f"\033[93mThe unique elements list : {result['unique_elements_list']}\033[97m")
                except Exception as e:
                    print(f"OOPS ! The Exception caught : {str(e)}")

            elif choice_list == '2':
                print(f"\033[94mOption 2 List product excluding duplicates\033[97m")
                try:
                    list_size = int(input("Enter the size of the list : "))
                    l = []
                    for i in range(0,list_size):
                        elements = int(input("Enter elements in the list : "))
                        l.append(elements)
                    lped = ListProductExcludingDuplicates(l)
                    print(f"Entered List : \033[93m{lped.get_list()}\033[97m")
                    result = lped.list_product_excluding_duplicates()
                    print(f"\033[93mProduct of elements that are unique in the list : {result}\033[97m")
                except Exception as e:
                    print(f"OOPS ! The Exception caught : {str(e)}")

            elif choice_list == '3':
                print(f"\033[94mOption 3 Extract elements with Frequency greater than K\033[97m")
                try:
                    list_size = int(input("Enter the size of the list : "))
                    k = int(input("Enter k : "))
                    l = []
                    for i in range(0,list_size):
                        elements = input("Enter elements : ")
                        l.append(elements)
                    ee = ExtractElements(l)
                    print(f"Entered list : \033[93m{ee.get_list()}\033[97m")
                    result = ee.extract_elements_frequency_greater_than_k(k)
                    print(f"\033[92mExtracted elements : {result}\033[97m")
                except Exception as e:
                    print(f"OOPS ! The Exception caught : {str(e)}")
            
            elif choice_list == '4':
                print(f"\033[94mOption 4 Test if List contains elements in Range\033[97m")
                try: 
                    list_size = int(input("Enter the size of the list : "))
                    l=[]
                    i = int(input("Enter starting element : "))
                    j = int(input("Enter ending element : "))
                    for i in range(0,list_size):
                        elements = int(input("enter the elements in the list : "))
                        l.append(elements)
                    leir = ListElementInRange(l)
                    print(f"Entered list : \033[93m{leir.get_list()}\033[97m")
                    result=leir.list_element_in_range(0,5)
                    print(f"\033[92mElements in range are : {result}\033[97m")
                except Exception as e:
                    print(f"OOPS ! The Exception caught : {str(e)}")

            elif choice_list == '5':
                print("\033[94mOption 5 Check if the list contains three consecutive common numbers in Python\033[97m")
                try: 
                   list_size = int(input("Enter the size of the list : "))
                   l = []
                   for i in range(0,list_size):
                       elements = (input("Enter elements in the list : "))
                       l.append(elements)
                   tco = ThreeConsecutiveOccurances(l)
                   print(f"Entered list : \033[93m{tco.get_list()}\033[97m")
                   result = tco.three_consicutive_occurances()
                   print(f"\033[92mConsecutive number are : {result}\033[97m")
                except Exception as e:
                    print(f"OOPS ! The Exception caught : {str(e)}")
            
            elif choice_list == '6':
                print("\033[94mOption 6 Print all Possible Combinations from the three Digits\033[97m")
                try:
                    print("Enter 3 digits")
                    l = []
                    for i in range(0,3):
                        elements = int(input("Enter digits in the list : "))
                        l.append(elements)
                    pctd = PossibleComboThreeDigits(l)
                    print(f"Entered list : \033[93m{pctd.get_list()}\033[97m")
                    result = pctd.possible_combo()
                    print("\033[92mPossible combinations of digits\033[97m")
                    for i in result : 
                        print(f"\033[92m{i}\033[97m")
                except Exception as e:
                    print(f"OOPS ! The Exception caught : {str(e)}")

            elif choice_list == '7':
                print("\033[94mOption 7 Find all the Combinations in the list with the given condition\033[97m")
                '''
                ["GFG", [5, 4], "is",
                ["best", "good", "better", "average"]]
                '''
                try:
                    l = []
                    size_of_list = int(input("Enter the size of the list : "))
                    for i in range(0,size_of_list):
                        elements = (input("Enter digits in the list : "))
                        l.append(elements)
                    cwc = CombinationWithConditions(l)
                    print(f"The entered list is : \033[93m{cwc.get_list()}\033[94m")
                    print("\033[92mAll possible combinations are as follows : \033[97m")
                    cwc.combination_with_list()
                except Exception as e:
                    print(f"OOPS ! The Exception caught : {str(e)}")

            elif choice_list == '8':
                print("\033[94mOption 8 Get all unique combinations of two lists\033[97m")
                try:
                    l_one = []
                    l_two = []
                    size_of_list_one = int(input("Enter the size of list one : "))
                    size_of_list_two = int(input("Enter the size of list two : "))
                    print("Enter elements in list one : ")
                    for i in range(0,size_of_list_one):
                        elements = (input("Enter elements : "))
                        l_one.append(elements)
                    print("Enter elements in list two : ")
                    for j in range(0,size_of_list_two):
                        elements = (input("Enter elements : "))
                        l_two.append(elements)
                    guctl = GetUniqueCombinationTwoList(l_one, l_two)
                    print(f"Entered list [LIST ONE] : \033[93m{guctl.get_list_one()}\033[97m")       
                    print(f"Entered list [LIST TWO] : \033[93m{guctl.get_list_two()}\033[97m")
                    result = guctl.get_unique_combination_two_list()
                    print(f"\033[92mPrint the unique combinations : {result}\033[97m")
                except Exception as e:
                    print(f"OOPS ! The Exception caught : {str(e)}")
            
            elif choice_list == '9':
                print("\033[94mOption 9 Remove all the occurrences of an element from a list in Python\033[97m")
                try:
                    l=[]
                    size_of_list = int(input("Enter the elements in the array : "))
                    for i in range(0,size_of_list):
                        elements = int(input("Enter elements : "))
                        l.append(elements)
                    raoil = RemoveAllOccurancesInList(l)
                    print(f"Entered list : \033[93m{raoil.get_list()}\033[94m")
                    ele = int(input("Enter the element to be removed from the list : "))
                    result = raoil.remove_all_occurances_in_list(ele)
                    print(f"\033[92mResult after removed occurances from the list : {result}\033[97m")
                except Exception as e:
                    print(f"OOPS ! The Exception caught : {str(e)}")
            
            elif choice_list == '10':
                print(f"\033[94mOption 10 Replace index elements with elements in Other List\033[97m")   
                try:            
                    l_two = []
                    # list_one_size = int(input("Enter the size of list one : "))
                    list_two_size = int(input("Enter the size of list two : "))
                    string_var = str(input("Enter the string : "))
                    print("Enter elements in list two : ")
                    for j in range(0,list_two_size):
                        element = int(input("Enter elements : "))
                        l_two.append(element)
                    rewole = ReplaceIndexElementsWithOtherListElement(string_var,l_two)
                    print(f"Entered list one : \033[93m{rewole.get_string()}\033[97m")
                    print(f"Entered list two : \033[93m{rewole.get_list_two()}\033[97m")
                    result = rewole.replace_index_element()
                    print(f"\033[92m\033Replaced index elements : {result}\033[97m")
                except Exception as e:
                    print(f"OOPS ! The Exception caught : {str(e)}") 
                
            else:
                print("\033[91m!!! Wrong choice !!!\033[97m")
                print("\n")