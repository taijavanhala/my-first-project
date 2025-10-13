def frameWord(pword):
    """Prints the given word inside a decorative frame."""
    frame = "*" * (len(pword) + 4)
    print(frame)
    print(f"* {pword} *")
    print(frame)
    return None


def main():
    """Main function that manages program flow."""
    print("Program starts...")
    print()  # Empty line
    user_word = input("Please enter a word: ")
    print()  # Empty line before frame
    frameWord(user_word)
    print()  # Empty line
    print("Program ends.")
    return None


if __name__ == "__main__":
    main()
