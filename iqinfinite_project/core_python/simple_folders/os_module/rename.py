# Using os.rename() Function
'''
A file old.txt can be renamed to new.txt, using the function os.rename(). 
The name of the file changes only if, the file exists and the user has sufficient privilege permission to change the file.
'''
import os
fd = "GFG.txt"
os.rename(fd,'New.txt')
os.rename(fd,'New.txt')
