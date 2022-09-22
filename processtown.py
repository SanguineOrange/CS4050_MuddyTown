# Cameron Colliver
# Muddy Town Project v0.2
# God damn I love python

import getopt
import sys
from town_generations import *

# long_arguments = ["Standard_Out", "Alternate_Out", "Create=", "Read=", "Write=", "Version", "Help"]

def main(argsv):
    current_town = read_town("towndata")
    try:
        arguments, values = getopt.getopt(argsv, "sac::r:w:vh")

        for currentArgument, currentValue in arguments:

            if currentArgument in ("-s", "--Standard_Out"):
                current_town.display_town()

            elif currentArgument in ("-a", "--Alternate_Out"):
                current_town.display_town_alt()

            elif currentArgument in ("-c", "--Create"):
                current_town = random_town(int(currentValue), int(currentValue) * 2)

            elif currentArgument in ("-r", "--Read"):
                current_town = read_town(currentValue)

            elif currentArgument in ("-w", "--Write"):
                current_town.write_town(currentValue)

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
                              \tv   show version
                              \th   help (this display)''')

    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))


if __name__ == "__main__":
    main(sys.argv[1:])
