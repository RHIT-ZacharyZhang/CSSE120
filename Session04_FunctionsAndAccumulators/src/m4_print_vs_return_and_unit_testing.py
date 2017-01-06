"""
This module helps you understand:
  -- the difference between PRINT and RETURN
  -- UNIT TESTING.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Yang Zhang.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# ----------------------------------------------------------------------
# TODO 2: READ this (pink) comment.
#
#   When you have read it, asking questions as needed,
#   and you feel that you (mostly, at least) understand it, THEN:
#
#     ** Put    i get it   anywhere in this pink comment. **
#
#   You can put that phrase on a new comment line (that begins
#   with a # or on an existing line, your choice.
#
# Students often confuse PRINT and RETURN at this point of the course.
# They are quite different:
#   -- PRINT displays information on the console window,
#        for a human to see.
#   -- RETURN sends information from a function back to the calling
#        function.  The calling function then uses the information
#        as needed.
#
# For example, consider a program that plays a game.
# The software developer might break the program down (in part)
# like so that   main  calls f1, then repeatedly calls f2 and f3, where:
#    f1 - Constructs a RoseWindow and puts the desired background
#           images on it, and returns that RoseWindow.
#    f2 - Takes that RoseWindow, modifies the window as needed to get the
#           human's move, and returns the human's move
#    f3 - Takes that RoseWindow and the human's move,
#           computes the computer's move, modifies the RoseWindow
#           to display the human's and computer's moves,
#           and returns the modified RoseWindow.
#
# Do you see how if f2 just PRINTED the human's move,
# that would be of no help whatsoever to the program?
# The above example has flaws, but I hope that you get the idea.

# I GET IT!
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# TODO 3: (which continues the above): READ this (pink) comment.
#
#   When you have read it, asking questions as needed,
#   and you feel that you (mostly, at least) understand it, THEN:
#
#     ** Put    i get it   anywhere in this pink comment. **
#
#   You can put that phrase on a new comment line (that begins
#   with a # or on an existing line, your choice.
#
# The reason that students confuse PRINT and RETURN is because of
# how we do UNIT TESTING -- testing a UNIT (for you, a FUNCTION).
#
# Testing is a BIG topic, but let's keep it simple for now.
# The simplest way to test a function is (for a single test):
#   1. Call the function, capturing the returned value in variable.
#   2. Print the expected value (that you calculated by hand)
#        and the returned value,
# The human must compare those two values to be sure that they are
# the same (and if they are NOT the same, then either the implementation
# of the function OR the calculation of the expected value is wrong.
#
# See the code below for a single example.
#
# The reason that students confuse PRINT and RETURN is because at
# this point of the course, you will almost always test your functions
# using this capture-in-variable, then print approach.  From that alone,
# it looks like the function could just have PRINTED the result
# instead of RETURNing it.  But remember -- in REAL programs, functions
# rarely print anything; they RETURN values for other functions to use.
# We are teaching you practices that scale up, so we demand that most
# of the functions that you write from here on RETURN a value instead
# of PRINTing it.
# I GET IT!
# ----------------------------------------------------------------------

import rosegraphics as rg
import math


def main():
    """ Calls the   TEST   functions in this module. """
    test_distance()


def test_distance():
    """ Tests the distance function by using 2 tests. """
    expected1 = 5
    answer1 = distance(rg.Point(3, 4))
    print(expected1, answer1)

    expected2 = math.sqrt(2)
    answer2 = distance(rg.Point(1, 1))
    print(expected2, answer2)


def distance(point):
    """
    Returns the distance that the argument, an rg.Point,
    is from the point (0, 0).
    """
    x_squared = point.x * point.x
    y_squared = point.y * point.y

    return (math.sqrt(x_squared + y_squared))

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
