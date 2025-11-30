class Vehicle:
    def __init__(self,name,storage_cap,fuel_cap):
        self.name = name
        self.storage_cap = storage_cap
        self.fuel_cap = fuel_cap
        self.fuel_curr = fuel_cap
        self.inventory = []

    def describe(self):
        print("---")
        print(f"Vehicle: {self.name}")
        print(f"Storage Capacity: {self.storage_cap}")
        print(f"Fuel Capacity: {self.fuel_cap}")
        print(f"Current Fuel: {self.fuel_curr}")
        print(f"Inventory: {self.inventory}")
        print("---")

    def add_item(self,item):
        if len(self.inventory) < self.storage_cap:
            self.inventory.append(item)
            print(f"{item} added to {self.name}'s inventory.")
        else:
            print("Storage is full!")

    def remove_item(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"{item} removed from {self.name}'s inventory.")
        else:
            print(f"{item} not found in {self.name}'s inventory.")

    def drive(self, distance):
        if self.fuel_curr >= distance:
            self.fuel_curr -= distance
            print(f"Drove {distance} units. Remaining Fuel: {self.fuel_curr}")
        else:
            print("Not enough fuel!")

    def refuel(self, amount):
        if self.fuel_curr + amount <= self.fuel_cap:
            self.fuel_curr += amount
            print(f"Refueled {amount} units. Current Fuel: {self.fuel_curr}")
        else:
            self.fuel_curr = self.fuel_cap
            print(f"Fuel tank is full at {self.fuel_cap} units.")

class Truck(Vehicle):
    def __init__(self):
        super().__init__("Truck", storage_cap=20, fuel_cap=50)

class Sedan(Vehicle):
    def __init__(self):
        super().__init__("Sedan", storage_cap=15, fuel_cap=75)

class Motorcycle(Vehicle):
    def __init__(self):
        super().__init__("Motorcycle", storage_cap=10, fuel_cap=100)
