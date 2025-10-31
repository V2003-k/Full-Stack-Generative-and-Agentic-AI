essential_spices = {"cardamon", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black paper"}

all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices
print(f"Common Spices: {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"Only essential spices: {only_in_essential}")

# membership test
print(f"Is 'cloves' in essential spices: {'cloves' in essential_spices}")
print(f"Is 'cloves' in optional spices: {'cloves' in optional_spices}")