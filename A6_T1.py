# A6_T1 Read Text File

def main():
    filename = input("Enter the filename (e.g., A6_T1_D1.txt): ").strip()

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        print(f'#### START "{filename}" ####')
        print(content, end="" if content.endswith("\n") else "\n")
        print(f'#### END "{filename}" ####')

    except FileNotFoundError:
        print(f'Error: File "{filename}" not found.')
    except PermissionError:
        print(f'Error: No permission to read "{filename}".')
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
