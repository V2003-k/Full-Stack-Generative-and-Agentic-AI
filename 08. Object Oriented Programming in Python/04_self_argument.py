class Chaicup:
    size = 150 # ml

    def destribe(self):
        return f"A {self.size} ml chai cup"
    
cup = Chaicup()
print(cup.destribe())
print(Chaicup.destribe(cup))

cup_two = Chaicup()
cup_two.size = 100
print(cup_two.destribe())
print(Chaicup.destribe(cup_two))