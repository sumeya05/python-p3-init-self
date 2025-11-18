class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed
        # Optional: You can add other attributes with defaults here
        # self.favorite_toy = "Any"
        # self.owner = None

    def bark(self):
        print("Woof!")

    def showing_self(self):
        return self

    def get_adopted(self, owner_name):
        self.owner = owner_name

    # You could also add the bark method with self.name if needed for other tests
    # def bark(self):
    #     print(f"{self.name} says Woof!")
