# for i in range(1,10):
#     print('*'*i)
# course=''' 
# Hi, Abbas
# How are you doing


# Thanks for your help dude
# '''
# print(course)
# for x in range(3):
#     print('x'*x)  
#     for y in range(1,2):
#         print('x'*5)



numbers=[5,3,6,1,6,5,3,5,2,1,6,5,6]
# numbers.sort()
for i in numbers:
    if(numbers.count(i)>1):
        numbers.remove(i)
        print(numbers)
print(numbers)