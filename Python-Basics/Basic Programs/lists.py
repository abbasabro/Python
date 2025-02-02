numbers=[1,5,2,6,3,4]
print(numbers)
print(numbers[-2])
print(numbers[3])
print(numbers[0:3])#Range of elements in list excluding last digit
print(type(numbers))#gives the type of the variable
mixlist=[1,True,"Helloo",9.0]
print(mixlist)
mixlist[-1]="Abbas"
print(mixlist)
mixlist.remove(1)#Removes the First Occurance of element
print(mixlist)
mixlist.append(56)#Add element at last 
print(mixlist)
mixlist.insert(1,"Welcome!")#Add at given index
print(mixlist)
print(len(mixlist))#Length of list
mixlist.clear()
print(mixlist)
numbers.sort()#Sort the list in ascendinf order
print(numbers)
numbers.sort(reverse=True)#Sort the list in descending order
print(numbers)
numbers.pop(3)#Remove Element at given index
print(numbers)
