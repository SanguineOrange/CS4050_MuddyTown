# Cameron Colliver
# Muddy Town Project v0.2
# God damn I love python

import argparse
import sys
from town_generations import *


def __main__():
    # Parser adapted from fellow student Stillian Balasoupolov
    current_town = read_town("towndata")

    argv = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--alternative', dest="a",
                        action="store_true", help="show current town in alternate format")
    parser.add_argument('-r', '--read', dest="r",
                        help="read town data from file identified by parameter")
    parser.add_argument('-s', '--standard', dest="s", action="store_true",
                        help="show current town in standard format")
    parser.add_argument('-v', '--version', dest="v",
                        action="store_true", help="show version")
    parser.add_argument('-w', '--write', dest="w",
                        help="write current town to file identified by parameter")
    parser.add_argument('-c', '--create', dest="c", nargs="+", type=int,
                        help="creates town given number of buildings and streets")

    args = parser.parse_args()

    if len(argv) == 0:
        current_town.display_town()
        return 0

    if args.r:
        current_town = read_town(args.r)
        current_town.display_town()
    if args.a:
        current_town.display_town_alt()
    elif args.s:
        current_town.display_town()
    elif args.v:
        print('muddytown version 0.2 by Cameron Colliver')
    elif args.w:
        current_town.write_town(args.w)
        print(args.w)
    elif args.c:
        current_town = random_town(args.c[0], args.c[1])
        current_town.display_town()

    elif args.h:
        print('''Syntax: [-option [parameter]]
                  options:
                  \ts   show current town in standard format
                  \ta   show current town in alternate format
                  \tr   read town data from file identified by parameter
                  \tw   write current town to file identified by parameter
                  \tc   create town given number of buildings and streets
                  \tv   show version
                  \th   help (this display)''')

    return 0


__main__()
