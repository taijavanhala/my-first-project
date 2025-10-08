# Prompt user for two integers
start = int(input("Enter the first integer: "))
end = int(input("Enter the second integer: "))

# Use for-loop to iterate through the range
if start <= end:
    for i in range(start, end + 1):
        # print numbers on the same line separated by spaces
        if i != end:
            print(i, end=" ")
        else:
            print(i)
else:
    for i in range(start, end - 1, -1):
        if i != end:
            print(i, end=" ")
        else:
            print(i)
