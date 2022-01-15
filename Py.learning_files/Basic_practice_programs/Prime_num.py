
num = int(input("Enter the number: \n"))
prime = True
for i  in range(2,num):
    if (num%i==0):
        prime= False

if prime:
    print( "Given no. is prime")     
else:
    print( "Given no. is not prime")    



