#given list
locations = ['dubai', 'paris', 'switzerland', 'London', 'amsterdam', 'New York']

#prints the given list and find its length
print("Original List:", locations)
print("Length of the List:", len(locations))

#sorted() to print the list in alphabetical order
sorted_alphabetical = sorted(locations)
print("Sorted in Alphabetical Order:", sorted_alphabetical)

#shows the unchanged original order
print("Original List (unchanged):", locations)

#sorted() to print the list in reverse alphabetical
sorted_reverse = sorted(locations, reverse=True)
print("Sorted in Reverse Alphabetical Order:", sorted_reverse)

#shows the unchanged original order
print("Original List (unchanged):", locations)

#reverse() to changes the order of the list
locations.reverse()
print("List after using reverse():", locations)

#sort() to changes the list to alphabetical order
locations.sort()
print("List after using sort() (Alphabetical Order):", locations)

#sort() to change the list to reverse alphabetical order
locations.sort(reverse=True)
print("List after using sort() (Reverse Alphabetical Order):", locations)
