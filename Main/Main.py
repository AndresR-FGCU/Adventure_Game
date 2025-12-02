import random
from Vehicle import Truck, Sedan, Motorcycle
from type_func import twpw
from Items import Gas
from scenario import (bank_scenario,gas_station_1_scenario,gas_station_scenario,grocery_store_scenario,house_1_scenario,house_2_scenario,
                      house_3_scenario,house_4_scenario,jewelry_store_scenario,pawn_shop_scenario,restaurant_1_scenario,restaurant_2_scenario)
from game_locations import (bank,gas_station_1,gas_station_2,gas_station_3,grocery_store,house_1,house_2,
                            house_3,house_4,jewelry_store,pawn_shop,restaurant_1,restaurant_2)

locations_scenarios_1 = {
    bank: bank_scenario,
    gas_station_1: gas_station_1_scenario,
    house_1: house_1_scenario,
    pawn_shop: pawn_shop_scenario,
}

locations_scenarios_2 = {
    gas_station_2: gas_station_scenario,
    house_2: house_2_scenario,
    jewelry_store: jewelry_store_scenario,
}

locations_scenarios_3 = {
    gas_station_3: gas_station_scenario,
    house_3: house_3_scenario,
    restaurant_2: restaurant_2_scenario,
}

locations_scenarios_4 = {
    house_4: house_4_scenario,
    restaurant_1: restaurant_1_scenario,
    grocery_store: grocery_store_scenario,
}

def calculate_inventory_value(vehicle):
    total = 0
    for item in vehicle.inventory:
        total += getattr(item, "value", 0)
    return total

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

print("")
print("-----")
input("Press Enter to Continue...")
print("-----")
print("")

#First Location
random_location = random.choice(list(locations_scenarios_1.keys()))

print(f"You find yourself at the {random_location.name}")
random_location.describe()
print(locations_scenarios_1[random_location](random_location,selected_vehicle))

print("First location has been looted here are the spoils:", selected_vehicle.inventory)
twpw("Now to continue your journey across a winding sandstone path...")

print("")
print("-----")
input("Press Enter to Continue...")
print("-----")
print("")

#Second Location
random_location = random.choice(list(locations_scenarios_2.keys()))

print(f"You find yourself at the {random_location.name}")
random_location.describe()
print(locations_scenarios_2[random_location](random_location,selected_vehicle))

print("Second Location has been looted here are the spoils:", selected_vehicle.inventory)
twpw("You're getting closer to the city, dont slow down.")
twpw("finish strong, that bag is turning out to be a good haul; I smell a payday!")

print("")
print("-----")
input("Press Enter to Continue...")
print("-----")
print("")

#Third Location
random_location = random.choice(list(locations_scenarios_3.keys()))

print(f"You find yourself at the {random_location.name}")
random_location.describe()
print(locations_scenarios_3[random_location](random_location,selected_vehicle))

print("Third Location has been looted here are the spoils:", selected_vehicle.inventory)
twpw("Hope fills your eyes as you look past the horizon into jutting spires rising from the ground")
twpw("The standing city is so close yet far, nothing can stop you from reaching it now!")

print("")
print("-----")
input("Press Enter to Continue...")
print("-----")
print("")

#Final Location
random_location = random.choice(list(locations_scenarios_4.keys()))

print(f"You find yourself at the {random_location.name}")
random_location.describe()
print(locations_scenarios_4[random_location](random_location,selected_vehicle))

twpw("YOU'VE MADE IT!!!")
twpw("A grueling adventure now finished, time to go claim your spoils and mark your high score!")

print("Standing City reached, your soils are:", selected_vehicle.inventory)
print(f"Total inventory value: ${calculate_inventory_value(selected_vehicle)}")