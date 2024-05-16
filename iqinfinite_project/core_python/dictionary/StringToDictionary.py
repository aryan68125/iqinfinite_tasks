# Convert dictionary string values to List of dictionaries
'''
Input : test_dict = {“Gfg” : “1:2:3”, “best” : “4:8:11”} 
Output : [{‘Gfg’: ‘1’, ‘best’: ‘4’}, {‘Gfg’: ‘2’, ‘best’: ‘8’}, {‘Gfg’: ‘3’, ‘best’: ’11’}] 
Explanation : List after dictionary values split.
 

Input : test_dict = {“Gfg” : “1:2:3”} 
Output : [{‘Gfg’: ‘1’}, {‘Gfg’: ‘2”}, {‘Gfg’: ‘3’}] 
Explanation : List after dictionary values split. 
'''
from collections import defaultdict

# Convert dictionary string values to List of dictionaries : Solution
class StringToDictionary:
    def __init__(self,var_dictionary):
        self.__dictionary = var_dictionary
    def get_dictionary(self):
        return self.__dictionary
    def string_to_dictionary(self):
        test_dict = self.__dictionary
        temp = defaultdict(dict)
        for key in test_dict:
         
            # iterate for each of splitted values
            for idx in range(len(test_dict[key].split(':'))):
                try:
                    temp[idx][key] = test_dict[key].split(':')[idx]
         
                # handle case with No value in split
                except Exception as e:
                    temp[idx][key] = None
        res = []
        for key in temp:
         
            # converting nested dictionaries to list of dictionaries
            res.append(temp[key])
        return str(res)