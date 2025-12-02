from Locations import Location
from scenario import (bank_scenario,gas_station_1_scenario,gas_station_scenario,grocery_store_scenario,house_1_scenario,house_2_scenario,
                      house_3_scenario,house_4_scenario,jewelry_store_scenario,pawn_shop_scenario,restaurant_1_scenario,restaurant_2_scenario)
from game_items import (cash,gold,car_battery,gold_ring,silver_ring,bandage,medkit,water_bottle,cat_food,old_parking_ticket,
                        dusty_boots,expensive_painting,spare_tire,house_keys,golden_toilet,rusty_hammer,mobile_phone,duct_tape,
                        super_glue,cola,gas,butcher_knife,rare_coin,kazoo,gum_wrapper,fire_wood,splint,rusty_zippo,hatchet,
                        jar_of_dirt,perfectly_preserved_pie)


bank = Location("Bank", "A financial establishment of past.", [cash, gold, gold_ring, silver_ring])
bank_scenario = bank_scenario
gas_station_1 = Location("SpeedTrac", "The certified best gas station around.", [gas,car_battery,golden_toilet,water_bottle,bandage,rusty_zippo])
gas_station_1_scenario = gas_station_1_scenario
gas_station_2 = Location("SpendCo Gas", "Affordable gasoline and great hotdogs!", [gas,car_battery,spare_tire,water_bottle,dusty_boots])
gas_station_scenario = gas_station_scenario
gas_station_3 = Location("Off-Brand Gas", "Is it even worth pumping here?", [gas,dusty_boots,rare_coin,rusty_hammer,rusty_zippo,cat_food,duct_tape])
gas_station_scenario = gas_station_scenario
grocery_store = Location("Dublix", "I can only seem to find this store here!",[cat_food,bandage,water_bottle,cola,perfectly_preserved_pie,medkit,splint])
grocery_store_scenario = grocery_store_scenario
house_1 = Location("Suburban Home", "White picket fence, almost perfect, too perfect...", [kazoo,cash,house_keys,fire_wood,medkit,hatchet,mobile_phone,expensive_painting])
house_1_scenario = house_1_scenario
house_2 = Location("Studio Apartment", "Typical studio, must've been cozy before all this.",[super_glue,dusty_boots,water_bottle,house_keys,splint,rusty_hammer])
house_2_scenario = house_2_scenario
house_3 = Location("Small Cabin", "Slightly run down, hopefully it doesn't collapse",[fire_wood,hatchet,rusty_zippo,rusty_hammer,gold_ring,cola,gas])
house_3_scenario = house_3_scenario
house_4 = Location("Oasis home", "Looks almost like a beach home.",[jar_of_dirt,butcher_knife,house_keys,spare_tire,dusty_boots,mobile_phone])
house_4_scenario = house_4_scenario
jewelry_store = Location("Jewelry Store", "Ooooo, Fancy",[cash,silver_ring,gold_ring,rare_coin,old_parking_ticket,rusty_hammer,gum_wrapper])
jewelry_store_scenario = jewelry_store_scenario
pawn_shop = Location("Pawn Shop","Scammers, just like those pawn snobs", [cash,rare_coin,silver_ring,gold,expensive_painting,car_battery,gas])
pawn_shop_scenario = pawn_shop_scenario
restaurant_1 = Location("Nombu", "Just the name sounds fancy!",[medkit,cash,perfectly_preserved_pie,water_bottle,expensive_painting,butcher_knife,])
restaurant_1_scenario = restaurant_1_scenario
restaurant_2 = Location("Benny's", "A timeless classic on a budget",[cat_food,water_bottle,cash,butcher_knife,super_glue,old_parking_ticket])
restaurant_2_scenario = restaurant_2_scenario

location_scenarios = {
    bank: bank_scenario,
    gas_station_1: gas_station_1_scenario,
    gas_station_2: gas_station_scenario,
    gas_station_3: gas_station_scenario,
    grocery_store: grocery_store_scenario,
    house_1: house_1_scenario,
    house_2: house_2_scenario,
    house_3: house_3_scenario,
    house_4: house_4_scenario,
    jewelry_store: jewelry_store_scenario,
    pawn_shop: pawn_shop_scenario,
    restaurant_1: restaurant_1_scenario,
    restaurant_2: restaurant_2_scenario,
}