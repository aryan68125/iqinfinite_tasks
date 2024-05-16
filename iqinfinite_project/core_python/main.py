# String related imports

#utility related imports
from list_package import ListPackageFiles
import pyfiglet

#string relataed imports
from drivers.driver_string import DriverString

#tuples related imports
from drivers.driver_tuples import DriverTuples

#list related imports
from drivers.driver_list import DriverList

#dictionary related imports
from drivers.driver_dictionary import DriverDictionary

#sets related imports
from drivers.driver_sets import DriverSets

#loops related imports
from drivers.driver_loops import DriverLoops

#operator related imports
from drivers.driver_operator import DriverOperator

welcome_message = """
\033[95m **      **  ********  **       **          **       \033[91m   ---------    \033[97m
\033[95m **      **  **        **       **        **  **     \033[91m  /         \   \033[97m
\033[95m **********  ********  **       **       **    **    \033[91m  |  /\ /\  |   \033[97m
\033[95m **********  ********  **       **       **    **    \033[91m  |    -    |   \033[97m
\033[95m **      **  **        *******  *******   **  **     \033[91m  |  \   /  |   \033[97m
\033[95m **      **  ********  *******  *******     **       \033[91m  \   ---   /   \033[97m
                                                     \033[91m   ---------    \033[97m
"""
print(welcome_message)
print(r"""

                                   ._ o o
                                   \_`-)|_
                                ,""       \ 
                              ,"  ## |   ಠ ಠ. 
                            ," ##   ,-\__    `.
                          ,"       /     `--._;)
                        ,"     ## /
                      ,"   ##    /


                """)

#Driving loop
for i in range(0,9999):
    #Enter choice
    print("Choose the items in the menu by using numbers : ")
    print("")
    print("""
          \033[91m
-----------------------------------------------------------------------------------------
|                                                                                       |
|                           Press 'n' or 'N' to exit program                            |
|                                                                                       |
-----------------------------------------------------------------------------------------
          \033[97m
    """)
    print("""
          \033[94m
-----------------------------------------------------------------------------------------
|                                                                                       |
|            Press 0 Check the list of files present in a package (FOR DEVS ONLY)       |
|                                                                                       |
-----------------------------------------------------------------------------------------
          \033[97m
    """)
    print("""
      \033[93m
-----------------------------------------------------------------------------------------
|                                                                                       |
|                                 >>> MAIN MENU <<<                                     |
|                                                                                       |
|               >>>   TYPE 'strings' to select the strings menu   <<<                   |
|               >>>    TYPE 'tuples' to select the tuples menu    <<<                   |
|               >>>      TYPE 'list' to select the list menu      <<<                   |
|               >>>TYPE 'dictionary' to select the dictionary menu<<<                   |
|               >>>      TYPE 'sets' to select the sets menu      <<<                   |
|               >>>      TYPE 'loop' to select the loop menu      <<<                   |
|               >>>  TYPE 'operator' to select the operator menu  <<<                   |
|                                                                                       |
-----------------------------------------------------------------------------------------
      \033[97m
    """)

    choice_input = input("Enter your choice: ")
    print('\n')
    #driving list_package_files
    if choice_input == '0':
        T = "</>"
        s = " Dev only"
        ASCII_art_symbol = pyfiglet.figlet_format(T,font="doh")
        ASCII_art_msg = pyfiglet.figlet_format(s,font="doh")
        print(f"\033[91m{ASCII_art_symbol}\033[97m{ASCII_art_msg}")
        print("""          

                   \033[92m        .---------------------------------.
                   \033[92m        |  .---------------------------.  |
                   \033[92m        |[]|\033[94m         __   __   *       \033[92m|[]|
                   \033[92m        |  |\033[94m        /  | /  | /        \033[92m|  |
                   \033[92m        |  |\033[94m       (___|(___|(         \033[92m|  |
                   \033[92m        |  |\033[94m       |   )|    |         \033[92m|  |
                   \033[92m        |  |\033[94m       |  / |    |         \033[92m|  |
                   \033[92m        |  |\033[94m /              |         |\033[92m|  |
                   \033[92m        |  |\033[94m(  ___  ___  ___| ___  ___|\033[92m|  |
                   \033[92m        |  |\033[94m| |   )|   )|   )|___)|   )\033[92m|  |
                   \033[92m        |  |\033[94m| |__/ |__/||__/ |__  |__/ \033[92m|  |
                   \033[92m        |  '---------------------------'  |
                   \033[92m        |                                 |
                   \033[92m        |                                 |
                   \033[92m        |  '---------------------------'  |
                   \033[92m        |  | .------.         |      | |  |
                   \033[92m        |  | |      |         |      | |  |
                   \033[92m        |  | |      |         |      | |  |
                   \033[92m        |  | |      |         |      | |  |
                   \033[92m        |  | '------'         |      | |  |
                   \033[92m        -----------------------------------
\033[97m
              
              \033[92m
-----------------------------------------------------------------------------------------
|                                                                                       |
|                               >>> SELECT PACKAGE <<<                                  |
|  0.  drivers                                                                          |
|  1.  strings                                                                          |
|  2.  tuples                                                                           |
|  3.  list_custom                                                                      |
|  4.  dictionary                                                                       |
|  5.  sets                                                                             |
|  6.  loop                                                                             |
|  7.  operator                                                                         |
|                                                                                       |
-----------------------------------------------------------------------------------------
              \033[97m
        """) 
        package_name = input("Enter your package name:")
        lpf = ListPackageFiles(package_name)
        try:
            files = lpf.list_package_files()
            print("\033[93mFiles in package \033[95m'{}':\033[97m".format(package_name))
            for file in files:
                print(f"\033[92m-{file}\033[97m")
            print("\n")
        except Exception as e: 
            print(str(e))
            print("\033[91m!!! PACKAGE NOT FOUND !!!\033[97m")
            print("\n")

    #driving palindrome
    if choice_input.lower() == 'strings':
        ds = DriverString()
        ds.driver()

    if choice_input.lower() == 'tuples':
        dt = DriverTuples()
        dt.driver_tuples()

    if choice_input.lower() == 'list':
        dl = DriverList()
        dl.driver_list()

    if choice_input.lower() == 'dictionary':
        dd = DriverDictionary()
        dd.driver_dictionary()
        
    if choice_input.lower() == 'sets':
        ds = DriverSets()
        ds.driver_sets()

    if choice_input.lower() == 'loop':
        dl = DriverLoops()
        dl.driver_loops()

    if choice_input.lower() == 'operator':
        dor = DriverOperator()
        dor.driver_operator()

    elif choice_input.lower() == 'n':
        print("Terminating program")
        T = "BYE"
        ASCII_art_1 = pyfiglet.figlet_format(T,font="doh")
        print(f"\033[91m{ASCII_art_1}\033[97m")
        print('\n')
        break
    
    else:
        if choice_input == '0':
            print("Dev only operation!!")
            print('\n')
        else:
           print("\033[91m!!! Wrong choice !!!\033[97m")
           print('\n')