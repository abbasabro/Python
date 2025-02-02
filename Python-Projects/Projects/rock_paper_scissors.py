import random as r
ROCK='r'
SCICCORS='s'
PAPER = 'p'
emojis = {
    ROCK : "🪨",
    PAPER : "📃",
    SCICCORS : "✂️"
}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_input = input("Rock Paper or Sccisors (r,p,s) ").lower()
        if user_input in choices:
            return user_input
        else:
            print("Invalid Choice!")    


def display_choice(user_input,computer_choice):
    print(f"You Choose {emojis.get(user_input)}")
    print(f"Computer Choose {emojis.get(computer_choice)}")


def find_winner(user_input,computer_choice):
    if user_input==computer_choice:
        print("Tie")
    elif(
        (user_input == SCICCORS and computer_choice == PAPER) or
        (user_input == PAPER and computer_choice == ROCK) or
        (user_input == ROCK and computer_choice == SCICCORS)):
            print("You Win")
    else:       
        print("You Lose")


def play_game():
    while True:
        user_input=get_user_choice()
        computer_choice = r.choice(choices)

        display_choice(user_input,computer_choice)

        find_winner(user_input,computer_choice)
        
        continue_input = input("Do You want to continue (y/n): ").lower()
        if continue_input=='n':
            break

play_game()
        


