# Anagrams together in Python using List and Dictionary
'''
                Input: arr = [‘cat’, ‘dog’, ‘tac’, ‘god’, ‘act’]
                Output: ‘cat tac act dog god’
'''
# Anagrams together in Python using List and Dictionary : Solution
from collections import Counter
class AllAnagram:
    def __init__(self, var_list):
        self.__var_list = var_list
    def get_list(self):
        return self.__var_list
    def all_anagram(self):
        var_list = self.__var_list
        dict = {}
        for strVal in var_list:
            key = ''.join(sorted(strVal))
            if key in dict.keys():
                dict[key].append(strVal)
            else:
                dict[key] = []
                dict[key].append(strVal)
        output = ""
        for key,value in dict.items():
            output = output + ' '.join(value) + ' '
        return output        



# Function to find the size of largest subset 
'''
Input: 
ant magenta magnate tan gnamate
Output: 3
Explanation
Anagram strings(1) - ant, tan
Anagram strings(2) - magenta, magnate,
                     gnamate
Thus, only second subset have largest
size i.e., 3

Input: 
cars bikes arcs steer 
Output: 2
'''
# Function to find the size of largest subset : Solution

class LargeSubsetsOfAnagram:
    def __init__(self, var_string):
        self.__input = var_string
    def get_string(self):
        return self.__input
    def maxAnagramSize(self):
        var_string = self.__input
        # split input string separated by space
        input = var_string.split(" ")
     
        # sort each string in given list of strings
        for i in range(0,len(input)):
             input[i]=''.join(sorted(input[i]))
     
        # now create dictionary using counter method
        # which will have strings as key and their 
        # frequencies as value
        freqDict = Counter(input)
     
        # get maximum value of frequency
        return max(freqDict.values())        