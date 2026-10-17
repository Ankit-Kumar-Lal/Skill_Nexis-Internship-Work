# Contact Book using Dictionary

contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display Contacts")
    print("6. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added successfully.")

    elif ch == "2":
        name = input("Enter name to search: ")
        if name in contacts:
            print("Phone number:", contacts[name])
        else:
            print("Contact not found.")

    elif ch == "3":
        name = input("Enter name to update: ")
        if name in contacts:
            phone = input("Enter new phone number: ")
            contacts[name] = phone
            print("Contact updated.")
        else:
            print("Contact not found.")

    elif ch == "4":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif ch == "5":
        print("Contact Book:", contacts)

    elif ch == "6":
        break

    else:
        print("Invalid choice.")
