# Cameron Colliver
# Muddy Town Project v1.0
# CS4050 Algorithms and Algorithm Analysis
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


# Read town from a file
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

    # Check if the town is in alternate format and process it if it is
    if "Town: " in town_name:
        town_name = town_name.replace("Town: ", '')
        num_buildings = fp.readline().replace("Number of buildings: ", "")
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

            # If the houses were not previously noted add them to the house list
            if address_x not in house_key:
                houses.append(house(address_x))
                house_key.append(address_x)

            if address_y not in house_key:
                houses.append(house(address_y))
                house_key.append(address_y)

            # Add the connections to houses, this is for the BFS implementation
            house_x = house_key.index(address_x)
            house_y = house_key.index(address_y)
            houses[house_x].add_connection(houses[house_y])
            houses[house_y].add_connection(houses[house_x])

            # Add road to list
            new_road_list = [weight, house_key.index(address_x), house_key.index(address_y)]
            unpaved_list.append(new_road_list)

    else:
        # Read in a standard format file
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

            # If the houses were not previously noted add them to the house list
            if address_x not in house_key:
                houses.append(house(address_x))
                house_key.append(address_x)

            if address_y not in house_key:
                houses.append(house(address_y))
                house_key.append(address_y)

            # Add the connections to houses, this is for the BFS implementation
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
    new_houses = []
    house_key = []
    seed = int(time.time() * 1000)

    invalid = True
    while invalid:
        duplicate = False
        new_houses.clear()
        house_key.clear()
        unpaved_roads.clear()

        # Generate a new road in [w,x,y] format
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
            new_rand_road = [weight, address_x, address_y]
            # Check if road is a duplicate
            for road in unpaved_roads:
                if [road[1], road[2]] == [address_x, address_y] or [road[2], road[1]] == [address_x, address_y]:
                    duplicate = True

            # if it isn't a duplicate, append to road list and note connection on houses
            if not duplicate:
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
        try:
            if check_connectivity(new_houses) and len(new_houses) == num_houses and len(unpaved_roads) == num_roads:
                seed += 1
                # Was getting an out of bounds error during printing
                # Adding a try-catch block during generation seems to have fixed it
                for road in unpaved_roads:
                    valid_road = ('"' + str(road[0]) + ", " + '"' +
                      new_houses[road[1]].name + '", "' +
                      new_houses[road[2]].name + '"')
                new_random_town = Town("Town " + str(seed), unpaved_roads, new_houses, house_key)
                return new_random_town

        except IndexError:
            invalid = True


# Check for connection validation using Breadth-first method
def check_connectivity(houses) -> bool:
    visited = [houses[0]]
    for house in visited:
        for connection in house.connections:
            if connection not in visited:
                visited.append(connection)

    # Return true if town is connected
    if len(visited) == len(houses):
        return True
    else:
        return False
