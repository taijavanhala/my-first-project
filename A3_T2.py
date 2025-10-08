# Prompt user to insert a word
word_first = input("Enter a word: ")

# Prompt user to insert a character
character = input("Enter a character: ")

# Check if the character exists in the word
if character in word_first:
    print(f'Word "{word_first}" contains character "{character}"')
else:
    print(f'Word "{word_first}" doesn\'t contain character "{character}"')

# Prompt user to insert one more word
word_second = input("Enter another word: ")

# Compare the words alphabetically
if word_first == word_second:
    print(f'Both inserted words are the same alphabetically, "{word_first}"')
elif word_first < word_second:
    print(f'The first word "{word_first}" is before the second word "{word_second}" alphabetically.')
else:
    print(f'The second word "{word_second}" is before the first word "{word_first}" alphabetically.')
