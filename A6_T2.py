# A6_T2 – Write text file

# Ask user input
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
file_name = input("Enter file name for writing (example: names.txt): ")

try:
    # Open file and write content
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(first_name + "\n")
        f.write(last_name + "\n")
        f.write("\n")  # empty line at the end

    print(f"File '{file_name}' written successfully.")

except Exception as e:
    print("An error occurred:", e)

print("Program exited cleanly.")
