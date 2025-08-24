# There are two types of String Interpolation in python
#1. f-Strings (formatted string literals)
#2. str.format() method

# f-strings can be used to embed experssion inside string literals, using curly braces '{}'
name = "Aditya"
age = 20
print(f"My name is {name} and I am {age} years old.")
# str.format() method can be used to format strings
print("My name is {} and I am {} years old.".format(name, age))
# You can also use the % foperator for String Interpolation
print("My name is %s and I am %d years old." % (name, age))
