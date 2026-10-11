# Student Grade Calculator:

m1 = float(input("Enter marks in subject 1: "))
m2 = float(input("Enter marks in subject 2: "))
m3 = float(input("Enter marks in subject 3: "))

avg = (m1 + m2 + m3) / 3

print("Average =", avg)

if avg >= 90:
    print("Grade A")
elif avg >= 75:
    print("Grade B")
elif avg >= 60:
    print("Grade C")
elif avg >= 40:
    print("Grade D")
else:
    print("Fail")
