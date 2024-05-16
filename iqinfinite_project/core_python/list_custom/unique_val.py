# count unique values inside a list
'''
input_list = [1, 2, 2, 5, 8, 4, 4, 8]
No of unique items are: 5
'''
# count unique values inside a list : solution
class UniqueItemsList:
    def __init__(self,input_list):
        self.__var_list = input_list
    def get_list(self):
        return self.__var_list
    def get_unique_elements_count(self):
        input_list = self.__var_list
        l = []
        count = 0
        for element in input_list:
            if not element in l:
                count+=1
                l.append(element)
        context = {
            'input_list' : input_list,
            'unique_element_count' : count,
            'unique_elements_list' : l
        }
        return context
            