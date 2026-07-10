""" Solution from Great Scott Gadgets SDR."""

import cmath
import matplotlib
matplotlib.use('QtAgg')
import  matplotlib.pyplot as plt

# Constnt
tau: float = 2 * cmath.pi

def create_plot() -> tuple:
    """ Create blank plot and return for use. """
    fig, ax = plt.subplots(figsize=(6,6))
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.grid = True
    ax.set_xlabel('Real')
    ax.set_ylabel('Imaginary')

    return fig, ax

def add_arrow(ax, vector: float) -> None:
    """ Add a vector arrow to a plot. """
    ax.arrow(0,0, vector.real, vector.imag, head_width=0.05,head_length=0.05, fc='r', ec='r')

def add_result(ax, result: float) -> None:
    """ Add a result arrow to the plot. """
    ax.arrow(0,0, result.real, result.imag, head_width=0.05,head_length=0.05, fc='b', ec='b')

def average_degrees(readings: list) -> float: 
    """ Average of complex numbers with vector addition. """
    # exponentiate base `e`, to the `1j` (python version of `i`, 
    #  imaginary unit) which gives 1 radian
    # multiply that by tau, making it 1 turn around the circle
    # divide by 360 to divide the complete turn into 360 parts
    #  Therefore, base is a copmlex number on the unit circle and is 1 degree 
    #  of rotation above the positive Real Axis
    
    fig, ax = create_plot()

    base = cmath.e ** (1j * tau / 360)
    total: float = 0
       
    for r in readings:
        # Very easy port to include scalars
        vector: float =  r[1] * (base ** r[0])
        total += vector
        add_arrow(ax, vector)

    avg_rad: float = total / len(readings)
    scalar: float = abs(avg_rad)

    add_result(ax, avg_rad)
    # Log with respect to the base
    #  This will give real and imaginary, only want the real part
    avg_degrees: float = cmath.log(avg_rad, base).real

    # Display the figure
    plt.show()

    return avg_degrees, scalar

if __name__== "__main__":
    """ Main program to run if this module is called"""
    # Initial solution only readings
    # print(average_degrees([12, 15, 13, 9, 16]))
    # print(average_degrees([358, 1, 359, 355, 2]))
    # print(average_degrees([210, 290, 10, 90, 170]))

    # Add list of tuples (direction, speed)
    print(average_degrees([(12, 1), (15, 1), (13, 1), (9, 1), (16, 1)]))
    print(average_degrees([(358, 1), (1, 1), (35, 1), (355, 1), (2, 1)]))
    
    # This gives average of vectors, so these being all different directions
    # means that the average direction is a "weak result" and the output of 
    # speed is close to 0; gives an indication of average wind/air motion
    # Different directions cancel each other out
    print(average_degrees([(210, 1), (290, 1), (10, 1), (90, 1), (170, 1)]))

 
