# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")

# value = 13

# if (remainder := value % 5):
#     print(f"Not divisible, remainder is {remainder}")


# available_sizes = ["small", "medium", "large"]

# if (choice := input("Enter Your chai cup size: ")) in available_sizes:
#     print(f"Serving {choice} chai")
# else:
#     print(f"Size is unavailable - {choice}")

flavors = ["masala", "ginger", "lemon", "mint"]

print("Available flavors: ", flavors)

while (flavor := input("Choose your flavor: ")) not in flavors:
    print(f"Sorry, {flavor} is not available")
print(f"You choose {flavor} chai")