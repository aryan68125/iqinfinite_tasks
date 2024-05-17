'''
Using os.close() Function
Close file descriptor fd. A file opened using open(), can be closed by close()only. But file opened through os.popen(), 
can be closed with close() or os.close(). If we try closing a file opened with open(), using os.close(), Python would throw TypeError
'''
import os
fd = "GFG.txt"
file = open(fd, 'r')
text = file.read()
print(text)
os.close(file)