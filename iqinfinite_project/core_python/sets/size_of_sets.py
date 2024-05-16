# Size of the sets
'''
Set1 = {"A", 1, "B", 2, "C", 3}
Set2 = {"Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu"}
Set3 = {(1, "Lion"), ( 2, "Tiger"), (3, "Fox")}

Size of Set1: 736bytes
Size of Set2: 736bytes
Size of Set3: 224bytes
'''
# Size of the sets : Solution
import sys
class SizeOfSets:
    def __init__(self,sets1):
        self.__sets1 = sets1
    def get_sets(self):
        return self.__sets1
    def get_size(self):
        sets1 = self.__sets1
        size_of_sets1 = str(sets1.__sizeof__()) + "bytes"
        return size_of_sets1