# Prompt user for two integers
start = int(input("Enter the first integer: "))
end = int(input("Enter the second integer: "))

# Use while-loop to print numbers between start and end
if start <= end:
    current = start
    while current <= end:
        print(current)
        current += 1
else:
    current = start
    while current >= end:
        print(current)
        current -= 1
