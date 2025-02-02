


inputClassesHeld=input("Enter Number of classes Held : ")
inputClassesAttended=input("Enter Number of classes Attended : ")
percetage = (float(inputClassesAttended)/float(inputClassesHeld))*(100)
print("Percentage = "+str(percetage))
if(percetage>=75 and percetage<=100):
    print("ELIGIBLE FOR EXAMS")
elif(percetage<75 and percetage>0):
    print("Not Eligible")
else:
    print