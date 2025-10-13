def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def main():
    print("Collatz Conjecture 1 - 10")
    print("--------------------------")
    try:
        number = int(input("Enter an integer: "))
        if number <= 0:
            print("Please enter a positive integer greater than zero.")
            return

        sequence = collatz_sequence(number)
        print(" → ".join(map(str, sequence)))

    except ValueError:
        print("Invalid input! Please enter an integer.")


if __name__ == "__main__":
    main()
