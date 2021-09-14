#class Pet:
#    def __init__(self,name,breed,color):  # self is going to refer back to itself when it is called
#        self.name = name
#        self.breed = breed
#        self.color = color

#dog = Pet("Malachi","great pyrneese","black and white")
#cat = Pet("Esper","bangle","orange with brown spots")

#print(f"{dog.name} is a {dog.breed} and is {dog.color}")
#print(f"{cat.name} is a {cat.breed} and is {cat.color}")


class Pet:
    def __init__(self):
        self.name = input("What is your pet's name? ")
        self.breed = input(f"What is {self.name}'s breed? ")
        self.color = input(f"What is {self.name}'s color? ")

cat = Pet()

print(f"{cat.name} is a {cat.breed} and is {cat.color}")