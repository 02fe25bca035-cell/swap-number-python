num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))

print("\nbefore swapping:")
print("first number:",num1)
print("second number:",num2)

num1, num2 = num2, num1

print("\nAfter swapping:")
print("first number:",num1)
print("second number:",num2)