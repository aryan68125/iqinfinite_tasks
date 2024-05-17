# Creating a Directory
import os
directory = "GeeksforGeeks"
parent_dir = "D:/Pycharm projects/"
path = os.path.join(parent_dir, directory)

os.mkdir(path)
print("Directory '% s' created" % directory)
directory = "Rollex997"
parent_dir = os.getcwd()
mode = 0o666
path = os.path.join(parent_dir, directory)
os.mkdir(path, mode)
print("Directory '% s' created" % directory)