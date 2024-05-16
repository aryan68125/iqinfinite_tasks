# Tuple Size
'''
Find the size of a Tuple in Python
'''
# Tuple Size : solution
import sys
class TupleSize:
    def __init__(self, word):
        self.__word = word
    def get_word(self):
        return self.__word
    def get_size_of_tuple(self):
        w_string = self.__word
        w_list = []
        for word in w_string:
            w_list.append(word)
        # Convert list back to tuple
        w_tuple = tuple(w_list)
        size_in_bytes = str(sys.getsizeof(w_tuple)) + " bytes"
        context = {
            'w_list' : w_list,
            'w_tuple' : w_tuple,
            'size_in_bytes' : size_in_bytes,
        }
        return context
    