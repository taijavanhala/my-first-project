# Ask user to insert two integers
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

# Compare integers
if a == b:
    print("Integers are the same.")
elif a > b:
    print("First integer is greater.")
else:
    print("Second integer is greater.")

# Create sum
summa = a + b
print("Sum of the two integers is:", summa)

# Check parity
if summa % 2 == 0:
    print("Sum is even.")
else:
    print("Sum is odd.")
