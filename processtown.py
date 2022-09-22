# Cameron Colliver
# CS4050 Algorithms and Algorthm Analysis
# Muddy Town Project v0.9

import getopt
import sys
from town_generations import *

VERSION = 0.9

def main(argsv):
    current_town = read_town("towndata")
    try:
        arguments, values = getopt.getopt(argsv, "sac::r:w:e:p:vh")

        for currentArgument, currentValue in arguments:

            if currentArgument in ("-s", "--Standard_Out"):
                current_town.display_town()

            elif currentArgument in ("-a", "--Alternate_Out"):
                current_town.display_town_alt()

            elif currentArgument in ("-c", "--Create"):
                current_town = random_town(int(currentValue), int(currentValue) * 2)

            elif currentArgument in ("-r", "--Read_Town"):
                current_town = read_town(currentValue)

            elif currentArgument in ("-w", "--Write"):
                print("Town data to: " + str(currentValue))
                current_town.write_town(currentValue)

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
                print("Muddytown Project <Version Num>, by Cameron Colliver")

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

    except getopt.error as err:
        # output error, and return with an error code
        print(str(err))


if __name__ == "__main__":
    main(sys.argv[1:])
