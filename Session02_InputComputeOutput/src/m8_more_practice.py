"""
This module lets you practice:
  -- calling functions from the MATH and RANDOM modules
  -- sending ARGUMENTS to those functions
  -- capturing RETURNED VALUES from those functions,
       in variables (i.e. names)
  -- INPUT and OUTPUT

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Yang Zhang.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # TODO: 2. Implement and test this function.
    print_distance_to_origin()
    print_logarithm()


def print_distance_to_origin():
    """
    Prompts for and gets (in the console, from the user)
    two floating-point numbers (using two input statements):
       an x-coordinate, then a y-coordinate.
    Prints the distance from that (x, y) to the origin (0, 0).

    Here is are TWO sample runs, where the user inputs
    are to the right of the colons:

       Enter an x-coordinate: 7.4
       Enter a y-coordinate: 12.6
       14.612323566086264

       Enter an x-coordinate: 4
       Enter a y-coordinate: 3
       5.0
    """
    # TODO: 3. Implement and test this function.
    # HINT: The    math.sqrt    function will be helpful.
    x = float(input('Enter an x-coordinate:'))
    y = float(input('Enter a y-coordinate:'))
    distance = math.sqrt(x ** 2 + y ** 2)
    print(distance)


def print_logarithm():
    """
    Prompts for and gets (in the console, from the user)
    a floating-point number.
    Then prints a message of the following form:

       The base-10 logarithm of XXX is YYY

    where XXX is the number that the user enters
    and YYY is the base-10 logarithm of that number.

    Here is are TWO sample runs, where the user inputs
    are to the right of the colons:

       Enter a number: 35.14
       The base-10 logarithm of 35.14 is 1.5458017571592761

       Enter a number: 10000
       The base-10 logarithm of 10000.0 is 4.0
    """
    # TODO: 4. Implement and test this function.
    # HINT: the    math.log10   function will be helpful.
    XXX = float(input('Enter a number:'))
    YYY = math.log10(XXX)
    print('The base-10 logarithm of', XXX, 'is', YYY)

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
