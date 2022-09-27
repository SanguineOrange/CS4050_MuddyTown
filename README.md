# Muddy Town project for CS4050

## Overview
This project solves the "muddy town" minimum spanning tree problem for either 
  towns that are read off a file
  towns that are randomly generated using an implementation of a linear congruational pseudorandom number generator

## Commands 
processtown contains the main function and has commmand line get-opt style commands
commands should resemble ** python processtown.py -arguments** where -arguments is any combination of the following:

#### -s
  Displays the town in the standard specified by the project overview
  
#### -a 
  Displays the town in the alternate specified by the project overview

#### -r *filename* 
  Reads town data in either specified standard or alternate formats to the speficied file
  
#### -w *filename* 
   Writes town data in either specified standard or alternate formats to the specified file
   
#### -c *number of buildings* 
  Pseudorandombly generates a new arbitrary town with the specified number of buildings
  
#### -e *filename* 
  Reads a paving plan from the specified file and evaluates it uising Kruskal's Algorithm
  
#### -p *filename* 
  Creates a minimum cost paving plan for the stored town and writes it to the specified file
  
#### -v
  Displays the version of this project
  
#### -h
  Displays all commands in the terminal

### Example:
*python processtown.py -caw town_data.dat*
This will create a new town and save that data to a new data file called town_data

*python processtown.py -r town_data.dat -p paving_plan.dat -e paving_plan.dat*
This will read the town information off of town_data.dat and generate a paving plan, then evalue and display it