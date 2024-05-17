# Deleting Directory or Files using Python
# delete a file inside a folder
import os 
file = 'file1.txt'
# location = "D:/Pycharm projects/GeeksforGeeks/Authors/Nikhil/"
location = os.getcwd() + "/Ballistic1000/"
path = os.path.join(location, file) 
os.remove(path) 

# delete a folder
import os 
directory = "Ballistic1000"
# parent = "D:/Pycharm projects/"
parent = os.getcwd()
path = os.path.join(parent, directory) 
os.rmdir(path) 