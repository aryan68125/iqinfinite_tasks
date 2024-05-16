'''
output : 
Hello
Welcome
to
GeeksforGeeks
'''
def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')