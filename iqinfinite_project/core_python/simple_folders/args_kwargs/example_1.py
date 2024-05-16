'''
Here, we are passing *args and **kwargs as an argument in the myFun function. 
where ‘geeks’, ‘for’, ‘geeks’ is passed as *args, and first=”Geeks”, mid=”for”, last=”Geeks”  
is passed as **kwargs and printing in the same line.
output:
args: ('geeks', 'for', 'geeks')
kwargs: {'first': 'Geeks', 'mid': 'for', 'last': 'Geeks'}
'''
def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")