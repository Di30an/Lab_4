class Dog():
    
    def __init__(self, breed,name):
        self.breed = breed
        self.name = name
        # Expect boolean True / False

    # OPERATIONS . Actions ------> Methods
    def bark (self):
        print("WOOF! My name is {}".format(self.name))
        x = (self.name + self.breed)
        print (x)

    def __str__ (self): 
        f"{self.breed} by {self.name}"
        return

my_dog = Dog("Frankie","Woods")

print(my_dog.bark()) 
print(my_dog)
