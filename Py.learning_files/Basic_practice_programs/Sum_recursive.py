def sum_recursive(n):
    if n==0:
        return 0
    return n+sum_recursive(n-1)

n = input("Enter the number upto which you want the sum : ")
t=(sum_recursive(5)) 
print(f"Sum upto {n} is : ", str(t) )   
