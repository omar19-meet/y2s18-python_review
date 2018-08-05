# Write your solutions for 1.5 here!
class Superheros:
    def __init__(self,name,superpower,strength):
        self.name=name
        self.superpower=superpower
        self.strength=strength
    def printNameStrength(self):
        print(self.name)
        print(self.strength)
    def save_civilian(self, work):
        
        if work>self.strength:
            print("Superhero is not strong enough :(")
        if work<=self.strength:
            self.strength=self.strength-work
            print(self.strength)

Omar=Superheros("Omar","Fists",9000)
Omar.printNameStrength()
Omar.save_civilian(500000)