# We are using map function to apply a
# function to all it elements of an iterable (like a list).
# The map function returns a map object (which is an iterator), 
# so we need to convert it to a list or another iterable type.

def square(x):
    return x**2
num = [1,2,3,4,5]
squared = list(map(square,num))
print(squared)
def str(s):
    if len(s)%2 == 0:
        return s.upper()
    else:
        return s.lower()
name = ["Aditya", "Sumit", "Aman", "Yohan"]
str_list = list(map(str, name))
print(str_list)
# Now we will use filter function to filter out elements from an iterable
# based on a condition.
# The filter function returns a filtered object (which is an iterator),
# so we need to convert it to a list or another iterable type.
def is_even(y):
    return y%2 == 0
num = [1,2,3,4,5,6,7,8]
even_num = list(filter(is_even, num))
print(even_num)
# Now we will use lambda experssion to create samll anonymous functions.
# Lambda function are often used with map and filter functions.
#example
def sqx(x):
    return x**2
#same function using lambda experssion

square = lambda num: num**2
square(2)
#output 4
# Now we will use lambda expression with map function
list(map(lambda x: x**2, [1,2,3,4,5]))

