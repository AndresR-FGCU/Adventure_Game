import random
from Vehicle import Truck, Sedan, Motorcycle
from type_func import twpw
from Items import Item, Gas
from Locations import Location
from scenario import *
from game_locations import (bank,gas_station_1,gas_station_2,gas_station_3,grocery_store,house_1,house_2,
                            house_3,house_4,jewelry_store,pawn_shop,restaurant_1,restaurant_2)

gas = Gas
Location_List = [bank,gas_station_1,gas_station_2,gas_station_3,grocery_store,house_1,house_2,
                house_3,house_4,jewelry_store,pawn_shop,restaurant_1,restaurant_2]

twpw("Welcome to an adventure car game!")
vehicle = [Truck(), Sedan(), Motorcycle()]

print("Start by selecting your vehicle")
print("1.Truck")
print("2.Sedan")
print("3.Motorcycle")
print("4.describe")
print("5.Exit")

while True:
    vehicle_choice = input("Enter your choice: ")
    if vehicle_choice == "1":
        selected_vehicle = vehicle[0]
        print("You selected a Truck")
        break
    elif vehicle_choice == "2":
        selected_vehicle = vehicle[1]
        print("You selected a Sedan")
        break
    elif vehicle_choice == "3":
        selected_vehicle = vehicle[2]
        print("You selected a Motorcycle")
        break
    elif vehicle_choice == "4":
        for v in vehicle:
            v.describe()
            print("---")
    elif vehicle_choice == "5":
        print("Darn, leaving already?")
        break
    else:
        print("Try again!")

print("Your adventure starts here!")
# noinspection PyUnboundLocalVariable
selected_vehicle.describe()
twpw("Our adventure begins in a baren desert, part of the southwestern region of the U.S.")
twpw("An unknown virus has ravaged much of life on earth leaving only a portion of the population alive")
twpw("Your goal during your journey is to make it across the desert to the Standing City")
twpw("Collect valuables along your way to sell at the end of your journey just dont forget to look out for gas.")

#First Location
location = random.choice(Location_List)
print("You've stumbled across a location:",location)

scenario = location_scenarios.get(location.name)

if hasattr(location, "scenario"):
    scenario(location)
else:
    print("Well that's awkward...")

