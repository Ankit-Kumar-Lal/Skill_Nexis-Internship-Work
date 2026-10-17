# Find largest and smallest number in a list

numbers = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest number:", largest)
print("Smallest number:", smallest)