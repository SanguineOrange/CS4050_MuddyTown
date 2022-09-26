# Cameron Colliver
# Muddy Town Project v0.2
# This file contains all necessary functions for:
#       1. town generation
#       2. Random number generation
#       3. Validation checking

import time
from town import Town
from house import house


# Generates pseudorandom numbers utilizing the linear congruentional method
def random(seed) -> int:
    modulus = 21089
    increment = 6262
    multiplier = 14945

    seed = (multiplier * seed + increment) % modulus
    return seed


def read_town(filename) -> Town:
    try:
        fp = open(filename, "r")
    except:
        print("An error occurred opening the file\n")
        pass

    town_name = fp.readline().replace('\n', '')
    houses = []
    house_key = []
    unpaved_list = []

    if "Town: " in town_name:
        town_name = town_name.replace("Town: ", '')
        num_buildings = fp.readline().replace("Number of buildings: " , "")
        num_buildings = int(num_buildings.replace('\n', ''))

        # Skip the lines that are just addresses
        for i in range(0, num_buildings, 1):
            fp.readline()

        while True:
            read_road = fp.readline()
            if not read_road:
                fp.close()
                break

            # Clean the string for consumtion
            read_road = read_road.replace('"', '')
            read_road = read_road.replace("\n", '')
            split_string = read_road.split(",", 2)
            weight = int(split_string[2])
            address_x = split_string[0]
            address_y = split_string[1]

            if address_x not in house_key:
                houses.append(house(address_x))
                house_key.append(address_x)

            if address_y not in house_key:
                houses.append(house(address_y))
                house_key.append(address_y)

            house_x = house_key.index(address_x)
            house_y = house_key.index(address_y)

            houses[house_x].add_connection(houses[house_y])
            houses[house_y].add_connection(houses[house_x])

            # Add road to list
            new_road_list = [weight, house_key.index(address_x), house_key.index(address_y)]
            unpaved_list.append(new_road_list)

    else:
        while True:
            read_road = fp.readline()
            if not read_road:
                fp.close()
                break

            # Clean the string for consumtion
            read_road = read_road.replace('"', '')
            read_road = read_road.replace("\n", '')
            split_string = read_road.split(",", 2)
            weight = int(split_string[0])
            address_x = split_string[1]
            address_y = split_string[2]

            if address_x not in house_key:
                houses.append(house(address_x))
                house_key.append(address_x)

            if address_y not in house_key:
                houses.append(house(address_y))
                house_key.append(address_y)

            house_x = house_key.index(address_x)
            house_y = house_key.index(address_y)

            houses[house_x].add_connection(houses[house_y])
            houses[house_y].add_connection(houses[house_x])

            # Add road to list
            new_road_list = [weight, house_key.index(address_x), house_key.index(address_y)]
            unpaved_list.append(new_road_list)
    new_town = Town(town_name, unpaved_list, houses, house_key)
    return new_town


# Generate arbitrary town data given a seed
def random_town(num_houses, num_roads) -> Town:
    unpaved_roads = []
    seed = int(time.time() * 1000)

    invalid = True
    while invalid:
        new_houses = []
        house_key = []
        for i in range(num_roads):
            seed = random(seed)
            weight = seed % (3 + num_roads)
            if weight == 0:
                weight += 1
            seed = random(seed)
            address_x = seed % num_houses
            while True:
                seed = random(seed)
                address_y = seed % num_houses
                if address_y != address_x:
                    break

                if new_rand_road not in unpaved_roads:
                    unpaved_roads.append(new_rand_road)
                else:
                    num_roads += 1

            new_rand_road = [weight, address_x, address_y]
            if new_rand_road not in unpaved_roads:
                unpaved_roads.append(new_rand_road)
                if address_x not in house_key:
                    new_houses.append(house(str(address_x) + " St"))
                    house_key.append(address_x)

                if address_y not in house_key:
                    new_houses.append(house(str(address_y) + " St"))
                    house_key.append(address_y)

                index_x = house_key.index(address_x)
                index_y = house_key.index(address_y)

                new_houses[index_x].add_connection(new_houses[index_y])
                new_houses[index_y].add_connection(new_houses[index_x])

        # if town is not connected it's invalid
        if check_connectivity(new_houses):
            seed += 1
            invalid = False
    new_random_town = Town("Random Town", unpaved_roads, new_houses, house_key)

    return new_random_town


# Check for connection validation using Breadth-first method
def check_connectivity(houses) -> bool:
    visited = [houses[0]]
    for house in visited:
        for connection in house.connections:
            if connection not in visited:
                visited.append(connection)

    # Return true if town is connected
    if len(visited) == len(houses):
        print("Valid")
        return True
    else:
        print("Invalid")
        return False
