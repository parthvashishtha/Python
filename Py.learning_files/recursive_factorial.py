# Used to print factorial
# n = 4
# fact = 1
# for i in range(n):
#     fact=fact*(i+1)

# print(fact)

def factorial_recursive(n):
    if n==1 or n==0:
     return 1

    return n*factorial_recursive(n-1)

f= factorial_recursive(6) 
print(f)   
