mydict = {
      "Duniya":"World",
      "Ram"   :"Hindu God",
      "Dil"   :"Heart"

}
print("Given words are",mydict.keys())
a = input("Enter the word whose meaning you want to know\n")
# print("Meaning of this word is:",mydict[a])
# Below line will not throw an error
print("Meaning of this word is:",mydict.get(a))
