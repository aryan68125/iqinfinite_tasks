# Python program to find tuples which have all elements divisible by K from a list of tuples 
'''
Python program to find tuples which have all elements divisible by K from a list of tuples


    Input : test_list = [(6, 24, 12), (60, 12, 6), (12, 18, 21)], K = 6 
    Output : [(6, 24, 12), (60, 12, 6)] 
    Explanation : Both tuples have all elements multiple of 6.

    Input : test_list = [(6, 24, 12), (60, 10, 5), (12, 18, 21)], K = 5 
    Output : [(60, 10, 5)] 
    Explanation : Multiple of 5 tuples extracted. 

    Test your self ::
    [(6, 24, 12), (1, 2, 3), (60, 12, 6), (4, 5, 6), (12, 18, 21), (7, 8, 9)]
'''
# Python program to find tuples which have all elements divisible by K from a list of tuples : Solution
class TuplesDividedByK:
    def __init__(self,number_of_tuples,size_of_tuple,k):
        self.__size_of_a_list = number_of_tuples
        self.__size_of_a_tuple = size_of_tuple
        self.__divided_by = k

    #number of tuples
    def get_number_of_tuples(self):
        return self.__size_of_a_list
    def set_number_of_tuples(self,number_of_tuples):
        self.__size_of_a_list = number_of_tuples
    #size of the tuple
    def set_size_of_a_tuple(self,size_of_tuple):   
        self.__size_of_a_tuple = size_of_tuple
    def get_size_of_a_tuple(self):
        return self.__size_of_a_tuple
    #divided by 
    def get_divided_by(self):
        return self.__divided_by
    def set_divided_by(self,divided_by):
        self.__divided_by = divided_by

    def divisible_by_k(self):
        list_size = int(self.__size_of_a_list)
        tuple_size = int(self.__size_of_a_tuple)
        divided_by = int(self.__divided_by)
        outer_list = []
        inner_list = []
        for i in range(0,list_size):
            print(f"\033[95mFor tuple {i} Enter elements : \033[97m")
            for j in range(0,tuple_size):
                element = int(input())
                inner_list.append(element)
            w_tuple = tuple(inner_list)
            outer_list.append(w_tuple)
            inner_list.clear()
        test_list = outer_list
        K = divided_by
        res = [sub for sub in test_list if all(ele % K == 0 for ele in sub)]
        context = {
            'list_size':list_size,
            'tuple_size':tuple_size,
            'divided_by':divided_by,
            'outer_list':outer_list,
            'res':res,
        }
        return context
