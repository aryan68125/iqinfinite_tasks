# Using os.path.exists() Function
'''
This method will check whether a file exists or not by passing the name of the file as a parameter. 
OS module has a sub-module named PATH by using which we can perform many more functions. 
'''
import os 
#importing os module

result = os.path.exists("os_close.py") #giving the name of the file as a parameter.

print(result)