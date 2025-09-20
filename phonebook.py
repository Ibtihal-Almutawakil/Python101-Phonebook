# Phonebook dictionary
phonebook = {
    "Amal": "1111111111",
    "Mohammed": "2222222222",
    "Khadijah": "3333333333",
    "Abdullah": "4444444444",
    "Rawan": "5555555555",
    "Faisal": "6666666666",
    "Layla": "7777777777"
}

# Function to validate the phone number
def is_valid_number(number):
    return number.isdigit() and len(number) == 10

# Function to search by phone number
def search_by_number():
    number = input("Enter the phone number: ")
    
    if not is_valid_number(number):
        print("This is invalid number")
        return
    
    for name, phone in phonebook.items():
        if phone == number:
            print(f"Name: {name}")
            return
    
    print("Sorry, the number is not found")

# Function to search by name
def search_by_name():
    name = input("Enter the name: ")
    
    if name in phonebook:
        print(f"{name}'s phone number: {phonebook[name]}")
    else:
        print("Sorry, this name is not found")

# Function to add a new entry to the phonebook
def add_new_entry():
    name = input("Enter the new person's name: ")
    number = input("Enter the phone number: ")
    
    if not is_valid_number(number):
        print("This is invalid number")
        return
    
    if name in phonebook:
        print(f"{name} is already in the phonebook.")
    else:
        phonebook[name] = number
        print(f"{name} has been added successfully!")

# User interface
def main():
    while True:
        print("\n1. Search by phone number")
        print("2. Search by name")
        print("3. Add a new entry")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            search_by_number()
        elif choice == "2":
            search_by_name()
        elif choice == "3":
            add_new_entry()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

# Run the program
main()
