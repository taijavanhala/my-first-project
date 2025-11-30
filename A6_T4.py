print("Program starting.")
print("This program analyses a list of names from a file.")

filename = input("Insert filename to read: ")

print(f'Reading names from "{filename}".')
print("Analysing names...")

try:
    with open(filename, "r", encoding="utf-8") as file:
        lengths = []  # list of name lengths

        for line in file:
            name = line.strip()
            if name != "":
                lengths.append(len(name))

        if len(lengths) == 0:
            print("File contains no valid names.")
        else:
            count = len(lengths)
            shortest = min(lengths)
            longest = max(lengths)
            average = sum(lengths) / count

            print("Analysis complete!")
            print("#### REPORT BEGIN ####")
            print(f"Name count - {count}")
            print(f"Shortest name - {shortest} chars")
            print(f"Longest name - {longest} chars")
            print(f"Average name - {average:.2f} chars")
            print("#### REPORT END ####")

except FileNotFoundError:
    print("Error: File not found.")

print("Program ending.")
