# Create a function called _if which takes 3 arguments: a boolean value bool and 2 functions (which do not take any parameters): func1 and func2

def _if(bool, func1, func2):
    if bool:
        func1()
    else:
        func2()