# Using os.error Function
import os
try:
    filename = 'GFG.txt'
    f = open(filename, 'rU')
    text = f.read()
    f.close()
except IOError:
  print('Problem reading: ' + filename)