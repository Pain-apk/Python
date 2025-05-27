# In this code we will be understanding *args and **kwargs in Python.
# *args allows you to pass a variable number of positional arguments to a function.
#  **kwargs allows you to pass a variable number of keyword arguments to a function.

def add(*args):
    for item in args:
        print(item)
    return sum(args)

print(add(1, 2, 3, 4, 5))

def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
            print("My favourite fruit is {}".format(kwargs['fruit']))
    else:
            print("No fruit found")


myfunc(fruit='apple', veggie='lettuce', jelly='grape')

def myfunc2(*args, **kwargs):
      print("I would like {} {}".format(args[0], kwargs['food']))
myfunc2(1,2, 3, food = "sandwich")
def myfunc(s):
    result = []
    for i, c in enumerate(s):
        if i % 2 == 0:
            result.append(c.upper())
        else:
            result.append(c.lower())
    return ''.join(result)

print(myfunc("Aditya"))  # Output: AdItYa
