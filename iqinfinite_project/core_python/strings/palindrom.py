# Palindrome 
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
# Palindrome : Solution

class Palindrome:
    def __init__(self, ch_string):
        self.__ch_string = ch_string
    def get_ch_string(self):
        return self.__ch_string
    def set_ch_string(self,ch_string):
        self.__ch_string = ch_string
    def check_palindrome(self):
        word = self.__ch_string
        mid = (len(word))//2
        start = 0
        last = len(word)-1
        flag = 0
        while(start<=mid):
            if word[start] == word[last]:
                start+=1
                last-=1
                flag=0
            else:
                flag=1
                break
        if flag==0:
            print(f"\033[92mThe word '{word}' is a Palindrome \033[97m")
        else:
            print(f"\033[92mThe word '{word}' is not a Palindrome \033[97m")