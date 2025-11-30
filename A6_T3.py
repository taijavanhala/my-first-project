# A6_T3 – Copy text file

# Ask file names from user
source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

try:
    # Read from source file
    with open(source, "r", encoding="utf-8") as src:
        content = src.read()

    # Write to destination file
    with open(destination, "w", encoding="utf-8") as dst:
        dst.write(content)

    print(f"File copied successfully from '{source}' to '{destination}'.")

except FileNotFoundError:
    print("Error: The source file does not exist.")

except Exception as e:
    print("An unexpected error occurred:", e)

print("Program exited cleanly.")
