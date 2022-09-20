class paving_plan:
    def __init__(self, paved_list, total_cost, houses):
        self.paved_list = paved_list
        self.minimum_cost = total_cost
        self.houses = houses

    def display_paving_plan(self):
        if self.minimum_cost is None:
            print("Error! There is no paving data stored")
            print("Please either run the shortest path algorithm or load paving data and try again")
            pass
        else:
            print("Minimum cost for this plan is " + str(self.minimum_cost))
            for road in self.paved_list:
                print('"' + road[0] + '", "' +
                      road[1] + '"')

    def write_paving_plan(self, filename):
        try:
            fp = open(filename, "x")
        except FileExistsError:
            fp = open(filename, "w")
            fp.write(str(self.minimum_cost))

        for road in self.paved_list:
            fp.write(road.addressX + ", " + road.addressY)
