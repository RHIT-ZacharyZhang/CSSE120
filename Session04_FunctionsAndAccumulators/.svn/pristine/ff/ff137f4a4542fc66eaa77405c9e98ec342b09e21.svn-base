"""
This module demonstrates and practices:
  -- using ARGUMENTs in function CALLs,
  -- having PARAMETERs in function DEFINITIONs, and
  -- RETURNING a value from a function,
        possibly CAPTURING the RETURNED VALUE in a VARIABLE.

It also lets you contrast PRINTING versus RETURNING.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Yang Zhang.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    test_print_it()
    test_return_it()
    test_digits_in_squares_and_cubes()
    test_digits_in_power()
    # ------------------------------------------------------------------
    # TODO: 6. DO THIS LAST!
    #   We have supplied an automated "tester" for you.
    #   All you do is RUN the file  m5t_tester.py
    #   and look at its output:
    #
    #     -- If all of its tests indicate that they
    #          "COMPLETED SUCCESSFULLY!"
    #        then you are good to go.
    #
    #     -- If any of its tests do NOT complete successfully,
    #          then you are likely not TESTING the methods correctly
    #          based on the specification.
    #          In that case, ask a TA or your professor for help.
    # ------------------------------------------------------------------


def sum_of_digits(number):
    """
    Returns the sum of the digits in the given integer.
    For example, if the number is 83135,
    this function returns (8 + 3 + 1 + 3 + 5), which is 20.

    Precondition: the given argument is an integer.
    """
    # ------------------------------------------------------------------
    # Students:
    #   Do NOT touch this function - it has no TODO in it.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    #
    # Ask for help if you are unsure what it means to CALL a function.
    # The ONLY part of this function that you need to understand is
    # the green doc-string above.  Treat this function as a black box.
    # ------------------------------------------------------------------
    if number < 0:
        number = -number

    digit_sum = 0
    while True:
        if number == 0:
            break
        digit_sum = digit_sum + (number % 10)
        number = number // 10

    return digit_sum


def test_print_it():
    """ Tests the   print_it   function. """
    # ------------------------------------------------------------------
    # TODO: 2a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 3 tests, one of which uses n=10.
    #
    # HINT: Testing a function that PRINTS things is easy:
    #       just call the function.  Each call is one test.
    #       We have provided your first test for you.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   print_it   function:')
    print('--------------------------------------------------')

    # ------------------------------------------------------------------
    # TODO: 2b. Change   -999   below to what it should be,
    #           by figuring out BY HAND what the function should print.
    # ------------------------------------------------------------------
    expected = 1
    print('The next line should print', expected)
    print_it(10)
    expected = 19084
    print('The next line should print', expected)
    print_it(2)
    expected = 124309
    print('The next line should print', expected)
    print_it(35)


def print_it(n):
    """
    Given an integer n:
      -- Let X denote the sum of the digits in n ** 1000.
      -- Let Y denote the sum of the digits in n ** 999.
    PRINTs the sum of the digits in X ** Y.

    Test cases that you can use include:
      -- If n is 2, then:
            -- the sum of the digits in n ** 1000 is 1366.
            -- the sum of the digits in n ** 999 is 1367.
            -- so X ** Y is VERY LARGE in this case
                     (don't try to print it!)
            -- and the function should print 19084.
      -- If n is 35, then:
            -- the sum of the digits in n ** 1000 is 7021.
            -- the sum of the digits in n ** 999 is 7145.
            -- so X ** Y is VERY LARGE in this case
                     (don't try to print it!)
            -- and the function should print 124309.

    Precondition: the given argument is an integer.
    """
    # ------------------------------------------------------------------
    # TODO: 2c. Implement and test this function.
    #    Implementation requirement: CALL, as many times as needed,
    #    the    sum_of_digits    function that is DEFINED ABOVE.
    # ------------------------------------------------------------------
    X = sum_of_digits(n ** 1000)
    Y = sum_of_digits(n ** 999)
    Sum = X ** Y
    print(sum_of_digits(Sum))


def test_return_it():
    """ Tests the   return_it   function. """
    # ------------------------------------------------------------------
    # TODO: 3a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 3 tests, one of which is m=10.
    #
    # HINT: To test a function that RETURNs a value,
    #       the usual approach is either to:
    #         -- Use a unit testing tool
    #              (more on that in a subsequent lesson), or
    #         -- Call the function, capture the returned value in a
    #              variable, and print the variable's value.
    #              It is helpful to print the "expected" value too.
    #              Each call is one test.
    #       Use the latter approach here.
    #       We have provided part of your first test for you.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   return_it   function:')
    print('--------------------------------------------------')

    # ------------------------------------------------------------------
    # TODO: 3b. Change   -999   below to what it should be,
    #           by figuring out BY HAND what the function should return.
    # ------------------------------------------------------------------
    expected1 = 1
    answer1 = return_it(10)
    print('Expected, returned:', expected1, answer1)
    expected2 = 19084
    answer2 = return_it(2)
    print('Expected, returned:', expected2, answer2)
    expected3 = 124309
    answer3 = return_it(35)
    print('Expected, returned:', expected3, answer3)


def return_it(m):
    """
    Same specification as for   print_it   (defined above),
    except this function  RETURNs   the sum of the digits in X ** Y
    (where    print_it    PRINTED   that sum).
    """
    # ------------------------------------------------------------------
    # TODO: 3c. Implement and test this function.
    #    Implementation requirement: CALL, as many times as needed,
    #    the    sum_of_digits    function that is DEFINED ABOVE.
    # ------------------------------------------------------------------
    X = sum_of_digits(m ** 1000)
    Y = sum_of_digits(m ** 999)
    Sum = X ** Y
    return(sum_of_digits(Sum))


def test_digits_in_squares_and_cubes():
    """ Tests the   digits_in_squares_and_cubes   function. """
    # ------------------------------------------------------------------
    # TODO: 4a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 2 tests.
    # ------------------------------------------------------------------
    print()
    print('-----------------------------------------------------')
    print('Testing the   digits_in_squares_and_cubes   function:')
    print('-----------------------------------------------------')
    print('The next line should print 12 3 144 9 1728 18')
    digits_in_squares_and_cubes(12)
    print('The next line should print 15 6 225 9 3375 18')
    digits_in_squares_and_cubes(15)

def digits_in_squares_and_cubes(n):
    """
    Given an integer n, prints (on separate lines):
      - the integer and the sum of its digits
      - the integer squared and the sum of the digits in that number
      - the integer cubed and the sum of the digits in that number.
    For example, if the argument is 12, then this function prints:
      12 3
      144 9
      1728 18

    Precondition: the given argument is a positive integer.
    """
    # ------------------------------------------------------------------
    # TODO: 4b. Implement and test this function.
    #    Implementation requirement: CALL, as many times as needed,
    #    the    sum_of_digits    function that is DEFINED ABOVE.
    # ------------------------------------------------------------------
    x = sum_of_digits(n)
    m = n ** 2
    o = n ** 3
    y = sum_of_digits(m)
    z = sum_of_digits(o)
    print(n , x)
    print(m , y)
    print(o , z)


def test_digits_in_power():
    """ Tests the   digits_in_power   function. """
    # ------------------------------------------------------------------
    # TODO: 5a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 2 tests.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   digits_in_power   function:')
    print('--------------------------------------------------')
    print('The next line should print 18')
    digits_in_power(12, 3)
    print('The next line should print 26')
    digits_in_power(35, 3)



def digits_in_power(n, k):
    """
    Given integers n and k, returns the sum of the digits
    in n raised to the kth power. For example, if the arguments
    are 12 and 3, respectively, then this function returns 18
    since 12 to the 3rd power is 1728 (whose digits sum to 18).

    Preconditions: the arguments are positive integers.
    """
    # ------------------------------------------------------------------
    # TODO: 5b. Implement and test this function.
    #    Implementation requirement: CALL, as many times as needed,
    #    the    sum_of_digits    function that is DEFINED ABOVE.
    # ------------------------------------------------------------------
    num = n ** k
    print(sum_of_digits(num))

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
