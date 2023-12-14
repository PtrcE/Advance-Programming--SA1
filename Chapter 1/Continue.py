#Exercise 5

loop_count = 0

#while loop used to repeatedly ask user
while True:
    user_input = input("Do you want to continue? (Y/N): ").upper()

    if user_input == 'Y':
        loop_count += 1

    elif user_input == 'N':
        break  #this exits the loop if the user enters 'N'
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")

#prints the number of times the loop was executed
print(f"The loop was executed {loop_count} times.")
