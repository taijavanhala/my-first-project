# Initialize counters
word_count = 0
char_count = 0

# Start repetitive prompt
while True:
    word = input("Insert a word (empty to stop): ")

    # Stop if input is empty
    if word == "":
        break

    # Count words and characters
    word_count += 1
    char_count += len(word)

# After loop, print results
print(f"You inserted {word_count} words.")
print(f"The total number of characters is {char_count}.")
