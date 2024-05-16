# Convert numbers to word
'''
Input: S = “zero four zero one”
Output: 0401

Input: S = “four zero one four”
Output: 4014
'''
# Convert numbers to word : solution
help_dict = {
'one' : '1',
'two' : '2',
'three' : '3',
'four' : '4',
'five' : '5',
'six' : '6',
'seven' : '7',
'eight' : '8',
'nine' : '9',
'ten' : '10'
}
class WordToNumber:
    def __init__(self,word):
        self.__word = word
    def get_word(self):
        return self.__word
    def set_word(self,word):
        self.__word = word
    def word_to_number(self):
        w_string = self.__word
        lower_case_string = w_string.lower()
        res = ''.join(help_dict[ele] for ele in lower_case_string.split())
        return res
        