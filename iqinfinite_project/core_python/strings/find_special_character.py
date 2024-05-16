# Find special characters in a string
'''
Finds the special characters in a given string
'''
# Find special characters in a string : solution
import re
class FindSpecialCharacters:
    def __init__(self,word):
        self.__word = word
    def get_word(self):
        return self.__word
    def set_word(self,word):
        self.__word = word
    def find_special_characters(self):
        w_string = self.__word
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        start = 0
        last = len(w_string)
        ch = []
        character_count = 0
        sp=[]
        specia_character_count = 0
        for i in range(start,last):
            if(regex.search(w_string[i]) == None):
                ch.append(w_string[i])
                character_count += 1
            else:
                sp.append(w_string[i])
                specia_character_count += 1                
        context = {
            'sp_list':sp,
            'sp_count':specia_character_count,
            'ch_list':ch,
            'ch_count':character_count
        }
        return context