#Exercise 12

#Calulate the area and circumference of the circle, triangle & rectangle using if elif else

def greet_user():
    print("==================================== Welcome! =========================================\n")
    print("======= Use me to find Areas, Circumference and Perimeters of different shapes! ========\n")


greet_user() #to greet user

shapes = ("\n1. Rectangle\n", "2. Triangle\n", "3. Circle\n")
shapes_choice = "\n".join(shapes)  # To print the list on individual lines
print(shapes_choice)

calculation = ("\n1. Area\n", "2. Circumference / Perimeter\n")

# User input
option = int(input("\nSelect which shape you'd like to calculate: "))

calcu_choice = "\n".join(calculation)  # To print the list on individual lines
print(calcu_choice)

# Area of Rectangle

if option == 1:
    option2 = int(input("\nWhat do you want to calculate? "))

    if option2 == 1:
        length = float(input("\nEnter Length: "))
        width = float(input("\nEnter Width: "))
        area = length * width  # formula to find the area of a rectangle
        print("\nThe Area of Rectangle is:", area)  # result


# Perimeter of Rectangle

    elif option2 == 2:
        length = float(input("\nEnter Length: "))
        width = float(input("\nEnter Width: "))
        perimeter = 2 * length + 2 * width  # formula to find the perimeter of a rectangle
        print("\nThe Perimeter of a Rectangle is:", perimeter)  # result


# Area of Triangle

elif option == 2:
    option2 = int(input("\nWhat do you want to calculate? "))

    if option2 == 1:
        base = float(input("\nEnter Base: "))
        height = float(input("\nEnter Height: "))
        area = (1/2) * base * height  # formula to find the area of a triangle
        print("\nThe Area of a Triangle is:", area)  # result

#Periemeter of Triangle

    elif option2 == 2:
        side1 = float(input("\nEnter length of first side: "))
        side2 = float(input("\nEnter length of second side: "))
        side3 = float(input("\nEnter length of third side: "))
        perimeter = side1 + side2 + side3  # formula to find the perimeter of a triangle
        print("\nThe Perimeter of a Triangle is:", perimeter)  # result


# Area of Circle

elif option == 3:
    option2 = int(input("\nWhat do you want to calculate? "))

    if option2 == 1:
        radius = float(input("\nEnter the radius: "))
        area = 3.142 * (radius ** 2)  # Formula to find the area of a circle
        print("\nThe area of the circle is:", area)  # Result

#Circumference of Circle

    elif option2 == 2:
        radius = float(input("\nEnter Radius: "))
        circ = 2 * 3.142 * radius  # Formula to find the circumference of a circle
        print("\nThe circumference of a circle is:", circ)  # Result

else:
    print("Invalid option. Please select a valid shape and calculation.")