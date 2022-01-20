
from pydoc import text

#  It will print firs line
f = open('sample.txt') # By default it will take read mode
text = f.readline()
print(text)

#  it will print second line
text = f.readline()
print(text)

#  it will print third line
text = f.readline()
print(text)
