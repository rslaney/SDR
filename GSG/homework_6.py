#!/usr/bin/env python3

""" HackRF SDR Lesson 6 homework.
# A weather station measures wind direction once per minute. 
# Write a program to indicate the average direction over a five minute period. 
# Try it on the following sets of readings:
#   12°, 15°, 13°, 9°, 16°
#   358°, 1°, 359°, 355°, 2°
#   210°, 290°, 10°, 90°, 170°
# Modify your program to handle wind speed input in addition to direction

Steps:
- Convert input (angles) to radians
- Calculate average (radians)
- Convert average to angle

This program will be a Procedural Programming 
"""


import math


# Full circle is 360 degrees
FULL_CIRCLE:float = 360
INITIAL_VALUE: float = 0



def degrees_to_radians(wind_dir_deg: float) -> float: 
    """ Convert argument (degrees) to radians"""
    wind_dir_rad: float = wind_dir_deg * (math.tau / FULL_CIRCLE)
    
    return wind_dir_rad

def radians_to_degrees(radians_value: float) -> float:
    """ Convert argument (radians) to degrees"""
    wind_avg_deg: float = (radians_value * (FULL_CIRCLE / math.tau)) % FULL_CIRCLE

    return wind_avg_deg

def homework() -> None: 
    """ Convert sample data in degrees to radians"""
    
    # Inputs (Degrees)
    # direction_inputs: list = [12, 15, 13, 9, 16]
    # direction_inputs: list = [358, 1, 359, 355, 2]
    direction_inputs: list = [210, 290, 10, 90, 170]

    #1. Convert degrees to radians. This uses custom function with tau instead
    # of built-in math.radians which uses pi
    radians:list = [degrees_to_radians(deg) for deg in direction_inputs]
    sum_sin: float = sum(math.sin(rad) for rad in radians)
    sum_cos: float = sum(math.cos(rad) for rad in radians)

    #2. Average the values
    avg_rad: float = math.atan2(sum_sin, sum_cos)

    #3. Convert average (radians) to degrees
    avg_deg = radians_to_degrees(avg_rad)

    print(avg_deg)

    # # With wind speed, would add scalar multiple of the speed in sum_sin and 
    # # sum_cos, with the input being list of (speed, direction) tuples e.g.,
    # vectors: list = [(22, 12), (16, 15), (25, 13), (1, 9), (5, 16)]
    # # populate radians manually with a for loop
    # for speed, deg in vectors:
    #     vectors_rd += (speed, degrees_to_radians(deg))
    # # This should be split out to be more readable, e.g., for speed, rad in vectors 
    # sum_sin: float = sum((speed * math.sin(rad)) for speed, rad in vectors)
    # sum_cos: float = sum((speed * math.cos(rad)) for speed, rad in vectors)

if __name__== "__main__":
    """ Main program to run if this module is called"""
    homework()
    # inputs 1: 13.000304779886218 (after modulo, same)
    # inputs 2: -0.9996952201137814 (after modulo, 359.0003047798862)
    # inputs 3: -169.99999999999997 (after modulo, 190.00000000000003)
