'''
A List Comprehension is concise way to create list in python
compact and easier to read than traditional Loops
[expresion for value in iterables condition]
'''

doubles = [x*2 for x in range(1,11)]
print(doubles)

numbers = [2,-2,5,-4,0,1,-3]
positives = [number for number in numbers if number>=0]
print(positives)