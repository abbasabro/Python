num1=input("Enter First Number : ")
num2=input("Enter Second Number : ")
sum=int(num1)+int(num2)
minus=int(num1)-int(num2)
product=int(num1)*int(num2)
power=int(num1)**int(num2)
divide1=float(num1)/float(num2)#(/)returns Floating
divide2=int(num1)//int(num2)#(//)returns integer
remainder=int(num1)%int(num2)
print("Addition of "+num1+" + "+num2+" = "+str(sum))
print("Subtraction = "+str(minus))
print("Product = "+str(product))
print("Power = "+str(power))
print("Division in Floating = "+str(divide1))
print("Division in Integer = "+str(divide2))
print("Remainder = "+str(remainder))
print("Augmented Assignment Operator")
num1+=10#(+=)augmented assignment operator
print(num1)
print("Operation Precedence")
x=2+3*6
print(x)
x=(2+3)*6#()operation precedence
print(x)
