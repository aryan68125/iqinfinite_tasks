# Maching Characters
'''
Input : str1 = 'abcdef'
        str2 = 'defghia'
Output : 4 
(i.e. matching characters :- a, d, e, f)

Input : str1 = 'aabcddekll12@'
        str2 = 'bb2211@55k'
Output : 5 
(i.e. matching characters :- b, 1, 2, @, k)
'''
# Maching Characters : Solution

class MatchingChar:
    def __init__(self,first_word,second_string):
        self.__first_word = first_word
        self.__second_word = second_string
    def get_first_word(self):
        return self.__first_word
    def set_first_word(self,first_word):
        self.__first_word = first_word
    def get_second_word(self):
        return self.__second_word
    def set_second_word(self,second_string):
        self.__second_word = second_string
    def match_char(self):
        f_string = self.__first_word
        s_string = self.__second_word
        
        #first string
        f_last = len(f_string)

        #second_string
        s_last = len(s_string)

        print(f"first string : {f_last}")
        print(f"second string : {s_last}")

        count = 0
        common_chars = []
        for char1 in f_string:
            if char1 in s_string and char1 not in common_chars:
                common_chars.append(char1)
                count += 1
        context = {
            'common_char':common_chars,
            'common_char_count':count
        }
        return context
