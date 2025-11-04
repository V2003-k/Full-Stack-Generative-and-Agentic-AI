import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Vishwajeet Khpale"
tokens = enc.encode(text)

# Tokens: [25216, 3274, 0, 3673, 1308, 382, 119951, 86, 7957, 292, 20724, 79, 1167]
print(f"Tokens: {tokens}")

decoded = enc.decode([25216, 3274, 0, 3673, 1308, 382, 119951, 86, 7957, 292, 20724, 79, 1167])
print(f"Decoded: {decoded}")