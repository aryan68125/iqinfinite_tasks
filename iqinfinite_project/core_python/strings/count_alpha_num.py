# count num and alpha
'''
counts the number of alphabets and numbers present in a string
'''
# count num and alpha : solution
class CountAlphaNum:
    def __init__(self,word):
        self.__word = word
    def get_word(self):
        return self.__word
    def set_word(self,word):
        self.__word = word
    def count_alpha_and_num(self):
        w_string = self.__word
        start = 0
        last = len(w_string)
        count_alpha = 0
        count_num = 0
        for i in range(start,last):
            if w_string[i].isalpha():
                count_alpha += 1
            elif w_string[i].isdigit():
                count_num += 1
        context = {
            'count_alpha': count_alpha,
            'count_num' : count_num,
            'total' : last
        }
        return context