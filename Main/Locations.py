import random as rand

class Location:
    def __init__(self, name,description,loot_table):
        self.name = name
        self.description = description
        self.loot_table = loot_table

    def __repr__(self):
        return f"{self.name}, ({self.description})"

    def describe(self):
        print( f"{self.name}: {self.description}")

    def collect(self, num_items = 1):
        if not self.loot_table:
            print("No loot to collect!")
            return []

        loot_found = rand.sample(self.loot_table, min(num_items, len(self.loot_table)))
        print(f"You collected: {', '.join([item.name for item in loot_found])}")
        return loot_found

    @staticmethod
    def random_location(locations):
        return rand.choice(locations)






