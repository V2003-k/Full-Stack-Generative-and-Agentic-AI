names = ["Vishwajeet", "Meera", "Sam", "Ali"]
bills = [50, 70, 100, 85]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")