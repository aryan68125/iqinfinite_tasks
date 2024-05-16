import pyfiglet
#string relataed imports
from strings.palindrom import *
from strings.symmetry import *
from strings.reverse import *
from strings.length_string import *
from strings.length_without_spaces import *
from strings.find_even_length_words import *
from strings.half_string import *
from strings.cap_first_last import *
from strings.count_alpha_num import *
from strings.matching_chars import *
from strings.count_vowels import *
from strings.remove_all_duplicates import *
from strings.frequency_of_numbers import *
from strings.find_special_character import *
from strings.uncommon_word import *
from strings.swap_comma_dot import *
from strings.extract_url import *
from strings.word_to_number import *
from strings.word_location import *
from strings.consecutive_characters import *

class DriverString:
    def driver(self):
        for i in range (0,9999):
            string_welcome_message = '''
        \033[95m
***********   ***************      ***********       **        ****         **      **************     **************
***********   ***************      ***********       **        ** **        **      **************     **************
**                  **             **       **       **        **  **       **      **                 **
**                  **             **       **       **        **   **      **      **                 **
***********         **             **       **       **        **    **     **      **                 **************
***********         **             ***********       **        **     **    **      **     *******     **************
         **         **             ***********       **        **      **   **      **     *******                 **
         **         **             ****              **        **       **  **      **          **                 **  
         **         **             ** **             **        **        ** **      **          **                 **
***********         **             **  **            **        **         ****      **************     **************
***********         **             **   **           **        **          ***      **************     **************
\033[97m
'''
            print(string_welcome_message)
            print("""
-----------------------------------------------------------------------------------------
|                                                                                       |
|                         >>> STRINGS SECTION <<<                                       |
|  1.  Check Palindrome                                                                 |
|  2.  Check Symmetry                                                                   |
|  3.  Reverse String                                                                   |
|  4.  Length of a String                                                               |
|  5.  Length of a String (EXCLUDING WHITE SPACES)                                      |
|  6.  Even Length words in a String                                                    |
|  7.  Half String (Converts the characters to upper case of half of the string passed) |
|  8.  Convert first and last characters in a string to capital letters                 |
|  9.  Count number of alphabets and numbers present in a string                        |
|  10. It will tell the characters that are common in two strings                       |
|  11. Count vowels in a string                                                         |
|  12. Remove all duplicate characters from the string                                  |
|  13. Frequency of numbers in a string                                                 |
|  14. Find special characters in a string                                              |
|  15. Find uncommon words in the two string                                            |
|  16. Swap commas with the dots in the string                                          |
|  17. Extract url from the string                                                      |
|  18. Convert numbers to word                                                          |
|  19. Word location in the string                                                      |
|  20. Compute the frequency of consecutive characters till the character changes       |
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
            choice_string = input("Enter your choice: ")
            if choice_string =='0':
                T = "Exit"
                ASCII_art_exit = pyfiglet.figlet_format(T,font="doh")
                print(f"\033[91m{ASCII_art_exit}\033[97m")
                break

            elif choice_string == '1':
                print("\033[94mOption 1 Check Palindrome -->\033[97m")
                try:
                    word = input("Enter the word that you want to check :")
                    pd = Palindrome(word)
                    print(f"The entered string is : \033[93m{pd.get_ch_string()}\033[97m")
                    pd.check_palindrome()
                    print('\n')
                except Exception as e:
                    print(f"\033[91mOOPS ! The Exception caught : {str(e)}\033[97m")
    
            elif choice_string == '2':
                print("\033[94mOption 2 Check Symmetry -->\033[97m")
                try:
                    word = input("Enter the word that you want to check :")
                    sm = Symmetry(word)
                    print(f"The entered string is : \033[93m{sm.get_ch_string()}\033[97m")
                    sm.check_symmetry()
                    print('\n')
                except Exception as e:
                    print(f"\033[91mOOPS ! The Exception caught : {str(e)}\033[97m")
    
            elif choice_string == '3':
                print('\033[94mOption 3 Reverse the given string -->\033[97m')
                try:
                    word = input("Enter the string to be reversed :")
                    rv = Reverse(word)
                    print(f"the entered string : \033[93m{rv.get_word()}\033[97m")
                    rv.reverse_word()
                    print('\n')
                except Exception as e:
                    print(f"\033[91mOOPS ! The Exception caught : {str(e)}\033[97m")
    
            elif choice_string == '4':
                print('\033[94mOption 4 Length of a given string -->\033[97m')
                try:
                    word = input("Enter the string to get it's length :")
                    len = Length(word)
                    print(f"the entered string : \033[93m{len.get_word()}\033[97m")
                    length = len.length_of_string()
                    print(f"\033[92mThe length of the string is : {length}\033[97m")
                    print('\n')
                except Exception as e:
                    print(f"\033[91mOOPS ! The Exception caught : {str(e)}\033[97m")
        
            elif choice_string == '5':
                print('\033[94mOption 5 Length of a given string (EXCLUDING WHITE SPACES) -->\033[97m')
                try:
                    word = input("Enter the string to get it's length :")
                    lws = LengthWithoutSpaces(word)
                    print(f"the entered string : \033[93m{lws.get_word()}\033[97m")
                    len_without_spaces = lws.length_without_spaces()
                    print(f"\033[92mThe length of the string is (EXCLUDING WHITE SPACES) : {len_without_spaces}\033[97m")
                    print('\n')
                except Exception as e:
                    print(f"\033[91mOOPS ! The Exception caught : {str(e)}\033[97m")
    
            elif choice_string == '6':
                print('\033[94mOption 6 Get the string that has even length -->\033[97m')
                try:
                    word = input("Enter the string :")
                    few = FindEvenLengthWords(word)
                    print(f"the entered string : \033[93m{few.get_word()}\033[97m")
                    few.find_even_length_words()
                    print('\n')
                except Exception as e:
                    print(f"\033[91mOOPS ! The Exception caught : {str(e)}\033[97m")
    
            elif choice_string == '7':
                print('\033[94mOption 7 Half String (Converts the characters to upper case of half of the string passed)\033[97m ')
                try:
                    word = input("Enter the string :")
                    hs = HalfString(word)
                    print(f"the entered string : \033[93m{hs.get_word()}\033[97m")
                    half_string_var = hs.half_string()
                    if not half_string_var == -1:
                        print(f"\033[92mHalf String Result : {half_string_var}\033[97m")
                    else:
                        print("\033[91mThe Half String class Failed to return a result\033[97m")
                    print('\n')
                except Exception as e:
                    print(f"\033[91mOOPS ! The Exception caught : {str(e)}\033[97m")
    
            elif choice_string == '8':
                print("\033[94mOption 8 Convert first and last characters in a string to capital letters\033[97m ")
                try:
                    word = input("Enter the string :")
                    cfl = CapFirstLast(word)
                    print(f"the entered string : \033[93m{cfl.get_word()}\033[97m")
                    result = cfl.cap_first_and_last_letter()
                    print(f"\033[92mCapitalized first and last characters of a string : {result}\033[97m")
                    print('\n')
                except Exception as e:
                    print(f"\033[91mOOPS ! The Exception caught : {str(e)}\033[97m")
    
            elif choice_string == '9':
                print("\033[94mOption 9 Count number of alphabets and numbers present in a string\033[97m ")
                try:
                    word = input("Enter the string :")
                    can = CountAlphaNum(word)
                    print(f"the entered string : \033[93m{can.get_word()}\033[97m")
                    result = can.count_alpha_and_num()
                    print(f"\033[92mNumber of Alphabets : {result['count_alpha']}\033[97m")
                    print(f"\033[92mNumber of Digits : {result['count_num']}\033[97m")
                    print(f"\033[92mTotal Characters : {result['total']}\033[97m")
                    print('\n')
                except Exception as e:
                    print(f"\033[91mOOPS ! The Exception caught : {str(e)}\033[97m")

            elif choice_string == '10':
                print("\033[94mOption 10 It will tell the characters that are common in two strings\033[97m ")
                try:
                     first_word = input("Enter the first string :")
                     second_word = input("Enter the second string :")
                     mc = MatchingChar(first_word,second_word)
                     print(f"the first entered string : \033[93m{mc.get_first_word()}\033[97m")
                     print(f"the second entered string : \033[93m{mc.get_second_word()}\033[97m")
                     result = mc.match_char()
                     print(f"\033[92mCommon Characters : {result['common_char']}\033[97m")
                     print(f"\033[92mNumber of common characters : {result['common_char_count']}\033[97m")
                     print('\n')
                except Exception as e:
                    print(f"\033[91mOOPS ! The Exception caught : {str(e)}\033[97m")
        
            elif choice_string == '11':
                print("\033[94mOption 11 Count vowels in a string\033[97m ")
                try:
                    word = input("Enter the string :")
                    cvw = CountVowels(word)
                    print(f"the entered string : \033[93m{cvw.get_word()}\033[97m")
                    result = cvw.count_vowels()
                    print(f"\033[92mNumber of Vowels in the string : {result}\033[97m")
                    print('\n')
                except Exception as e:
                    print(f"\033[91mOOPS ! The Exception caught : {str(e)}\033[97m")

            elif choice_string == '12':
                print("\033[94mOption 12 Remove all duplicate characters from the string\033[97m ")
                try:
                    word = input("Enter the string :")
                    rad = RemoveAllDuplicates(word)
                    print(f"the entered string : \033[93m{rad.get_word()}\033[97m")
                    result = rad.remove_all_duplicates()
                    print(f"\033[92mAfter Removing duplicate characters in the string : {result}\033[97m")
                    print('\n')
                except Exception as e:
                    print(f"\033[91mOOPS ! The Exception caught : {str(e)}\033[97m")
    
            elif choice_string == '13':
                print("\033[94mOption 13 Frequency of numbers in a string\033[97m ")
                try:
                    word = input("Enter the string :")
                    fon = FrequencyOfNumbers(word)
                    print(f"the entered string : \033[93m{fon.get_word()}\033[97m")
                    result = fon.freqency_of_numbers()
                    print(f"\033[92mFrequency of numbers in the string : {result}\033[97m")
                    print('\n')
                except Exception as e:
                    print(f"\033[91mOOPS ! The Exception caught : {str(e)}\033[97m")

            elif choice_string == '14':
                print("\033[94mOption 14 Find special characters in a string\033[97m ")
                try:
                    word = input("Enter the string :")
                    fsc = FindSpecialCharacters(word)
                    print(f"the entered string : \033[93m{fsc.get_word()}\033[97m")
                    result = fsc.find_special_characters()
                    print(f"\033[92mSpecial characters list in the string : {result['sp_list']}\033[97m")
                    print(f"\033[92mFrequency of special characters in the string : {result['sp_count']}\033[97m")
                    print(f"\033[92mNormal characters list in the string : {result['ch_list']}\033[97m")
                    print(f"\033[92mFrequency of normal characters in the string : {result['ch_count']}\033[97m")
                    print('\n')
                except Exception as e:
                    print(f"\033[91mOOPS ! The Exception caught : {str(e)}\033[97m")

            elif choice_string == '15':
                print("\033[94mOption 15 Find uncommon words in the two string\033[97m ")
                try:
                    word = input("Enter the string :")
                    search = input("Enter the word to be searched in the string :")
                    ucw = UncommonWords(word, search)
                    print(f"the entered first string : \033[93m{ucw.get_f_word()}\033[97m")
                    print(f"the entered second string : \033[93m{ucw.get_s_word()}\033[97m")
                    result = ucw.uncommon_word()
                    print(f"\033[92mList of uncommon words in the two strings : {result}\033[97m")
                    print('\n')
                except Exception as e:
                    print(f"\033[91mOOPS ! The Exception caught : {str(e)}\033[97m")

            elif choice_string == '16':
                print("\033[94mOption 16 Swap commas with the dots in the string\033[97m ")
                try:
                    word = input("Enter the string :")
                    scd = SwapCommaDots(word)
                    print(f"the entered string : \033[93m{scd.get_word()}\033[97m")
                    result = scd.swap_common_dots()
                    print(f"\033[92mSwapped commas with the dots in the string : {result}\033[97m")
                    print('\n')
                except Exception as e :
                    print(f"\033[91mOOPS ! The Exception caught : {str(e)}\033[97m")

            elif choice_string == '17':
                print("\033[94mOption 17 Extract url from the string\033[97m ")
                try:
                    word = input("Enter the string :")
                    exu = ExtractUrl(word)
                    print(f"the entered string : \033[93m{exu.get_word()}\033[97m")
                    result = exu.extract_url()
                    print(f"\033[92mExtract url from the string : {result}\033[97m")
                    print('\n')
                except Exception as e:
                    print(f"\033[91mOOPS ! The Exception caught : {str(e)}\033[97m")

            elif choice_string == '18':
                print("\033[94mOption 18 Convert numbers to word\033[97m ")
                word = input("Enter the string :")
                wtn = WordToNumber(word)
                print(f"the entered string : \033[93m{wtn.get_word()}\033[97m")
                try:
                    result = wtn.word_to_number()
                    print(f"\033[92mConveted numeric words to numbers in the string : {result}\033[97m")
                except Exception as e:
                    print(f"\033[91m!!! {str(e)} is not in the dictionary !!!\033[97m")
                print('\n')

            elif choice_string == '19':
                print("\033[94mOption 19 Word location in the string\033[97m ")
                word = input("Enter the string :")
                search = input("Enter the string that you want to get the location of :")
                wlc = WordLocation(word,search)
                print(f"the entered first string : \033[93m{wlc.get_word()}\033[97m")
                print(f"the entered string whoes location you want : \033[93m{wlc.get_search_word()}\033[97m")
                try:
                    result = wlc.word_location()
                    print(f"\033[92mLocation of the searched word in the string : {result}\033[97m")
                except Exception as e:
                    print(f"\033[91mOOPS ! The Exception caught : {str(e)}\033[97m")
                print('\n')

            elif choice_string == '20':
                print("\033[94mOption 20 Compute the frequency of consecutive characters till the character changes\033[97m ")
                word = input("Enter the string :")
                ctc = ConsecutiveCharacters(word)
                print(f"the entered string : \033[93m{ctc.get_word()}\033[97m")
                try:
                    result = ctc.consecutive_word()
                    print(f"\033[92mFrequency of consecutive characters in the string : {result}\033[97m")
                except Exception as e:
                    print(f"\033[91mOOPS ! The Exception caught : {str(e)}\033[97m")
                print('\n')

            else:
                print("\033[91m!!! Wrong choice !!!\033[97m")
                print('\n')