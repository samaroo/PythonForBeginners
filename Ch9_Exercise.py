# Notes
# 
# Tuples
#
# Just lists that can't be changed
# Defined with parentheses
# Access elements in tuple like a list []
# "len(t)" where t is a tuple will return the amount of elements in the tuple
# "min(t)" where t is a tuple wlll return the minimum elements in the tuple
# "max(t)" where t is a tuple wlll return the maximum elements in the tuple
# "tuple(l)" where l is a list, will return a tuple version of a list
#
# Dictionaries
#
# Defined with curly braces {}
#   randomList = {key1 : value1, key2 : value2, key3 : value3}
# Each key must be unique but values dont have to be unique
# Everything in a dictionary can be modified
# Keys can be added and removed from dictionary
# "del d[k]" where d is a dictionary and k is a valid key, will delete the pair from the dicitonary
# "d.clear()" will empty everything from dictionary d
# "d.get(k)" will return the value at key k if it is valid and will return "None" if not
# "d.items()" will return a list of each key and value in the dictionary
# "d.values()" will return a list of values in a dictionary
# "d.keys()" will return a list of keys in a dicitonary

# generate an average gpa from the tuple

gpas = (3.14, 3.45, 3.98, 2.55, 3.24, 2.27)
sum = 0
for i in gpas:
    sum+= i;

print("The average GPA is:", sum / len(gpas))

# given names and gpas, make a dictionary

gpasDictionary = {"Bob" : 3.14, "Mark" : 3.45, "Melissa" : 3.98, "Travis" : 2.55, "DeeDee" : 3.24, "Ian" : 2.27}

# calculate the average gpa

sum = 0
for i in gpasDictionary.values():
    sum += i

print("The average GPA is:", sum / len(gpas))