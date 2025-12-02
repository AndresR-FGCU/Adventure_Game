from type_func import twpw

def bank_scenario(location,vehicle):
    twpw("As you approach the bank you get an exciting sensation of riches and wealth. ")
    twpw("Entering through the front doors a dim glow catches your eye...")
    twpw("You decide to explore and stumble into an open vault!!!")

    loot = location.collect(2)
    for item in loot:
        vehicle.add_item(item)
    print("You quietly pocket what you find.")

def gas_station_1_scenario(location,vehicle):
    twpw("I must be lucky today to find my way to SpeedTrac!!!")
    twpw("After prying through the non-functioning sliding doors a cold chill hits your neck.")
    twpw("You smell a familiar smell, the smell of hope and a brighter future!!!")
    twpw("SpeedTrac has everything needed to get you back on your feet and continue your journey")

    loot = location.collect(4)
    for item in loot:
        vehicle.add_item(item)
    print("You quietly pocket what you find.")

def gas_station_scenario(location,vehicle):
    twpw("This gas station might not be SpeedTrac but fingers crossed it still has gas.")
    twpw("As you enter through the glass doors the store is in unsightly disarray!")
    twpw("Mold covers the walls and spores float through the air; you might get sick after this one...")

    loot = location.collect(3)
    for item in loot:
        vehicle.add_item(item)
    print("You quietly pocket what you find.")

def grocery_store_scenario(location,vehicle):
    twpw("Crossing this vast desert leave you weak and hungry.")
    twpw("Coming across a Dublix was a much needed familiar sight to restock on supplies.")
    twpw("Despite being ransacked by looters and raiders, scraps remain for us to scavenge.")
    twpw("Not much but it means another day alive in this climate.")

    loot = location.collect(3)
    for item in loot:
        vehicle.add_item(item)
    print("You quietly pocket what you find.")

def house_1_scenario(location,vehicle):
    twpw("It a nice escape driving through a picture perfect neighborhood while the world collapses.")
    twpw("You settle on a house to scavenge through, who knows you might find some valuables.")

    loot = location.collect(2)
    for item in loot:
        vehicle.add_item(item)
    print("You elegantly pocket what you find.")

def house_2_scenario(location,vehicle):
    twpw("A studio apartment!!!")
    twpw("I feel the claustrophobia just opening the door!")
    twpw("I'm sure if I had coded choices you would've passed this one up.")
    twpw("Yet here we stand, maybe it'll be worth it?")

    loot = location.collect(3)
    for item in loot:
        vehicle.add_item(item)
    print("You quietly pocket what you find.")

def house_3_scenario(location,vehicle):
    twpw("The only glimpse of serenity left in this post apocalypse.")
    twpw("Perhaps you've day dreamed of settling down in a place like this?")
    twpw("Unfortunately we're just here for the goods.")

    loot = location.collect(4)
    for item in loot:
        vehicle.add_item(item)
    print("You quietly pocket what you find.")

def house_4_scenario(location,vehicle):
    twpw("All this desert and I manage to find a house by the water.")
    twpw("Makes you question if it a mirage or really there, might as well give it a gander.")

    loot = location.collect(3)
    for item in loot:
        vehicle.add_item(item)
    print("You quietly pocket what you find.")

def jewelry_store_scenario(location,vehicle):
    twpw("Can't tell yet if this one is better than the bank location!!!")
    twpw("The only thought flowing through my head is how lucky I must be this run!")
    twpw("I guess the only thing left to do is head inside and cash out.")

    loot = location.collect(2)
    for item in loot:
        vehicle.add_item(item)
    print("You quietly pocket what you find.")

def pawn_shop_scenario(location,vehicle):
    twpw("Before the apocalypse this was a scam center but now its free pickings.")
    twpw("I guess its easier to not feel bad for scavenging this location.")
    twpw("Hopefully theres still some valuables left!")

    loot = location.collect(2)
    for item in loot:
        vehicle.add_item(item)
    print("You greedily pocket what you find.")

def restaurant_1_scenario(location,vehicle):
    twpw("Jeez, this place a seriously fancy!!!")
    twpw("Gold etched doors, chandelier lined ceiling, and world class painting's lining the wall!")
    twpw("I definitely wouldn't have been able to eat here prior to the virus.")
    twpw("I guess catastrophes are the great equalizer")

    loot = location.collect(3)
    for item in loot:
        vehicle.add_item(item)
    print("You elegantly pocket what you find.")

def restaurant_2_scenario(location,vehicle):
    twpw("It might not be Nombu but definitely a classic almost nostalgic even...")
    twpw("Not much but scraps left but enough to survive.")

    loot = location.collect(3)
    for item in loot:
        vehicle.add_item(item)
    print("You quietly pocket what you find.")