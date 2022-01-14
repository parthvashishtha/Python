for i in range(10):
    print(i)
    if i==5:
       break
else: # This will not execute coz loop is not fully terminated
    print("This lies under else of for")    
