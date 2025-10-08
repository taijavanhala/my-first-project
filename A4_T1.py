# Prompt user for two integers
start = int(input("Enter the first integer: "))
end = int(input("Enter the second integer: "))

# Use for-loop to iterate through the range
# If start <= end → count up
# If start > end → count down
if start <= end:
    for i in range(start, end + 1):
        print(i)
else:
    for i in range(start, end - 1, -1):
        print(i)
