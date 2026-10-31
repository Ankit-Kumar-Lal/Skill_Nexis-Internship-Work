# 1. Contact Book App Using Dictionary

contacts = {}


# Function to add a contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")

    contacts[name] = phone
    print("Contact added successfully!")


# Function to search for a contact
def search_contact():
    name = input("Enter name to search: ")

    if name in contacts:
        print("Name:", name)
        print("Phone Number:", contacts[name])
    else:
        print("Contact not found!")


# Function to update a contact
def update_contact():
    name = input("Enter name to update: ")

    if name in contacts:
        phone = input("Enter new phone number: ")
        contacts[name] = phone
        print("Contact updated successfully!")
    else:
        print("Contact not found!")


# Function to delete a contact
def delete_contact():
    name = input("Enter name to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")


# Function to display all contacts
def display_contacts():
    if not contacts:
        print("Contact book is empty.")
    else:
        print("\n--- Contact List ---")

        for name, phone in contacts.items():
            print("Name:", name, "| Phone:", phone)


# Main program
while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        search_contact()

    elif choice == "3":
        update_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        display_contacts()

    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")

        