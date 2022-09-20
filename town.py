from paving_plan import paving_plan


class Town:
    def __init__(self, town_name, unpaved_list, houses) -> None:
        self.townName = town_name
        self.unpaved_list = unpaved_list
        self.paved_list = []
        self.minimum_cost = None
        self.houses = houses

    def display_town(self):
        print(self.townName)
        for road in self.unpaved_list:
            print('"' + str(road[0]) + ", " + '"' +
                  self.houses[road[1]].name + '", "' +
                  self.houses[road[2]].name + '"')

    def display_town_alt(self):
        print(self.townName)
        for house in self.houses:
            print(house.name)
        for road in self.unpaved_list:
            print(self.houses[road[1]].name + ", " +
                  self.houses[road[2]].name + ", " +
                  str(road[0]))

    def write_town(self, filename):
        try:
            fp = open(filename, "x")
        except FileExistsError:
            fp = open(filename, "w")
        fp.write(self.townName + '\n')

        for road in self.unpaved_list:
            fp.write('"' + str(road[0]) + '", "' +
                     self.houses[road[1]].name + '", "' +
                     self.houses[road[2]].name + '"\n')

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

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

    # code for Kruskal's algorithm was adapted from Skeina's C code
    def kruskals_algorithm(self) -> paving_plan:
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
        self.paved_list = result.copy()
        self.minimum_cost = minimum_cost
        return paving_plan(self.paved_list, self.minimum_cost, self.houses)
