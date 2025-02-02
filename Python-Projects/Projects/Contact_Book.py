contact_book = {}
def make_choice():
    try:
        choice = int(input('''
        What Do want to do?
        1.Add a new contact.
        2.Search for a contact by name.
        3.Delete or update a contact.
        4.Display all contacts sorted alphabetically 
        5.Exit
        Press Given Number (1/2/3/4/5) :               
        '''))
        return choice
    except ValueError:
        print("Invalid Value")


def search_contact(contact):
    if contact not in contact_book.keys():
        return f'{contact} not found!'
    else:
        return f'{contact} is {contact_book.get(contact)}'

def update_contact(contact):
    if contact not in contact_book.keys():
        return f'{contact} not found!'
    else:
        try:
            new_number = int(input("Enter New Number : "))
            contact_book[contact] = new_number
            return f'{contact} has been` Updated!'
        except ValueError:
            return "Invalid number entered."

def show_item():
    if not contact_book:
        print("Contact book is empty.")
    else:   
        for name , number in sorted(contact_book.items()):
         print(f'{name} : {number}')

while True:
    choice = make_choice()
    if(choice == 1):
        name = input("Enter Contact Name : ")
        number = int(input("Enter Contact Number : "))
        contact_book.update({name : number})
    elif choice == 2:
        name = input("Enter Contact Name to search : ")  
        print(search_contact(name))
    elif choice == 3:
        name = input("Enter Contact Name to update : ")  
        print(update_contact(name))    
    elif choice == 4:
        show_item() 
    elif choice == 5:
        break
    else:
        print("Invalid")

