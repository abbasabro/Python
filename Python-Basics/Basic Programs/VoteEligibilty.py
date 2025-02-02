inputAge=input("Enter You age?")
age=int(inputAge)
if(age>18 and age<100):
    print("Eligible for Vote")
elif(age<18 and age>0):
    print("Not Eligible")
else:
    print("Not Valid age")
