a = {1, 2 , 3, 4}
print(type(a))

# It's a collection of non empty elements
# As shown below it will ignore 4

a = {1,2,3,4,5,4}
print(a)

b = {} # This syntax will create an empty dictionary not an empty set
print(type(b))

# For an empty set we have to use this
c = set()
print(type(c))


