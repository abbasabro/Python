f=open("Filing_read01.txt","r") # r refers to mode of reading other are w(writing), append(a) , Binary(b) , both(+)

line1=f.readline()

line2=f.readline()

line3=f.readline()

print(line1)
print(line2)
print(line3)

#if i try to read an other line there will be blank space

line4=f.readline()  #Shows Space only

print(line4)

f.close()