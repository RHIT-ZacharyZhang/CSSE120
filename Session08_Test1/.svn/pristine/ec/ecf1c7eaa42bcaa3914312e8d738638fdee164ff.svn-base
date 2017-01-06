"""
Test 1, problem 1.

Authors: David Mutchler, Chandan Rupakheti, their colleagues,
         and Yang Zhang.  Summer 2015.
"""  # DONE: PUT YOUR NAME IN THE ABOVE LINE.

import math
def main():
    """ Calls the   TEST   functions in this module. """
    test_problem1()


def test_problem1():
    """ Tests the   problem1   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1   function:')
    print('--------------------------------------------------')
    problem1()


def problem1():
    """
    Prompts the user for and inputs:
      -- A floating point number
      -- A positive integer
      -- A string
    in that order (via three separate inputs).
    Then prints, in this order, all on separate lines:
      -- The cosine of the floating point number
      -- The string, repeated the input integer number of times
      -- The input integer, repeated the input integer number of times.
    No input validation is required.  Nothing else should be printed.

    Here is a sample run, where the user input is to the right
    of the colons:
         Enter a floating point number: 2.5
         Enter a positive integer: 3
         Enter a string: March Madness!
         -0.8011436155469337
         March Madness!
         March Madness!
         March Madness!
         3
         3
         3

    Here is another sample run, again with user input after colons:
         Enter a floating point number: -1
         Enter a positive integer: 2
         Enter a string: Who is on first?
         0.5403023058681397
         Who is on first?
         Who is on first?
         2
         2
    """
    # TODO: Implement and test this function.
    #     The testing code is already written for you (above).
    n1 = float(input('Enter a floating number:'))
    n2 = int(input('Enter a positive integer:'))
    string1 = str(input('Enter a string:'))
    print(math.cos(n1))
    for k in range (n2):
        print(string1)
    for k in range (n2):
        print(n2)


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
