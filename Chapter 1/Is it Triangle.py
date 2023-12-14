#Exercise 3

#user input asking for desired length for each side
side1 = float(input("Enter length of the 1st side: "))
side2 = float(input("Enter length of the 2nd side: "))
side3 = float(input("Enter length of the 3rd side: "))

#this checks triangle inequality
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    print("These side lengths form a valid triangle.")
else:
    print("These side lengths do not form a valid triangle.")
