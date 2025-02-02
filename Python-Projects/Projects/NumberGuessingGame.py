import random as r

computer_number = r.randint(1,100)

while True:
    try:
        guessed_number = int(input("Guess Number between 1 to 100 : "))
        if guessed_number > computer_number:
            print("Too High")
        elif guessed_number < computer_number:
            print("Too Low")
        else:
            print("Congrats You win 🥳")  
            break
    except ValueError:
        print("Enter a Valid Number")         