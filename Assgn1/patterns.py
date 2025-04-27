# Ask user for the last number
last_number = int(input("Enter the last number: "))

# Generate the pattern
for i in range(1, last_number + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# Ask the user for the last number
last_number = int(input("Enter the last number: "))

# Generate the pattern
for i in range(1, last_number + 1):
    print(str(i) * i)


# Take input from the user
n = int(input("Enter the number of rows: "))

# Print the star pattern
for i in range(1, n + 1):
    print("*" * i)
