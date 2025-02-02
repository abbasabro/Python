import random as r
counter = 0
while True :
    choice = input("Do You want to play (y/n) :").upper()
    if(choice=='Y'):
        counter +=1
        r1=r.randint(1,6)
        r2=r.randint(1,6)
        print(f"({r1},{r2})")
    elif choice=='N':
        print(f"Dice Rolled for {counter} times")
        print("Thanks for Playing ❤️") 
        break
    else:
        print("Invalid Choice")         

