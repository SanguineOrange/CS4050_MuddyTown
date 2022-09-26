# Cameron Colliver
# Muddy Town Project v0.9
# CS4050 Algorithms and Algorithm Analysis
# This file contains the town object as well as methods for:
#       1. Write/Display town in standard or alternate format
#       2. Write/Display paving plans for a town
#       3. Generating a paving plan from Kruskal's minimum spanning tree algorithm
#       4. Evaluation of paving data also from Kruskal's minimum spanning tree algorithm

from house import house


class Town:
    def __init__(self, town_name, unpaved_list, houses, house_key) -> None:
        self.townName = town_name
        self.unpaved_list = unpaved_list

        self.house_key = house_key
        self.houses = houses

        self.paved_list = []
        self.paved_houses = []

        self.minimum_cost = None
        self.total_cost = None

    # Display town in standard format
    def display_town(self):
        print(self.townName)
        for road in self.unpaved_list:
            print('"' + str(road[0]) + ", " + '"' +
                  self.houses[road[1]].name + '", "' +
                  self.houses[road[2]].name + '"')

    # Display town in alternate format
    def display_town_alt(self):
        print("Town: " + self.townName)
        print("Number of buildings: " + str(len(self.houses)))
        i = 1
        for house in self.houses:
            print('[' + str(i) + '] ' + house.name)
            i += 1
        for road in self.unpaved_list:
            print('"' + self.houses[road[1]].name + '", ' +
                  '"' + self.houses[road[2]].name + '", ' +
                  str(road[0]))

    # Write town data to a file
    def write_town(self, filename, mode):
        try:
            fp = open(filename, "x")
        except FileExistsError:
            fp = open(filename, "w")

        # If mode is default, write standard format
        if mode == 'd':
            fp.write(self.townName + '\n')

            for road in self.unpaved_list:
                fp.write('"' + str(road[0]) + '", "' +
                         self.houses[road[1]].name + '", "' +
                         self.houses[road[2]].name + '"\n')

        # else write in alternate format
        elif mode == 'a':
            fp.write("Town: " + self.townName + '\n')
            fp.write("Number of buildings: " + str(len(self.houses)) + '\n')

            i = 0
            for house in self.houses:
                i += 1
                fp.write("[" + str(i) + "]" + house.name + '\n')
            for road in self.unpaved_list:
                fp.write(self.houses[road[1]].name + ", " +
                      self.houses[road[2]].name + ", " +
                      str(road[0]) + '\n')


    # Find root of tree, adapted from Skeina's C code
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Union two trees together, adapted from Skeina's C code
    def union_find(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    # Kruskal's algorithm was adapted from Skeina's C code
    def kruskals_algorithm(self, overwrite):
        result = []
        total_vertices = len(self.houses)
        i = 0
        e = 0
        self.unpaved_list = sorted(self.unpaved_list, key=lambda item: item[0])

        parent = []
        rank = []

        for node in range(total_vertices):
            parent.append(node)
            rank.append(0)

        minimum_cost = 0
        while e < total_vertices - 1:
            weight, u, v = self.unpaved_list[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([self.houses[u].name, self.houses[v].name])
                self.union_find(parent, rank, x, y)
                minimum_cost += weight

        # If overwrite flag is on, set result as paving plan
        if overwrite:
            houses = []
            house_key = []
            self.paved_list = result.copy()
            self.total_cost = minimum_cost
            for road in result:
                address_x = road[0]
                address_y = road[1]
                if address_x not in house_key:
                    houses.append(house(address_x))
                    house_key.append(address_x)

                if address_y not in house_key:
                    houses.append(house(address_y))
                    house_key.append(address_y)

                houseX = house_key.index(address_x)
                houseY = house_key.index(address_y)

                houses[houseX].add_connection(houses[houseY])
                houses[houseY].add_connection(houses[houseX])
            self.paved_houses = houses.copy()
        # Else simply return the minimum cost
        else:
            return minimum_cost

    # Check if currently stored plan is also the smallest according to Kruskal's
    def check_paving_plan(self):
        if self.kruskals_algorithm(False) == self.total_cost:
            return True
        else:
            return False

    # Read paving plan from a file
    def read_paving_plan(self, filename):
        try:
            fp = open(filename, "r")
        except:
            print("An error occurred opening the file\n")
            return

        paved_roads = []
        total_cost = 0

        if self.townName != fp.readline().replace('\n',''):
            print("Warning! Town data does not match paving data stored on this file! +"
                  "\nThis might mean the paving plan is invalid!")

        while True:
            read_paving = fp.readline()
            if not read_paving:
                break
            read_paving = read_paving.replace('"', '')
            read_paving = read_paving.replace("\n", '')
            split_string = read_paving.split(", ", 1)

            try:
                index_x = self.house_key.index(split_string[0])
                index_y = self.house_key.index(split_string[1])
            except ValueError:
                print("Error! Town data does not match paving data stored on this file!")
                return

            # Check for duplicate streets, make sure to only append lowest weight
            lowest_weight = None
            address_x = None
            address_y = None
            for road in self.unpaved_list:
                if index_x == road[1] and index_y == road[2]:
                    if lowest_weight is None or road[0] < lowest_weight:
                        lowest_weight = road[0]
                        address_x = road[1]
                        address_y = road[2]

            total_cost += lowest_weight
            paved_roads.append([self.houses[address_x].name, self.houses[address_y].name])
        self.total_cost = total_cost
        self.paved_list = paved_roads.copy()

    # Print the paving plan in standard format
    def display_paving_plan(self):
        if self.total_cost is None:
            print("Error! There is no paving data stored")
        else:
            print("Minimum cost for this plan is " + str(self.total_cost))
            for road in self.paved_list:
                print('"' + str(road[0]) + '", "' +
                      str(road[1]) + '"')

    # Write the paving plan in standard format
    def write_paving_plan(self, filename):
        try:
            fp = open(filename, "x")
        except FileExistsError:
            fp = open(filename, "w")
        fp.write(self.townName + '\n')
        for road in self.paved_list:
            fp.write('"' + road[0] + '", "' +
                     road[1] + '"\n')
