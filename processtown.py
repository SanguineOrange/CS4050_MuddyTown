# Cameron Colliver
# Muddy Town Project v1.0
# CS4050 Algorithms and Algorithm Analysis
# This parses input on the command line and calls the necessary functions:


import getopt
import sys
from town_generations import *

VERSION = str(1.0)


def main(argsv):
    current_town = read_town("MiniTown.dat")
    current_mode = "d"

    try:
        arguments, values = getopt.getopt(argsv, "sacr:w:e:p:vh")

        for currentArgument, currentValue in arguments:

            if currentArgument in ("-s", "--Standard_Out"):
                current_mode = "d"
                current_town.display_town()

            elif currentArgument in ("-a", "--Alternate_Out"):
                current_mode = "a"
                current_town.display_town_alt()

            elif currentArgument in ("-c", "--Create"):
                current_town = random_town(10, 21)

            elif currentArgument in ("-r", "--Read_Town"):
                current_town = read_town(currentValue)

            elif currentArgument in ("-w", "--Write"):
                current_town.write_town(currentValue, current_mode)

            elif currentArgument in ("-e", "--Read_Paving"):
                current_town.read_paving_plan(currentValue)
                current_town.display_paving_plan()
                if current_town.check_paving_plan():
                    print("This plan is the lowest cost for " + current_town.townName)
                else:
                    print("This plan is not the minimum plan possible!")

            elif currentArgument in ("-p", "--Create_Paving"):
                print(currentValue)
                current_town.kruskals_algorithm(True)
                current_town.write_paving_plan(currentValue)

            elif currentArgument in ("-v", "--Version"):
                print("Muddytown Project version " + VERSION + ", by Cameron Colliver")

            elif currentArgument in ("-h", "--Help"):
                print('''Syntax: [-option [parameter]]
                              options:
                              \ts   show current town in standard format
                              \ta   show current town in alternate format
                              \tr   read town data from file identified by parameter
                              \tw   write current town to file identified by parameter
                              \tc   create town given number of buildings and streets
                              \te   read paving plan data from file identified by parameter
                              \tp   find the minimum cost paving plan and write plan to file identified by parameter
                              \tv   show version
                              \th   help (this display)''')

    # Catch unexpected input and print the error
    except getopt.error as err:
        print(str(err))


if __name__ == "__main__":
    main(sys.argv[1:])
