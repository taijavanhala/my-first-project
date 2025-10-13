def getArea(width, height):
    """Calculates and returns the area of a rectangle."""
    area = width * height
    return area


def askDimensions():
    """Prompts the user to enter width and height, returns them as floats."""
    width = float(input("Enter the width: "))
    height = float(input("Enter the height: "))
    return width, height


def main():
    """Main function controlling the program flow."""
    print("Program starting.")
    print()
    width, height = askDimensions()
    area = getArea(width, height)
    print()
    print(f"The area of the rectangle is {area:.2f}")
    print()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
