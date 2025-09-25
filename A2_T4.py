print("Program starting.")
print("Estimate how many minutes you spent on programming...\n")

times = []
for i in range(1, 8):  # A1_T1 ... A1_T7
    minutes = int(input(f"A1_T{i}: "))
    times.append(minutes)

total = sum(times)
average = total / len(times)
average_rounded = round(average, 2)
average_int = round(average)  # kokonaisluku, lähin minuutti

print(f"\nIn total you spent {total} minutes on programming.")
print(f"Average per task was {average_rounded:.2f} min and same rounded to the nearest integer {average_int} min.")

print("\nProgram ending.")
