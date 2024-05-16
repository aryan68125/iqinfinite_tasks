# Python program to sort a list of tuples alphabetically
'''
Input: [("Amana", 28), ("Zenat", 30), ("Abhishek", 29), ("Nikhil", 21), ("B", "C")]
Output: [('Amana', 28), ('Abhishek', 29), ('B', 'C'), ('Nikhil', 21), ('Zenat', 30)]
'''
# Python program to sort a list of tuples alphabetically : solution
class SortTuplesAlpha:
    def __init__(self,var_list):
        self.__var_list = var_list
    def get_list(self):
        return self.__var_list
    def sort_tuples_based_on_alphabets(self):
        tup = self.__var_list
        n = len(tup)
         
        for i in range(n):
            for j in range(n-i-1):
                 
                if tup[j][0] > tup[j + 1][0]:
                    tup[j], tup[j + 1] = tup[j + 1], tup[j]
        return tup