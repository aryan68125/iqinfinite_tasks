# Reverse
'''
Input : str =" geeks quiz practice code"
Output : str = code practice quiz geeks  
Input : str = "my name is laxmi"
output : str= laxmi is name my 
'''
# Reverse : Solution
class Reverse:
    def __init__(self,rev_word):
        self.__reverse_word = rev_word
    def get_word(self):
        return self.__reverse_word
    def set_word(self,rev_word):
        self.__reverse_word = rev_word
    def reverse_word(self):
        word = self.__reverse_word
        
        '''
        word.split() : this will split the entire string into sub stings based on white spaces in a string by default
        [::-1] : The [::-1] syntax creates a slice that starts from the end of the list and ends at the beginning, effectively reversing the list.
        '''
        reverse_word = word.split()[::-1]
        l = []
        for i in reverse_word:
            l.append(i)
        '''
        print(" ".join(l)) : Here, l is assumed to be a list of strings. The join() method is used to concatenate the elements of the list l into a single string, separated by the string " ".
        '''
        print("\033[92mThe reversed string is : \033[97m")
        print(f'\033[92m{" ".join(l)}\033[97m')
        