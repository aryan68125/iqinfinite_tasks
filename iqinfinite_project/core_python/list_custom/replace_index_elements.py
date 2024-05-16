# Replace index elements with elements in Other List
'''
# Initializing lists
test_list1 = ['Gfg', 'is', 'best']
test_list2 = [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]
'''
# Replace index elements with elements in Other List : Solution

class ReplaceIndexElementsWithOtherListElement : 
    def __init__(self, var_list_one, var_list_two):
        self.__var_list_one = var_list_one
        self.__var_list_two = var_list_two
    def get_string(self):
        return self.__var_list_one
    def get_list_two(self):
        return self.__var_list_two
    def split_input(self):
        input_str = self.__var_list_one
        words = input_str.split()  # Split the input string into words
        result = []
        for word in words:
            # Try to convert each word to an integer
            try:
                number = int(word)
                result.append(number)
            except ValueError:
                result.append(word)
        return result
    def replace_index_element(self):
        var_list_two = self.__var_list_two
        var_list_one = self.split_input()
        res = [var_list_one[idx] for idx in var_list_two]
        return res
    
'''
def split_input(input_str):
    words = input_str.split()  # Split the input string into words
    result = []
    for word in words:
        # Try to convert each word to an integer
        try:
            number = int(word)
            result.append(number)
        except ValueError:
            result.append(word)
    return result

input_str = "I want 4 apples and 18 oranges"
output = split_input(input_str)
print(output)
'''