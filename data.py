#Data Types in Python
#1)Lists Ordered Sequence of Objects
myList = ['One', 'two' ,'three']

# 2) Integers Whole Numbers with int as type and float for decimal numbers
myInt =7
myfloat = 7.5
# 3) Strings sequence of characters
mystring = "Yo python"
# Indexing starts at 0 to N and -1 to -N for reverse indexing

# 4) Disctionaries key value pairs
mydict = {'name': 'john', 'age': 25}
# 5) Tuples are Ordered sequence of objects similar to lists but immutable ie cannot be changes
mytuple = ('one', 'two', 'three')
# 6) Sets are unordered collection of unique objects
myset = {'one', 'two', 3}
# Key Differences Between Lists and Sets
# While both can store mixed types, they behave differently:
# Order: Lists maintain the order of items, while sets are unordered.
# Duplicates: Lists allow multiple copies of the same value; sets only store unique items.
# Mutability of Items: You can put mutable objects (like other lists) inside a list, but you cannot put them inside a set.
# Sets are faster than lists for membership tests (checking is an item is in the collection)
# because they use a hash table internally and lists require a linear search.
# 7) Booleans represent True or False vallues
mybool = True
# 8) NoneType represents the abscence of a value
# It is often used to signify 'no value' or null value
mynone = None
