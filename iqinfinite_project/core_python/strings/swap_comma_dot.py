#Swap commas and dots in a String
'''
Input : 14, 625, 498.002
Output : 14.625.498, 002 
'''
def Replace(str1):
    maketrans = str1.maketrans
    final = str1.translate(maketrans(',.', '.,', ' '))
    return final.replace(',', ", ")
#Swap commas and dots in a String : solution
class SwapCommaDots:
    def __init__(self, word):
        self.__word = word
    def get_word(self):
        return self.__word
    def set_word(self, word):
        self.__word = word
    def swap_common_dots(self):
        w_string = self.__word
        maketrans = w_string.maketrans
        final = w_string.translate(maketrans(',.', '.,', ' '))
        return final.replace(',', ", ")