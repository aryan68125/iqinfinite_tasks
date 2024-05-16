# Remove keys with Values Greater than K ( Including mixed values )
'''


    Input : test_dict = {‘Gfg’ : 3, ‘is’ : 7, ‘best’ : 10, ‘for’ : 6, ‘geeks’ : ‘CS’}, K = 7 
    Output : {‘Gfg’ : 3, ‘for’ : 6, ‘geeks’ : ‘CS’} 
    Explanation : All values greater than K are removed. Mixed value is retained. 

    Input : test_dict = {‘Gfg’ : 3, ‘is’ : 7, ‘best’ : 10, ‘for’ : 6, ‘geeks’ : ‘CS’}, K = 1 
    Output : {‘geeks’ : ‘CS’} 
    Explanation : Only Mixed value is retained.

'''
# Remove keys with Values Greater than K ( Including mixed values ) : Solution
class RemoveKeysValuesInK:
    def __init__(self,test_dict,k):
        self.__test_dict = test_dict
        self.__k = k
    def get_dictionary(self):
        return self.__test_dict
    def get_k(self):
        return self.__k
    def remove_keys_with_values_greater_than_k(self):
        test_dict = self.__test_dict
        K = self.__k
        res = {}
        for key in test_dict:
           
            # testing for data type and then condition, order is imp.
            if not (isinstance(test_dict[key], int) and test_dict[key] > K):
                res[key] = test_dict[key]
        return res