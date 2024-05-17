import os
directory = "Ballistic1000"
# parent_dir = "D:/Pycharm projects/GeeksForGeeks/Authors"  
parent_dir = os.getcwd()
path = os.path.join(parent_dir, directory)
os.makedirs(path)
print("Directory '% s' created" % directory)
directory = "Barricade247"
parent_dir = os.getcwd()
mode = 0o666
path = os.path.join(parent_dir, directory)
os.makedirs(path, mode)
print("Directory '% s' created" % directory)