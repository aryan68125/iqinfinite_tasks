import pyfiglet
from tuples.size_of_tuple import *
from tuples.tuples_div_by_k import *
import sys
from tuples.flattern_tuples import *
from tuples.extract_digits import *
from tuples.remove_duplicate_tuples import *
from tuples.remove_duplicate_elements import *
from tuples.extract_positive_tuples import *
from tuples.flatten_to_string import *
from tuples.tuples_occurances import *
from tuples.sort_tuples_alpha import *

class DriverTuples:
    def driver_tuples(self):
        for i in range (0,9999):
            tuples_welcome_message = """
            \033[95m
********************   **         **   *************   **              *************   ************                     
********************   **         **   *************   **              *************   ************                     
         **            **         **   **         **   **              **              **          
         **            **         **   **         **   **              **              **          
         **            **         **   *************   **              *************   ************                     
         **            **         **   *************   **              *************   ************                     
         **            **         **   **              **              **                        **  
         **            **         **   **              **              **                        **  
         **            *************   **              *************   *************   ************                        
         **            *************   **              *************   *************   ************                        
\033[97m
         """
            print(tuples_welcome_message)
            print("""
-----------------------------------------------------------------------------------------
|                                                                                       |
|                         >>> TUPLES SECTION <<<                                        |
|  1.  Get size of a tuple                                                              |
|  2.  Find tuples which have all elements divisible by K from a list of tuples         |
|  3.  Flatten tuple of List to tuple                                                   |
|  4.  Extract digits from tuples list                                                  |
|  5.  Remove duplicate lists in tuples (Preserving Order)                              |
|  6.  Removing duplicate elements from tuple                                           |
|  7.  Python program to find Tuples with positive elements in List of tuples           |
|  8.  Flatten Tuples List to String                                                    |
|  9.  Count tuples occurrence in list of tuples                                        |
|  10. Sort a list of tuples alphabetically                                             |
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
            choice_tuples = input("Enter your choice: ")
            if choice_tuples =='0':
                T = "Exit"
                ASCII_art_exit = pyfiglet.figlet_format(T,font="doh")
                print(f"\033[91m{ASCII_art_exit}\033[97m")
                break

            elif choice_tuples == '1':
                print("\033[94mOption 1 Get size of a tuple\033[97m ")
                try:
                    word = input("Enter the string :")
                    ts = TupleSize(word)
                    print(f"the entered string : \033[93m{ts.get_word()}\033[97m")
                    try:
                        result = ts.get_size_of_tuple()
                        print(f"\033[96mConverted string into a list :\n {result['w_list']}\033[97m")
                        print(f"\033[96mConverted list into a tuple :\n {result['w_tuple']}\033[97m")
                        print(f"\033[92mSize of tuples : {result['size_in_bytes']}\033[97m")
                    except Exception as e:
                        print(f"\033[91m!!! {str(e)} !!!\033[97m")
                    print('\n')
                except Exception as e:
                    print(f"OOPS ! The Exception caught : {str(e)}")

            elif choice_tuples == '2':
                print("\033[94mOption 2 Find tuples which have all elements divisible by K from a list of tuples\033[97m ")
                try:
                    size_of_list = input("Enter the number of tuples :")
                    size_of_tuples = input("Enter the size of all the tuples :")
                    divided_by = input("Enter the number that divides the tuple's elements :")
                    tdbk = TuplesDividedByK(size_of_list,size_of_tuples,divided_by)
                    print(f"number of tuples : \033[93m{tdbk.get_number_of_tuples()}\033[97m")
                    print(f"number of elements in tuples : \033[93m{tdbk.get_size_of_a_tuple()}\033[97m")
                    result = tdbk.divisible_by_k()
                    print(f"\033[93mNumber of tuples :\n {result['list_size']}\033[97m")
                    print(f"\033[93mNumber of elements in tuples :\n {result['tuple_size']}\033[97m")
                    print(f"\033[93mThe number that divides the tuple's elements : {result['divided_by']}\033[97m")
                    print(f"\033[93mList of tuples : {result['outer_list']}\033[97m")
                    print(f"\033[92mTuples Divided by the number \033[93m{result['divided_by']}\033[92m : {result['res']}\033[97m")
                    print('\n')
                except Exception as e:
                    print(f"OOPS ! The Exception caught : {str(e)}")
            
            elif choice_tuples == '3':
                print("\033[94mOption 3 Flatten tuple of List to tuple\033[97m ")
                '''
                Insert tuple of lists
                '''
                try:
                    size_of_tuple = int(input("Enter the size of the tuple : ")) # number of lists
                    size_of_list = int(input("Enter the size of the list : "))
    
                    temp_outer_list = []
                    for list_number in range(0,size_of_tuple):
                        print(f"List number = {list_number}")
                        inner_list = []
                        for i in range(0,size_of_list):
                            elements = int(input(f"Enter elements in list {list_number} "))
                            inner_list.append(elements)
                        temp_outer_list.append(inner_list)
                    print(temp_outer_list)
                    tuple_var = tuple(temp_outer_list)
                    print(f"The entered tuple of lists is : \033[93m{tuple_var}\033[97m")
                    flat = FlattenTuple(tuple_var)
                    result = flat.flatten_tuple()
                    print(f"\033[92mFlatten Tuple = {result}\033[97m")
                except Exception as e:
                    print(f"OOPS ! The Exception caught : {str(e)}")
            
            elif choice_tuples == '4':
                print("\033[94mOption 4 Extract digits from tuples list\033[97m")
                try:
                    outer_list = []
                    outer_list_size = int(input("Enter the size of the list : "))
                    inner_list_size = int(input("Enter the size of the tuples : "))
                    for inner_list_number in range(0,outer_list_size):
                        inner_list = []
                        print(f"Enter elements in List number {inner_list_number}")
                        for elements in range(0,inner_list_size):
                            elements = input("enter elements : ")
                            inner_list.append(elements)
                        var_tuple = tuple(inner_list)
                        outer_list.append(var_tuple)
                    exd = ExtractDigits(outer_list)
                    print(f"The entered list of tuples : \033[93m{exd.get_list_of_tuples()}\033[97m")
                    result = exd.extract()
                    print(f"\033[92mExtracted digits : {result}\033[97m")
                except Exception as e:
                    print(f"OOPS ! The Exception caught : {str(e)}")
            
            elif choice_tuples == '5':
                print("\033[94mOption 5 Remove duplicate lists in tuples (Preserving Order)\033[97m")
                try:
                    outer_list_size = int(input("Enter the size of the tuple : "))
                    inner_list_size = int(input("Enter the size of the list : "))
                    outer_list = []
                    for inner_list_number in range(0,outer_list_size):
                        inner_list = []
                        print(f"Enter elements in list {inner_list_number}")
                        for elements in range(0,inner_list_size):
                            elements = input("Enter elements : ")
                            inner_list.append(elements)
                        outer_list.append(inner_list)
                    var_tuple = tuple(outer_list)
                    rd = RemoveDuplicateTuples(var_tuple)
                    print(f"The entered tuple is : \033[93m{rd.get_tuple()}\033[97m")
                    result = rd.remove_duplicates()
                    print(f"\033[92mRemoved Duplicated tuples : {result}\033[97m")
                except Exception as e:
                    print(f"OOPS ! The Exception caught : {str(e)}")

            elif choice_tuples == '6':
                print("\033[94mOption 6 Removing duplicate elements from tuple\033[97m")
                try:
                    outer_list_size = int(input("Enter the size of the tuple : "))
                    outer_list = []
                    for i in range(0,outer_list_size):
                        elements = input("Enter elements : ")
                        outer_list.append(elements)
                    var_tuple = tuple(outer_list)
                    dupele = RemoveDuplicateElements(var_tuple)
                    print(f"Entered tuples : \033[93m{dupele.get_tuple()}\033[97m")
                    result = dupele.remove_duplicate_elements()
                    print(f"\033[92mRemoved duplicate elements : {result}\033[97m")
                except Exception as e:
                    print(f"OOPS ! The Exception caught : {str(e)}")

            elif choice_tuples == '7':
                print("\033[94mOption 7 Python program to find Tuples with positive elements in List of tuples\033[97m")
                try:
                    # [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, -6)] 
                    outer_list_size = int(input("Enter the size of the list : "))
                    inner_list_size = int(input("Enter the size of the tuple : "))
                    outer_list = []
                    for num_of_tuples in range(0,outer_list_size):
                        inner_list = []
                        print(f"tuple {num_of_tuples}")
                        for num_of_elements in range(0,inner_list_size):
                            elements = int(input("Enter the elements : "))
                            inner_list.append(elements)
                        outer_list.append(tuple(inner_list))
                    expt = ExtractPositiveTuples(outer_list)
                    print(f"Entered list of tuples : \033[93m{expt.get_list()}\033[97m")
                    result = expt.extract_positive_tuples()
                    print(f"\033[92mThe positive tuples : {result}\033[97m")
                except Exception as e:
                    print(f"OOPS ! The Exception caught : {str(e)}")

            elif choice_tuples == '8':
                print("\033[94mOption 8 Flatten Tuples List to String\033[97m")
                try:
                    # [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, -6)] 
                    outer_list_size = int(input("Enter the size of the list : "))
                    inner_list_size = int(input("Enter the size of the tuple : "))
                    outer_list = []
                    for num_of_tuples in range(0,outer_list_size):
                        inner_list = []
                        print(f"tuple {num_of_tuples}")
                        for num_of_elements in range(0,inner_list_size):
                            elements = str(input("Enter the elements : "))
                            inner_list.append(elements)
                        outer_list.append(tuple(inner_list))
                    fts = FlattenTuplesToString(outer_list)
                    print(f"Entered list of tuples : \033[93m{fts.get_list()}\033[97m")
                    result = fts.flatten_tuples_to_strings()
                    print(f"\033[92mFlatten tuples into a list : {result}\033[97m")
                except Exception as e:
                    print(f"OOPS ! The Exception caught : {str(e)}")

            elif choice_tuples == '9':
                print("\033[94mOption 9 Count tuples occurrence in list of tuples\033[97m")
                '''
                [[('hi', 'bye')], [('Geeks', 'forGeeks')], [('a', 'b')], [('hi', 'bye')], [('a', 'b')]]
                '''
                try:
                    outer_list_size = int(input("Enter number of lists : "))
                    size_of_tuples = int(input("Enter the size of the tuples : "))
                    outer_list = []
                    for i in range(0,outer_list_size):
                        print(f" list number : {i}")
                        tuple_list = []
                        inner_list = []
                        for j in range(0, size_of_tuples):
                            elements = int(input("Enter the elements : "))
                            tuple_list.append(elements)
                        var_tuple = tuple(tuple_list)
                        inner_list.append(var_tuple)
                        outer_list.append(inner_list)
                    to = TupleOccurances(outer_list)
                    print(f"The entered list of tuples is : \033[94m{to.get_list()}\033[97m")
                    result = to.tuples_occurrence_in_list_of_tuples()
                    print(f"\033[92m Number of occurances of a tuple : {result} \033[97m")
                except Exception as e:
                    print(f"OOPS ! The Exception caught : {str(e)}")

            elif choice_tuples == '10':
                print("\033[94mOption 10 Sort a list of tuples alphabetically\033[97m")
                '''
                [("Amana", 28), ("Zenat", 30), ("Abhishek", 29), ("Nikhil", 21), ("B", "C")]
                '''
                try:
                    outer_list_size = int(input("Enter number of lists : "))
                    size_of_tuples = int(input("Enter the size of the tuples : "))
                    outer_list = []
                    for i in range(0,outer_list_size):
                        print(f" list number : {i}")
                        tuple_list = []
                        for j in range(0, size_of_tuples):
                            elements = str(input("Enter the elements : "))
                            tuple_list.append(elements)
                        var_tuple = tuple(tuple_list)
                        outer_list.append(var_tuple)
                    sta = SortTuplesAlpha(outer_list)
                    print(f"The entered list of tuples is : \033[94m{sta.get_list()}\033[97m")
                    result = sta.sort_tuples_based_on_alphabets()
                    print(f"\033[92m Sorted tuples in alphabetical form : {result} \033[97m")
                except Exception as e:
                    print(f"OOPS ! The Exception caught : {str(e)}")

            else:
                print("\033[91m!!! Wrong choice !!!\033[97m")
                print("\n")