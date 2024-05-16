'''
Extract digits from tuples list
'''

class ExtractDigits:
    def __init__(self,list_of_tuples):
        self.__list_of_tuples = list_of_tuples
    def get_list_of_tuples(self):
        return self.__list_of_tuples
    def extract(self):
        test_list = self.__list_of_tuples
        temp = ''.join([str(i) for sublist in test_list for i in sublist])
        result = set(temp)
        result = [int(i) for i in result]
        res = list(result)
        return res