# Extract elements with Frequency greater than K
'''
nput : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3 
Output : [4, 3] 
'''
# Extract elements with Frequency greater than K : Solution
class ExtractElements:
    def __init__(self,var_list):
        self.__var_list = var_list
    def get_list(self):
        return self.__var_list
    def extract_elements_frequency_greater_than_k(self,K):
        input_list = self.__var_list
        res = [] 
        for i in input_list: 
             
            # using count() to get count of elements
            freq = input_list.count(i) 
             
            # checking if not already entered in results
            if freq > K and i not in res: 
                res.append(i)
        return res
            
