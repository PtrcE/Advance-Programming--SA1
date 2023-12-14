#Exercise 13

def calculate_product(input_list):
    """Calculate the product of values in the given list."""
    product = 1
    for value in input_list:
        product *= value
    return product

numbers = [2, 3, 4, 5]

result = calculate_product(numbers)

print(f"The product of the list values is: {result}")
