# Uncommon words
'''
Input : A = “Geeks for Geeks”,  B = “Learning from Geeks for Geeks”
Output : [‘Learning’, ‘from’]
'''
# Uncommon words : solution
class UncommonWords:
    def __init__(self, first_word, second_word):
        self.__f_word = first_word
        self.__s_word = second_word
    def get_f_word(self):
        return self.__f_word
    def get_s_word(self):
        return self.__s_word
    def uncommon_word(self):
        f_string = self.__f_word
        s_string = self.__s_word
        count = {}
        for word in f_string.split():
            count[word] = count.get(word,0)+1
        for word in s_string.split():
            count[word] = count.get(word,0)+1
        return [word for word in count if count[word] == 1]
        