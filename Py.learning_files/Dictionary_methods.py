myDict = {
    "laptop" : "An electronic machine",
    "parth " : "A simple boy",
    "number" : [1,3,5],
    "anotherDict" : {"Parth": "Coder"}
}

# Dictionary methods 

print(myDict.keys())
print(list(myDict.keys())) # Prints the keys of dictionary
print(myDict.items()) # Prints the (keys,items) of the contents
print(myDict.values())
print(myDict)
updatedict = {
    "Lakshya" : "Brother",
    "Madhur"  : "Brother",
}
myDict.update(updatedict)
print(myDict)

print(myDict.get("parth ")) # Prints value associated with key parth 
print(myDict["parth "]) # Prints value associated with key parth 

# Difference between get method and [] syntac dictionaries

print(myDict.get("Parth1")) # Returns none as Parth1 is not present in dictionary
print(myDict["Parth1"]) # Throws an error because Parth1 is nor present in dictionary
