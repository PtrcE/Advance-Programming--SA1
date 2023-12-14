#Exercise 9

#integer list with 10 values
integer_list = [23, 45, 12, 56, 78, 9, 34, 67, 89, 5]

#using a for loop for output
print("Original List:")
for num in integer_list:
    print(num, end=" ")
print()

#highest and lowest value
highest_value = max(integer_list)
lowest_value = min(integer_list)
print(f"Highest Value: {highest_value}")
print(f"Lowest Value: {lowest_value}")

#sorts in ascending order
ascending_order = sorted(integer_list)
print("Sorted in Ascending Order:", ascending_order)

#sorts in descending order
descending_order = sorted(integer_list, reverse=True)
print("Sorted in Descending Order:", descending_order)

integer_list.append(100)
integer_list.append(200)

#prints list appending
print("List after Appending:")
for num in integer_list:
    print(num, end=" ")
print()
