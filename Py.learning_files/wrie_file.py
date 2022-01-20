# This is for writing in a file
# and if something is written already in the file it will override
f = open('sample.txt','w')
f.write("Dil se sab ka shukriya")

f.write("Dil se sab ka shukriya")

f.write("Dil se sab ka shukriya")
f.close()

# This will append the sentence in the line
f=open('sample.txt','a')
f.write('This is for append')
f.close()
