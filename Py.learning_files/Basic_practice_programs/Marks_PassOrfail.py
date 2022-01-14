print("Scores of Student")

m = int(input("Enter the score of Maths\n"))
e = int(input("Enter the score of English\n"))
h = int(input("Enter the score of Hindi\n"))

if(m/100>=0.33 and e/100>=0.33 and h/100>=0.33 and (m+e+h)/100>=0.40):
    print("Pass")
    
else:
    print("Fail")    


