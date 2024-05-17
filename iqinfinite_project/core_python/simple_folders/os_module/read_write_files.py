'''
Using os.popen() Function
This method opens a pipe to or from command. The return value can be read or written depending on whether the mode is ‘r’ or ‘w’.
'''
import os
fd = "GFG.txt"

file = open(fd, 'w')
file.write("Hello")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)

file = os.popen(fd, 'w')
file.write("Hello")