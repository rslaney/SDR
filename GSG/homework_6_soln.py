""" Solution from Great Scott Gadgets SDR."""

import cmath
tau: float = 2 * cmath.pi

def average_degrees(readings: list) -> float: 
    """ Average of complex numbers with vector addition. """
    # exponentiate base `e`, to the `1j` (python version of `i`, 
    #  imaginary unit) which gives 1 radian
    # multiply that by tau, making it 1 turn around the circle
    # divide by 360 to divide the complete turn into 360 parts
    #  Therefore, base is a copmlex number on the unit circle and is 1 degree 
    #  of rotation above the positive Real Axis
    base = cmath.e ** (1j * tau / 360)

    total: float = 0

    for r in readings:
        total += base ** r
    
    avg_rad: float = total / len(readings)

    # Log with respect to the base
    #  This will give real and imaginary, only want the real part
    avg_degrees: float = cmath.log(avg_rad, base).real

    return avg_degrees

if __name__== "__main__":
    """ Main program to run if this module is called"""
    print(average_degrees([12, 15, 13, 9, 16]))
    print(average_degrees([358, 1, 359, 355, 2]))
    print(average_degrees([210, 290, 10, 90, 170]))
    # inputs 1: 13.000304779886218 (after modulo, same)
    # inputs 2: -0.9996952201137814 (after modulo, 359.0003047798862)
    # inputs 3: -169.99999999999997 (after modulo, 190.00000000000003)

