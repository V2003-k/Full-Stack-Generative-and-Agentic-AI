class Chai:
    origin = "India"

# print(Chai.origin)

Chai.is_hot = True
# print(Chai.is_hot)

# crating objects from class

masala = Chai()
print(f"Masala: {masala.origin}")
print(f"Masala: {masala.is_hot}")

masala.is_hot = False

print(f"Chai: {Chai.is_hot}")
print(f"Masala: {masala.is_hot}")

masala.flavor = "Masala"
print(masala.flavor)