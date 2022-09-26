# Cameron Colliver
# Muddy Town Project v0.9
# CS4050 Algorithms and Algorithm Analysis
# This file contains info for the house object

class house:
    def __init__(self, name):
        self.name = name
        self.connections = []

    def add_connection(self, connection):
        self.connections.append(connection)
