"""
This module lets you practice the INPUT-COMPUTE-OUTPUT pattern,
including:
  -- INPUT numbers (using input and float and int)
  -- COMPUTE (using variables and arithmetic operators)
  -- OUTPUT (using print)
  -- CALLING a function from main.

For a simple example of input/compute/output, see the module:
     m0e_input_compute_output

For a more elaborate (and commented) example that includes multiple
function definitions, see the module:
     m1e_input_compute_output_in_functions

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Yang Zhang.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # ------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #
    #   ** IMPORTANT NOTE: **
    #   You will see "implement and test" a lot.
    #   Here is what they mean for us at this point of the course:
    #
    #     -- IMPLEMENT:
    #          1. Read the green doc-string that precedes the TODO.
    #             It says what the function should do.
    #          2. Write code below the pink TODO that makes the function
    #             do what the green doc-string said it should do.
    #
    #     -- TEST:
    #          1. Run the function after implementing it.
    #          2. If the function behaves as hoped for, you are done
    #             with the exercise.  If not, fix your implementation
    #             and re-test.
    #
    #   Later in the course, we will discuss and you will use
    #   more elaborate processes for implement/test.
    # ------------------------------------------------------------------
    rectangle_area()
    raise_to_power()
    cylinder_volume()


def rectangle_area():
    """
    Prompts for and inputs the width and height of a rectangle
    (as floating point numbers) and prints the area of the rectangle.

    Here is a sample run (where the inputs are to the right of the
    colon signs):
        Enter the width of the rectangle: 4.5
        Enter the height of the rectangle: 8
        36.0
    """
    # TODO: 3. Implement and test this function.
    input_string = input('Enter the width of the rectangle:')
    width = float(input_string)
    input_string2 = input('Enter the height of the rectangle:')
    height = float(input_string2)
    rectangle_area = width * height
    print(rectangle_area)

def raise_to_power():
    """
    Prompts for and inputs:
      -- a floating point number X
      -- an integer N
    Prints X raised to the Nth power.

    Here is a sample run (where the inputs are to the right of the
    colon signs):
        Enter a number: 3.8
        Enter an integer: 6
        3010.936383999999

    Note: Whenever you compute a floating-point number, your answer
    might differ from the sample in the last few decimal places,
    depending on how you computed the value.  No problem if so.
    """
    # ------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    # Hints:
    #  -- Use  float  to convert to a floating point number
    #     but   int   to convert to an integer
    #  -- Use   **  for raising to a power
    # ------------------------------------------------------------------
    input_string = input('Enter a number:')
    X = float(input_string)
    input_string2 = input('Enter an integer:')
    N = float(input_string2)
    number = X ** N
    print(number)


def cylinder_volume():
    """
    Prompts for and inputs the diameter and height of a cylinder
    (as floating point numbers) and prints the volume of the cylinder.

    Here is a sample run (where the inputs are to the right of the
    colon signs):
        Enter the diameter of the cylinder: 8.55
        Enter the height of the cylinder: 4.2
        241.14119080700027

    Note: Whenever you compute a floating-point number, your answer
    might differ from the sample in the last few decimal places,
    depending on how you computed the value.  No problem if so.
    """
    # ------------------------------------------------------------------
    # TODO: 5. Implement and test this function.
    # Hint: You need PI in this formula.  For PI, use the "dot trick",
    # that is, type:
    #    math,
    #    then a dot,
    #    then pause, then look for what to select/type.
    # ------------------------------------------------------------------
    input_string = input('Enter the diameter of the cylinder:')
    d = float(input_string)
    input_string2 = input('Enter the height of the cylinder:')
    h = float(input_string2)
    volume = ((d / 2) ** 2) * math.pi * h
    print(volume)


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
