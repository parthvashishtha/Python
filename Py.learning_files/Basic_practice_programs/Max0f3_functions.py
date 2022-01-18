def Max(num1,num2,num3):
    if(num1>num2):
       if(num1>num3):
           return num1

    else:
      
        if(num2>num3):
           return num2

        else:
          return num3

m = Max(12,35,40)
print("Maximum of these three is: ",str(m))                  
