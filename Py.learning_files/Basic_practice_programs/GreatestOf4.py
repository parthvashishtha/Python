a = int(input("Enter first  number : \n"))
b = int(input("Enter second number : \n"))
c = int(input("Enter third  number : \n"))
d = int(input("Enter fourth number : \n"))

# if(a>b and a>c and a>d):
#     print("Greatest number is : ",a)
# if(b>c and b>d and b>a):
#     print("Greatest number is : ",b)
# if(c>a and c>b and c>d):
#     print("Greatest number is : ",c)
# if(d>a and d>b and d>c):
#     print("Greatest number is : ",d)
 
# Second method

if a>d:
    f1=a
else:
    f1=d;    
if b>c:
    f2=c
else:
    f2=b;

if f1>f2:
    print(str(f1) + " is the greatest number ")   
else: 
    print(str(f2) + " is the greatest number ")   
   

