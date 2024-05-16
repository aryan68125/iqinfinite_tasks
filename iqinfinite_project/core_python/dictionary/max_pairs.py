# Dictionary with maximum count of pairs
'''
     Input : test_list = [{“gfg”: 2, “best” : 4}, {“gfg”: 2, “is” : 3, “best” : 4, “CS” : 9}, {“gfg”: 2}]
    Output : 4
    Explanation : 2nd dictionary has maximum keys, 4.

    Input : test_list = [{“gfg”: 2, “best” : 4}, {“gfg”: 2}]
    Output : 2
    Explanation : 1st dictionary has maximum keys, 2. 
'''
# Dictionary with maximum count of pairs : Solution

class MaxPairs:
    def __init__(self,test_list):
        self.__test_list = test_list
    def get_list(self):
        return self.__test_list
    def max_pair(self):
        res = {}  
        test_list = self.__test_list
        max_len = 0
        for ele in test_list: 
              
            # checking for lengths 
            if len(ele) > max_len:  
                res = ele 
                max_len = len(ele) 
                  
        # printing results 
        return res