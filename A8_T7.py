# A8_T7.py
# SVG program: draw squares, circles and regular hexagons (bestagons!)

import math
from svgwrite import Drawing
from svgwrite.shapes import Rect, Circle, Polygon


def drawSquare(PDwg: Drawing) -> None:
    print("Insert square")
    left = float(input("- Left edge position: "))
    top = float(input("- Top edge position: "))
    side = float(input("- Side length: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")

    square = Rect(
        insert=(left, top),
        size=(side, side),
        fill=fill,
        stroke=stroke,
    )
    PDwg.add(square)


def drawCircle(PDwg: Drawing) -> None:
    print("Insert circle")
    cx = float(input("- Center x position: "))
    cy = float(input("- Center y position: "))
    radius = float(input("- Radius: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")

    circle = Circle(
        center=(cx, cy),
        r=radius,
        fill=fill,
        stroke=stroke,
    )
    PDwg.add(circle)


def drawHexagon(PDwg: Drawing) -> None:
    print("Insert hexagon details:")
    cx = float(input("Middle point X: "))
    cy = float(input("Middle point Y: "))
    apothem = float(input("Apothem length: "))

    fill = input("Insert fill: ")
    stroke = input("Insert stroke: ")

    # circumradius R from apothem a:
    # a = R * cos(30°) => R = a / cos(30°)
    R = apothem / math.cos(math.radians(30))

    # angles in degrees, starting from top-right and going clockwise:
    # Top Right, Right, Bottom Right, Bottom Left, Left, Top Left
    angles = [-60, 0, 60, 120, 180, 240]

    points: list[tuple[int, int]] = []
    for ang in angles:
        rad = math.radians(ang)
        # SVG coordinate system: x right, y down
        x = cx + R * math.cos(rad)
        y = cy + R * math.sin(rad)
        points.append((round(x), round(y)))

    hexagon = Polygon(points=points, fill=fill, stroke=stroke)
    PDwg.add(hexagon)


def saveSvg(PDwg: Drawing) -> None:
    filename = input("Insert filename: ").strip()
    if filename == "":
        print("Invalid filename.")
        return

    print(f'Saving file to "{filename}"')
    proceed = input("Proceed (y/n)?: ").strip().lower()
    if proceed != "y":
        print("Save cancelled.")
        return

    PDwg.filename = filename
    PDwg.save(pretty=True, indent=2)
    print("Vector saved successfully!")


def showOptions() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Draw hexagon")
    print("4 - Save svg")
    print("0 - Exit")


def main() -> None:
    print("Program starting.")

    # Simple 500x500 canvas
    dwg = Drawing(size=("500px", "500px"))

    while True:
        print()
        showOptions()
        choice = input("Your choice: ").strip()

        if choice == "0":
            print("Exiting program.")
            break
        elif choice == "1":
            drawSquare(dwg)
        elif choice == "2":
            drawCircle(dwg)
        elif choice == "3":
            drawHexagon(dwg)
        elif choice == "4":
            saveSvg(dwg)
        else:
            print("Invalid choice.")

    print("\nProgram ending.")


if __name__ == "__main__":
    main()
