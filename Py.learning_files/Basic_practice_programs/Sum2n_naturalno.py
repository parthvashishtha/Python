from tkinter import N


n = int(input("Enter the number upto which you want to sum: "))

sum=0
while n>0:
    sum=sum+n
    n=n-1

print("Sum is :",sum)     
    

