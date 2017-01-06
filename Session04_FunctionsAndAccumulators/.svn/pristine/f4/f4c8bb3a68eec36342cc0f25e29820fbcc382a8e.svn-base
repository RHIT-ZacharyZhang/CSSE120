"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Yang Zhang.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.
import math

def main():
    """ Calls the   TEST   functions in this module. """
    test_sum_cosines()
    test_sum_square_roots()


def test_sum_cosines():
    """ Tests the   sum_cosines   function. """
    # ------------------------------------------------------------------
    # TODO: 2a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 3 tests.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_cosines   function:')
    print('--------------------------------------------------')
    print('The next line should print 0.13416')
    total_1 = sum_cosines(3)
    print(total_1)
    print('The next line should print 0.71532')
    total_2 = sum_cosines(15)
    print(total_2)
    print('The next line should print 0.72435')
    total_3 = sum_cosines(6)
    print(total_3)


def sum_cosines(n):
    """
    Returns the sum of the cosines of the integers 0, 1, 2, ... n,
    for the given n.

    For example, sum_cosines(3) returns
       cos(0) + cos(1) + cos(2) + cos(3)   which is about 0.13416.

    Precondition: n is a non-negative integer.
    """
    # ------------------------------------------------------------------
    # TODO: 2b. Implement and test this function.
    # ------------------------------------------------------------------
    total = 0
    for k in range(n + 1):
        total = total + math.cos(k)
    return total



def test_sum_square_roots():
    """ Tests the   sum_square_roots   function. """
    # ------------------------------------------------------------------
    # TODO: 3a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 3 tests.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_square_roots   function:')
    print('--------------------------------------------------')
    print('The next line should print 11.8544')
    total1 = sum_square_roots(5)
    print(total1)
    print('The next line should print 57.2320')
    total2 = sum_square_roots(15)
    print(total2)
    print('The next line should print 121.1044')
    total3 = sum_square_roots(25)
    print(total3)


def sum_square_roots(n):
    """
    Returns the sum of the square roots of the integers
        2, 4, 6, 8, ... 2n    for the given n.
    So if n is 7, the last term of the sum is for 14 (not 7).

    For example, sum_square_roots(5) returns
       sqrt(2) + sqrt(4) + sqrt(6) + sqrt(8) + sqrt(10),
    which is about 11.854408.

    Precondition: n is a non-negative integer.
    """
    # ------------------------------------------------------------------
    # TODO: 3b. Implement and test this function.
    # ------------------------------------------------------------------
    total = 0
    for k in range(2, 2 * n + 2, 2):
        total = total + math.sqrt(k)
    return total


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
