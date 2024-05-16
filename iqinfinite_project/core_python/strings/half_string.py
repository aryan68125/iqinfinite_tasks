# Half String
'''
Input : test_str = 'geeksforgeek' 
Output : geeksfORGEEK 
Explanation : Latter half of string is uppercased. 

Input : test_str = 'apples' 
Output : appLES 
Explanation : Latter half of string is uppercased.
'''

# Half String : Solution

class HalfString:
    def __init__(self, word):
        self.__word = word
    def get_word(self):
        return self.__word
    def set_word(self,word):
        self.__word = word

    def half_string(self):
        w_string = self.__word
        start = 0
        last = len(w_string)
        mid = last//2

        l = []
        for i in range(start,last):
            if i>=mid and (not w_string[i].isspace()):
                ch = w_string[i].upper()
                l.append(ch)
            elif w_string[i].isspace():
                print('White spaces in a string not allowed!!')
                return -1
            else:
                ch = w_string[i]
                l.append(ch)
        res_str = "".join(l)
        return res_str
