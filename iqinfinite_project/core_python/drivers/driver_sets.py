import pyfiglet
#sets related imports
from sets.size_of_sets import *
from sets.iterate_sets import *
from sets.max_min_sets import *
from sets.remove_items_sets import *
from sets.common_elements import *
from sets.convert import  *
from sets.common_elements_in_three_list import *
from sets.difference_between_two_lists import *

class DriverSets:
    def driver_sets(self):
        for i in range (0,9999):
            T = "sets"
            ASCII_art_1 = pyfiglet.figlet_format(T,font="doh")
            print(f"\033[95m{ASCII_art_1}\033[97m")
            print("""
-----------------------------------------------------------------------------------------
|                                                                                       |
|                               >>> SETS SECTION <<<                                    |
|  1.  Find the size of a Set in Python                                                 |
|  2.  Iterate over a set in Python                                                     |
|  3.  Maximum and Minimum in a Set                                                     |
|  4.  Remove items from Set                                                            |
|  5.  Check if two lists have at-least one element common                              |
|  6.  Convert sets into tuples                                                         |
|  7.  Convert set into a list                                                          |
|  8.  Convert set into a string                                                        |
|  9.  Find common elements in three lists using sets                                   |
|  10. Difference between two lists                                                     |
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
                print(f"\033[94mOption 1 Find the size of a Set in Python\033[97m")
                size = int(input("Enter the size of the set: "))
                my_set = set()
                print("Enter the elements of the set:")
                for i in range(size):
                    element = input("Element {}: ".format(i+1))
                    my_set.add(element)
                '''
                Set1 = {"A", 1, "B", 2, "C", 3}
                Set2 = {"Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu"}
                Set3 = {(1, "Lion"), ( 2, "Tiger"), (3, "Fox")}
                '''
                sos = SizeOfSets(my_set)
                print(f"Entered sets : \033[93m{sos.get_sets()}\033[97m")
                result = sos.get_size()
                print(f"\033[92mSize of the sets : {str(result)}\033[97m")

            elif choice_sets == '2':
                print(f"\033[94mOption 2 Iterate over a set in Python\033[97m")
                var_strings = input("Enter the string : ")
                ise = IterateSetsElements(var_strings)
                print(f"Entered strings : \033[93m{ise.get_strings()}\033[97m")
                print(f"\033[92mElements of the sets : \033[97m")  
                print(f"\033[92m{ise.interate_sets_elements()}\033[97m")           

            elif choice_sets == '3':
                print(f"\033[94mOption 3 Maximum and Minimum in a Set\033[97m")
                size = int(input("Enter the size of the set: "))
                my_set = set()
                print("Enter the elements of the set:")
                for i in range(size-1):
                    element = input("Element {}: ".format(i+1))
                    my_set.add(element)
                mes = MaxElementsSets(my_set)
                print(f"Entered set : \033[93m{mes.get_sets()}\033[97m")
                var_max = mes.max_element()
                print(f"\033[92mMaximum element in the set : {var_max}\033[97m")
                var_min = mes.min_element()
                print(f"\033[92mMinimum element in the set : {var_min}\033[97m")

            elif choice_sets == '4':
                print(f"\033[94mOption 4 Remove items from Set\033[97m")
                size = int(input("Enter the size of the set: "))
                my_set = set()
                print("Enter the elements of the set:")
                for i in range(size):
                    element = input("Element {}: ".format(i+1))
                    my_set.add(element)
                ris = RemoveItemsSets(my_set)
                print(f"Entered set : \033[93m{ris.get_sets()}\033[97m")
                print(f"\033[92mRemoved items fom the sets : \033[97m")
                print(f"\033[92m{ris.remove_element()}\033[97m")

            elif choice_sets == '5':
                print(f"\033[94mOption 5 Check if two lists have at-least one element common\033[97m")
                size_one = int(input("Enter the size of the set one: "))
                my_set_one = set()
                print("Enter the elements of the set one:")
                for i in range(size_one):
                    element_one = input("Element {}: ".format(i+1))
                    my_set_one.add(element_one)
                size_two = int(input("Enter the size of the set one: "))
                my_set_two = set()
                print("Enter the elements of the set two:")
                for i in range(size_two):
                    element_two = input("Element {}: ".format(i+1))
                    my_set_two.add(element_two)
                aloce = AtLeastOneCommonElements(my_set_one,my_set_two)
                print(f"Entered set : \033[93m{aloce.get_list_one()}\033[97m")
                print(f"Entered set : \033[93m{aloce.get_list_two()}\033[97m")
                result = aloce.at_least_common_elements()
                print(f"\033[92mTwo sets atleast have one common elements in the sets : {result}\033[97m")
            
            elif choice_sets == '6':
                print(f"\033[94mOption 6 Convert sets into tuples\033[97m")
                size = int(input("Enter the size of the set: "))
                my_set = set()
                print("Enter the elements of the set:")
                for i in range(size):
                    element = input("Element {}: ".format(i+1))
                    my_set.add(element)
                c = Convert(my_set)
                print(f"Entered set : \033[93m{c.get_sets()}\033[97m")
                print(f"Printing the Type : \033[93m{type(c.get_sets())}\033[97m")
                result = c.convert_sets()
                print(f"\033[92mConvert sets into tuples : {result}\033[97m") 
                print(f"\033[92mPrinting the Type : \033[93m{type(result)}\033[97m")          

            elif choice_sets == '7':
                print(f"\033[94mOption 7 Convert set into a list\033[97m")    
                size = int(input("Enter the size of the set: "))
                my_set = set()
                print("Enter the elements of the set:")
                for i in range(size):
                    element = input("Element {}: ".format(i+1))
                    my_set.add(element)              
                c = Convert(my_set)
                print(f"Entered set : \033[93m{c.get_sets()}\033[97m")
                print(f"Printing the Type : \033[93m{type(c.get_sets())}\033[97m")
                result = c.convert_list()
                print(f"\033[92mConvert sets into list : {result}\033[97m") 
                print(f"\033[92mPrinting the Type : \033[93m{type(result)}\033[97m")          

            elif choice_sets == '8':
                print(f"\033[94mOption 8 Convert set into a string\033[97m")    
                size = int(input("Enter the size of the set: "))
                my_set = set()
                print("Enter the elements of the set:")
                for i in range(size):
                    element = input("Element {}: ".format(i+1))
                    my_set.add(element)              
                c = Convert(my_set)
                print(f"Entered set : \033[93m{c.get_sets()}\033[97m")
                print(f"Printing the Type : \033[93m{type(c.get_sets())}\033[97m")
                result = c.convert_string()
                print(f"\033[92mConvert sets into string : {result}\033[97m") 
                print(f"\033[92mPrinting the Type : \033[93m{type(result)}\033[97m")   

            elif choice_sets == '9':
                print(f"\033[94mOption 9 Find common elements in three lists using sets\033[97m")    
                l_one = []
                l_two = []
                l_three = []
                size_of_list_one = int(input("Enter the size of list one : "))
                size_of_list_two = int(input("Enter the size of list two : "))
                size_of_list_three = int(input("Enter the size of list three : "))
                print("Enter elements in list one : ")
                for i in range(0,size_of_list_one):
                    elements = (input("Enter elements : "))
                    l_one.append(elements)
                print("Enter elements in list two : ")
                for j in range(0,size_of_list_two):
                    elements = (input("Enter elements : "))
                    l_two.append(elements)
                print("Enter elements in list three : ")
                for k in range(0,size_of_list_three):
                    elements = (input("Enter elements : "))
                    l_three.append(elements)  
                citl = CommonInThreeList(l_one,l_two,l_three)
                print(f"Entered list one : \033[93m{citl.get_list_1()}\033[97m")
                print(f"Entered list two : \033[93m{citl.get_list_2()}\033[97m")
                print(f"Entered list three : \033[93m{citl.get_list_3()}\033[97m")
                result = citl.find_common_in_three_list()
                print(f"\033[92mCommon Elements : {result}\033[97m") 
            
            elif choice_sets == '10':
                print(f"\033[94mOption 10 Difference between two lists\033[97m")
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
                dbtl = DifferenceBetweenTwoLists(l_one,l_two)
                print(f"Entered list one : \033[93m{dbtl.get_list_1()}\033[97m")
                print(f"Entered list two : \033[93m{dbtl.get_list_2()}\033[97m")
                result = dbtl.difference_between_two_lists()
                print(f"\033[92mDifferent Elements in the two lists from list one : {result}\033[97m") 

            else:
                print("\033[91m!!! Wrong choice !!!\033[97m")
                print("\n")