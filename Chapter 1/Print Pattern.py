#Exercise 8

for i in range(1, 6):  # Outer loop for the number of rows
    for j in range(1, i + 1):  # Inner loop for printing numbers in each row
        print(j, end=" ")
    print()  # Move to the next line after each row
