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

class Gas(Item):
    def __init__(self,amount=15):
        super().__init__("Gas", "Some boom-boom juice", value = amount)
        self.amount = amount

    def use(self,vehicle):
        if hasattr(vehicle,"fuel"):
            vehicle.fuel += self.amount
            print(f"{vehicle.name} refueled by {self.amount} units. Fuel: {vehicle.fuel}")
        else:
            print(f"{vehicle.name} cant be refueled.")
