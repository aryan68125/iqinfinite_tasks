#Count Vowels
'''
Input : GeeksforGeeks
Output : No. of vowels : 5
Explaination: The string GeeksforGeeks contains 5 vowels in it 4 letter of 'e' and 1 'o'.
'''
#Count Vowels : solution
class CountVowels:
    def __init__(self,word):
        self.__word = word
    def get_word(self):
        return self.__word
    def set_word(self,word):
        self.__word = word
    def count_vowels(self):
        w_string = self.__word
        count=0
        for i in w_string:
            if i in 'aeiou':
               count+=1
        return count 