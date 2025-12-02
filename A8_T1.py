# A8_T1.py
# Menu-driven program with pause functionality (template-ready)
from time import sleep

def main():
    print("Program starting.")

    pause_duration = 1.0  # default pause duration in seconds

    while True:
        print("\nOptions:")
        print("1 - Set pause duration")
        print("2 - Activate pause")
        print("0 - Exit")

        choice = input("Your choice: ").strip()

        if choice == "0":
            print("Exiting program.")
            break

        elif choice == "1":
            try:
                pause_duration = float(input("Insert pause duration (s): "))
            except ValueError:
                print("Invalid input. Please insert a number.")

        elif choice == "2":
            print(f"Pausing for {pause_duration} seconds.")
            sleep(pause_duration)
            print("Unpaused.")

        else:
            print("Invalid choice. Try again.")

    print("\nProgram ending.")

if __name__ == "__main__":
    main()
