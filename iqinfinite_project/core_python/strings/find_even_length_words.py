'''
Input: s = "This is a python language"
Output: This is python language

Input: s = "i am laxmi"
Output: am
'''
class FindEvenLengthWords:
  def __init__(self,word):
    self.__word = word
  def get_word(self):
    return self.__word
  def set_word(self,word):
    self.__word = word
  def find_even_length_words(self):
    w_string = self.__word
    s=w_string.split(" ") 
    for i in s: 
      #checking the length of words
      if len(i)%2==0: 
        print(f"\033[92mEven length string : {i}\033[97m")