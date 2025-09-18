# A1_T5 Calculate area

print("Calculate the area of a wall.")

# Ask for width
Feed = input("Enter the width in meters: ")
Width = float(Feed)   # convert to integer

# Ask for height
Feed = input("Enter the height in meters: ")
Height = float(Feed)  # convert to integer

# Show width and height
print(f"Width is {Width} m and height is {Height} m.")

# Calculate area
Area = Width * Height

# Show result
print(f"The wall will be {Area} square meters.")
