#Exercise 1

user_greeting = input("Hello, user!\nWhat is your name? ").title()

user_age = int(input("What is your age? "))
print(f"It is good to meet you, {user_greeting}")
user_name_length = len(user_greeting)
next_year_user_age = user_age + 1
print("The length of your name is:")
print(user_name_length)

print("You will be", next_year_user_age, "in a year.")