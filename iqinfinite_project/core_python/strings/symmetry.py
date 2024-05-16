# Symmetry 
'''
Input: khokho
Output: 
The entered string is symmetrical
The entered string is not palindrome

Input:amaama
Output:
The entered string is symmetrical
The entered string is palindrome

A string is said to be symmetrical if both the halves of the string are the same and a string is said to be a palindrome string if 
one half of the string is the reverse of the other half or if a string appears the same when read forward or backward
'''
# Symmetry : Solution

class Symmetry:
    def __init__(self, ch_string):
        self.__ch_string = ch_string
    def get_ch_string(self):
        return self.__ch_string
    def set_ch_string(self,ch_string):
        self.__ch_string = ch_string
    def check_symmetry(self):
        word = self.__ch_string
        start1 = 0
        last = len(word)
        if len(word) % 2:
            mid = len(word)//2 + 1
        else:
            mid = len(word)//2
        start2 = mid
        flag = 0
        while(start1 <= mid and start2 <= last-1):
            if word[start1] == word[start2]:
                start1 += 1
                start2 += 1
            else:
                flag=1
                break
        if flag==0:
            print(f"\033[92mThe word '{word}' is symmetrical\033[97m")
        else:
            print(f"\033[92mThe word '{word}' is not symmetrical\033[97m")