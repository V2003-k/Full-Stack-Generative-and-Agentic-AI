class Chai:
    temperature = "hot"
    strength = "Strong"

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "mild"
cutting.cup = "samll"
print("After changing", cutting.temperature)
print("Cup size: ", cutting.cup)
print("Direct look into the class", Chai.temperature)

cutting.cup = "large"

cutting.temperature = "Very hot"
del cutting.temperature
# del cutting.cup
print(cutting.temperature)
print(cutting.cup)