Letter= ''' Dear <|NAME|> 
 You are selected!
 Date : <|DATE|> '''

name = input("Enter your name:\n")
date= input("Enter the date:\n ")

Letter= Letter.replace("<|NAME|>",name)
Letter= Letter.replace("<|DATE|>",date)

print (Letter)
       
