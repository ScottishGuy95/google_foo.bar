# Google foo.bar 2020 Challenge
# solar-doomsday - Challenge 1
# When run in foo.bar, it handles testing the values

import math


def solution(area):
    panels = []                             # Stores the area of each panel
    remainder = area                        # Store the current total area
    while remainder != 0:                   # Loop until there is no more area
        sqRoot = int(math.sqrt(remainder))  # Passes the current area to get its square root
        sqRoot = sqRoot * sqRoot            # Get the area of that panel
        panels.append(sqRoot)               # Add the panel size to list
        remainder -= sqRoot                 # Remove the panel area from the remainder
    return panels
