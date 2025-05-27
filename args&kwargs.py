/*
In this code we will be understanding *args and **kwargs in Python.
*args allows you to pass a variblr number of positional arguments to a function.
**kwargs allows you to pass a varuable number of keyword arguments to a function. 
*/
def add(*args):
    return sum(args)
    add(1,2,3,4,5)
    print(add(1,2,3,4,5))
for item in args:
    print(item)


