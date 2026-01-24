#Sequence of characters, using the single quote or double quote
#String and it's Operations
mystring = "python is cool"
#Returns values from 0 to 5
print(mystring[0:5])
#Returns with skipping one letter
print(mystring[::2])
#Reversing the String
print(mystring[::-1])
# Concetination can also be done in string
print(mystring+"language")
# mystring.(press tab) gives inbuilt function of python on strings few examples are
mystring.split('t') #Splits string from strart into substrings
mystring.upper() #Converts all` characters to uppercase
mystring.lower() #Converts all characters to lowercase  
mystring.capitalize() #Capitalizes first character of string
mystring.find('is') #Finds the starting index of substring 'is'
mystring.replace('cool', 'awesome') #Replaces substring 'cool' with 'awesome'
#String Formatting
name = "Aditya"
age = 30
#Using f-strings (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")
#Using format() method
print("My name is {} and I am {} years old.".format(name, age)) #Positional formatting
print("My name is {0} and I am {1} years old.".format(name, age)) #Indexed formatting
#Assigning values to variables in format method
print("My name is {name} and I am {age} years old.".format(name=name, age=age))
print("My name is {} and I have three friends {a}, {b}, {c}".format(name, a="Alice", b="Bob", c="Charlie"))
#Using % operator
print("My name is %s and I am %d years old." % (name, age)) # %s for string, %d for integer
#Escape Sequences in Strings
print("Hello\nWorld") #New line escape sequence
print("Hello\tWorld") #Tab escape sequence
print("He said, \"Hello World!\"") #Double quote escape sequence
print('It\'s a beautiful day!') #Single quote escape sequence
#Float Formatting in Strings
pi = 3.141592653589793
x = 123.456789
print(f"Value of pi up pi up to 2 decimal places: {pi:.2f}")
print(f"Value of x up to 3 decimal places: {x:1.3f}")
print("Value of pi up to 4 decimal places: {:.4f}".format(pi))
print("Value of x up to 2 decimal places: %.2f" % x) #to 2 decimal places: %.2f" % pi)
