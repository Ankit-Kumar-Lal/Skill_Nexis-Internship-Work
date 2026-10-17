# Create a list and perform CRUD operations

list1 = []

while True:
    print("\n1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        n = input("Enter an element: ")
        list1.append(n)
        print("Element added.")

    elif ch == 2:
        print("List elements are:", list1)

    elif ch == 3:
        pos = int(input("Enter position to update: "))
        if pos >= 0 and pos < len(list1):
            n = input("Enter new element: ")
            list1[pos] = n
            print("Element updated.")
        else:
            print("Invalid position.")

    elif ch == 4:
        pos = int(input("Enter position to delete: "))
        if pos >= 0 and pos < len(list1):
            list1.pop(pos)
            print("Element deleted.")
        else:
            print("Invalid position.")

    elif ch == 5:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
