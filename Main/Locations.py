import random as ran
class Locations:
    def __init__(self, name,spawn,loot,enemy):
        self.name = name
        self.spawn = spawn
        self.loot = loot
        self.enemy = enemy
        self.loot_num = loot
        self.enemy_num = enemy

    def describe(self):
        print(self.name)
        print(self.enemy_num)
        print(self.loot_num)

    def collect(self,item):
        if






