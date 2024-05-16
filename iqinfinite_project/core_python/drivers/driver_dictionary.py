import pyfiglet
# dictionary related imports
from dictionary.StringToDictionary import *
from dictionary.swapping_nested_dictionary import *
from dictionary.ReverseDictionary import *
from dictionary.remove_keys import *
from dictionary.max_pairs import *
from dictionary.UniqueValues import *
from dictionary.KeysValuesDict import *
from dictionary.anagrams import *
from dictionary.sort_dict_key_value import *

class DriverDictionary:
    def driver_dictionary(self):
        for i in range (0,9999):
            T = "Dictionary"
            ASCII_art_1 = pyfiglet.figlet_format(T,font="doh")
            print(f"\033[95m{ASCII_art_1}\033[97m")
            print("""
-----------------------------------------------------------------------------------------
|                                                                                       |
|                               >>> DICTIONARY SECTION <<<                              |
|  1.  Convert dictionary string values to List of dictionaries                         |
|  2.  Swapping Hierarchy in Nested Dictionaries                                        |
|  3.  Reverse Dictionary Keys Order                                                    |
|  4.  Remove keys with Values Greater than K ( Including mixed values )                |
|  5.  Dictionary with maximum count of pairs                                           |
|  6.  Extract Unique values dictionary values                                          |
|  7.  Keys associated with Values in Dictionary                                        |
|  8.  Anagrams together in Python using List and Dictionary                            |
|  9.  Counter to find the size of largest subset of anagram words                      |
|  10. Sort Dictionary key and values List                                              |
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
            choice_dictionary = input("Enter your choice: ")
            if choice_dictionary == '0':
                T = "Exit"
                ASCII_art_exit = pyfiglet.figlet_format(T,font="doh")
                print(f"\033[91m{ASCII_art_exit}\033[97m")
                break

            elif choice_dictionary == '1':
                print(f"\033[94mOption 1 Convert dictionary string values to List of dictionaries\033[97m")
                try:
                    # initializing dictionary
                    test_dict = {"Gfg": "1:2:3:7:9", "best": "4:8", "good": "2"}
                    std = StringToDictionary(test_dict)
                    print(f"Entered dictionary : \033[93m{std.get_dictionary()}\033[97m")
                    result = std.string_to_dictionary()
                    print(f"\033[92mConverted string from dictionary : {result}\033[97m")
                except Exception as e:
                    print(f"OOPS ! The Exception caught : {str(e)}")
                
            elif choice_dictionary == '2':
                print(f"\033[94mOption 2 Swapping Hierarchy in Nested Dictionaries\033[97m")
                try:
                    # initializing dictionary
                    test_dict = {'Gfg': { 'a' : [1, 3], 'b' : [3, 6], 'c' : [6, 7, 8]},
                                 'Best': { 'a' : [7, 9], 'b' : [5, 3, 2], 'd' : [0, 1, 0]}}
                    snd = SwapNestedDictionary(test_dict)
                    print(f"Entered dictionary : \033[93m{snd.get_dictionary()}\033[97m")
                    result = snd.swapping_hierarchy()
                    print(f"\033[92mSwapping Hierarchy : {result}\033[97m")
                except Exception as e:
                    print(f"OOPS ! The Exception caught : {str(e)}")
            
            elif choice_dictionary == '3':
                print(f"\033[94mOption 3 Reverse Dictionary Keys Order\033[97m")
                try:
                    test_dict = {'gfg' : 4, 'is' : 2, 'best' : 5}
                    rd = ReverseDictionary(test_dict)
                    print(f"Entered dictionary : \033[93m{rd.get_dictionary()}\033[97m")
                    result = rd.reverse_dictionary()
                    print(f"\033[92mSwapping Hierarchy : {result}\033[97m")
                except Exception as e:
                    print(f"OOPS ! The Exception caught : {str(e)}")

            elif choice_dictionary == '4':
                print(f"\033[94mOption 4 Remove keys with Values Greater than K ( Including mixed values )\033[97m")
                try:
                    # initializing dictionary
                    test_dict = {'Gfg': 3, 'is': 7, 'best': 10, 'for': 6, 'geeks': 'CS'} 
                    k = 6
                    rkvik = RemoveKeysValuesInK(test_dict,k)
                    print(f"Entered dictionary : \033[93m{rkvik.get_dictionary()}\033[97m")
                    print(f"Entered k : \033[93m{rkvik.get_k()}\033[97m")
                    result = rkvik.remove_keys_with_values_greater_than_k()
                    print(f"\033[92mRemove Keys with values greater than k : {result}\033[97m")  
                except Exception as e:
                    print(f"OOPS ! The Exception caught : {str(e)}")       
            
            elif choice_dictionary == '5':     
                print(f"\033[94mOption 5 Dictionary with maximum count of pairs\033[97m")
                try:
                    test_list = [{"gfg": 2, "best" : 4}, {"gfg": 2, "is" : 3, "best" : 4, "CS" : 9}, {"gfg": 2}]
                    mp = MaxPairs(test_list)
                    print(f"Entered dictionary : \033[93m{mp.get_list()}\033[97m")
                    result = mp.max_pair()
                    print(f"\033[92mDictionary with maximum count of pairs : {result}\033[97m") 
                except Exception as e:
                    print(f"OOPS ! The Exception caught : {str(e)}")
            
            elif choice_dictionary == '6':
                print(f"\033[94mOption 6 Extract Unique values dictionary values\033[97m")
                try:
                    test_dict = {'gfg': [5, 6, 7, 8],
                    'is': [10, 11, 7, 5],
                    'best': [6, 12, 10, 8],
                    'for': [1, 2, 5]}
                    uv = UniqueValues(test_dict)
                    print(f"Entered dictionary : \033[93m{uv.get_dictionary()}\033[97m")
                    result = uv.unique_values()
                    print(f"\033[92mExtract Unique values dictionary values : {result}\033[97m") 
                except Exception as e:
                    print(f"OOPS ! The Exception caught : {str(e)}")
            
            elif choice_dictionary == '7':
                print(f"\033[94mOption 7 Keys associated with Values in Dictionary\033[97m")
                test_dict = {'is': [1, 4], 'gfg': [1, 2, 3], 'best': [4, 2]}
                kawvid = KeyAssociatedWithValuesInDictionary(test_dict)
                print(f"Entered dictionary : \033[93m{kawvid.get_dictionary()}\033[97m")
                result = kawvid.key_associated_with_values_in_dictionary()
                print(f"\033[92mKeys associated with Values in Dictionary : {str(result)}\033[97m") 

            elif choice_dictionary == '8':
                print(f"\033[94mOption 8 Anagrams together in Python using List and Dictionary\033[97m")
                test_dict = ['cat', 'dog', 'tac', 'god', 'act']
                aag = AllAnagram(test_dict)
                print(f"Entered dictionary : \033[93m{aag.get_list()}\033[97m")
                result = aag.all_anagram()
                print(f"\033[92mAnagrams together in Python using List and Dictionary : {str(result)}\033[97m") 

            elif choice_dictionary == '9':
                print(f"\033[94mOption 9 Counter to find the size of largest subset of anagram words\033[97m")
                var_string = input("Enter the string : ")
                lsoa = LargeSubsetsOfAnagram(var_string)
                print(f"Entered dictionary : \033[93m{lsoa.get_string()}\033[97m")
                result = lsoa.maxAnagramSize()
                print(f"\033[92mCounter to find the size of largest subset of anagram words : {str(result)}\033[97m")  

            elif choice_dictionary == '10':
                print(f"\033[94mOption 10 Sort Dictionary key and values List\033[97m")
                test_dict = {'gfg': [7, 6, 3], 
                                 'is': [2, 10, 3], 
                                 'best': [19, 4]}
                sd = SortDictionary(test_dict)
                print(f"Entered dictionary : \033[93m{sd.get_dictionary()}\033[97m")
                result = sd.sort()
                print(f"\033[92mCounter to find the size of largest subset of anagram words : {str(result)}\033[97m")

            else:
                print("\033[91m!!! Wrong choice !!!\033[97m")
                print("\n")