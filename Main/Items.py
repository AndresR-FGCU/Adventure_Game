class Item:
    def __init__(self,name,description, value):
        self.name = name
        self.description = description
        self.value = value

    def __repr__(self):
        return f"Item({self.name}, value={self.value})"

    def describe(self):
        print(f"Item: {self.name}")
        print(f"Description: {self.description}")
        print(f"Value: {self.value}")
