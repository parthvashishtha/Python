a = set() # Empty set created
print(type(a))

# Methods in sets
# 1. Addition
a.add(3)
a.add(4)
a.add(4) # Will not add duplicate item
a.add((2,3,4)) # Will add Tuple
# a.add([1,2,3]) # Cannot add list or dictionary to sets coz they can be changed further

print(a)

# Length of a set 
print(len(a))

# Removing an element in a set

a.remove(3)
print(a)

# For removing any random element use pop

a.pop()
print(a)
