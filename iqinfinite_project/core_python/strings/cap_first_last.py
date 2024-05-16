# Capitalize the first and last letters in a string
'''
Input: hello world 
Output: HellO WorlD

Input: welcome to geeksforgeeks
Output: WelcomE TO GeeksforgeekS
'''

# capitalize first and last letters in a string : Solution
class CapFirstLast:
    def __init__(self, word):
        self.__word = word
    def get_word(self):
        return self.__word
    def set_word(self,word):
        self.__word = word

    def cap_first_and_last_letter(self):
        input_string = self.__word
        words = input_string.split()
        modified_words = []
        
        for word in words:
            if len(word) > 1:
                modified_word = word[0].upper() + word[1:-1] + word[-1].upper()
            else:
                modified_word = word.upper()
            modified_words.append(modified_word)
        
        return " ".join(modified_words)
    
