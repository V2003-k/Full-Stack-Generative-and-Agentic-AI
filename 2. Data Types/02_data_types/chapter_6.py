chai_type = "Ginger chai"
customer_name = "Vishwajeet"

print(f"Order for {customer_name}: {chai_type} please !")

chai_description = "Armoatic and Bold"
print(f"First word: {chai_description[:8]}")
print(f"Last word: {chai_description[12:]}")
print(f"Last word: {chai_description[::-1]}")

label_text = "स्पेशल चाई"
encoded_label = label_text.encode("utf-8")
print(f"Non Encoded Label: {label_text}")
print(f"Encoded Label: {encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded Label: {decoded_label}")