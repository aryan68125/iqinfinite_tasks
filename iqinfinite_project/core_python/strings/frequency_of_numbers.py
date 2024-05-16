# Frequency of numbers
'''
The original string is : geeks4feeks is No. 1 4 geeks
Count of numerics in string : 3
'''
# Frequency of numbers : solution
class FrequencyOfNumbers:
    def __init__(self,word):
        self.__word = word
    def get_word(self):
        return self.__word
    def set_word(self,word):
        self.__word = word
    def freqency_of_numbers(self):
        w_string = self.__word
        start = 0
        last = len(w_string)
        count = 0
        for i in range(start,last):
            if w_string[i] in "123456789":
                count += 1
        return count