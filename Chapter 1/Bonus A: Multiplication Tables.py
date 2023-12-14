
#prints the multiplication table from 1 to 10
for i in range(1, 11):
    print(f"\nMultiplication table for {i}:\n")
    for j in range(1, 11):
        result = i * j
        print(f"{i} x {j} = {result}")
