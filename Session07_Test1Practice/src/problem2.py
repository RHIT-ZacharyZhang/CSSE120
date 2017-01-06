"""
PRACTICE Test 1, problem 2.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Yang Zhang.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math
def main():
    """ Calls the   TEST   functions in this module. """
    test_problem2a()
    test_problem2b()
    test_problem2c()


def test_problem2a():
    """ Tests the   problem2a   function. """
    # ------------------------------------------------------------------
    # TODO: 2a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 4 tests, i.e., 4 calls to the function to test.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2a   function:')
    print('--------------------------------------------------')
    answer1 = problem2a(3, 5)
    expected1 = -1.601
    print('Actual answer:', answer1, 'Ecpected:', expected1)
    answer2 = problem2a(1, -2)
    expected2 = -1.135
    print('Actual answer:', answer2, 'Ecpected:', expected2)
    answer3 = problem2a(30, 100)
    expected3 = 1.278
    print('Actual answer:', answer3, 'Ecpected:', expected3)
    answer4 = problem2a(1, 2)
    expected4 = 1.13509
    print('Actual answer:', answer4, 'Ecpected:', expected4)

def problem2a(m, n):
    """
    Returns the sum of the sines of the integers from m squared
    to n squared, inclusive, where m and n are the given arguments.

    For example, if m is 3 and n is 5, this function returns:
       sine(9) + sine(10) + sine(11) +  ...  + sine(24) + sine(25)

    Preconditions: m and n are integers and the absolute value of m
                   is less than the absolute value of n.

    Examples that you can (AND SHOULD) use for testing include:
      When m is 3 and n is 5, the correct answer is about -1.601.
      When m is 1 and n is -2, the correct answer is about 1.135.
      When m is 30 and n is 100, the correct answer is about 1.278.
    """
    # ------------------------------------------------------------------
    # TODO: 2b. Implement and test this function.
    # ------------------------------------------------------------------
    result = 0
    for k in range(m ** 2, n ** 2 + 1):
        result = result + math.sin(k)
    return result

def is_prime(n):
    """
    Returns True if the given integer is prime, else returns False.

    Note: The algorithm used here is simple and clear but slow.

    Precondition:  The given argument is an integer that is at least 2.
    """
    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False

    return True
    # ------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  is_prime  function - it has no TODO.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # ------------------------------------------------------------------


def test_problem2b():
    """ Tests the   problem2b   function. """
    # ------------------------------------------------------------------
    # TODO: 3a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 4 tests, i.e., 4 calls to the function to test.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2b   function:')
    print('--------------------------------------------------')
    print(problem2b(3, 5))
    print(problem2b(2, 1))
    print(problem2b(2, 20))
    print(problem2b(1, 4))


def problem2b(m, f):
    """
    Returns the number of integers from m to (f * m), inclusive,
    that are prime.

    For example, if m is 3 and f is 5, this function returns 5,
       since 3, 5, 7, 11, and 13 are the integers between 3 and 15,
       inclusive, that are prime.

    Preconditions: m and f are positive integers and m is at least 2.

    Examples that you can (AND SHOULD) use for testing include:
      When m is 3 and f is 5, the correct answer is 5.
      When m is 2 and f is 1, the correct answer is 1
        (since 2 is the only prime between 2 and 2, inclusive).
      When m is 5 and f is 40, the correct answer is 44.
    """
    # ------------------------------------------------------------------
    # TODO: 3b. Implement and test this function.
    # IMPLEMENTATION REQUIREMENT:
    #    Use (call) the   is_prime   function above appropriately.
    # ------------------------------------------------------------------
    count = 0
    for k in range(m, f * m + 1):
        if is_prime(k):
            count = count + 1
    return count

def sum_of_digits(number):
    """
    Returns the sum of the digits in the given integer.
    For example, if the number is 83135,
    this function returns (8 + 3 + 1 + 3 + 5), which is 20.

    Precondition: the given argument is an integer.
    """
    # ------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  sum_of_digits function - it has no TODO.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
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


def test_problem2c():
    """ Tests the   problem2c   function. """
    # ------------------------------------------------------------------
    # TODO: 4a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 4 tests, i.e., 4 calls to the function to test.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2c   function:')
    print('--------------------------------------------------')
    print(problem2c(20, 50))
    print(problem2c(50, 60))
    print(problem2c(25, 35))
    print(problem2c(28, 55))


def problem2c(m, n):
    """
    Let's say that an integer X is STRANGE if and only if:
      1. X is prime, OR
      2. the sum of the digits of X is odd,
    BUT NOT BOTH.

    For example, the following are STRANGE:
       31 (IS prime, and sum of digits is NOT odd)
       32 (NOT prime and sum of digits IS odd)
    while the following are NOT STRANGE:
       33 (neither prime nor sum of digits is odd)
       41 (prime AND sum of digits is odd)

    This function returns the number of integers from m to n,
    inclusive, that are STRANGE.

    To assist your testing, here are all the STRANGE integers
    between 20 and 50, inclusive:
       21  25  27  30  31  32  34  36  37  38  45  49  50

    Preconditions: m and n are positive integers, m is at least 2
                   and m <= n.
    """
    # ------------------------------------------------------------------
    # TODO: 4b. Implement and test this function.
    # IMPLEMENTATION REQUIREMENT:
    #    Use (call) the  is_prime  AND the  sum_of_digits  functions,
    #    both defined above, as appropriate.
    # ------------------------------------------------------------------
    count = 0
    for k in range(m, n + 1):
        if (is_prime(k) and (sum_of_digits(k) % 2) == 0) or (is_prime(k) == False and (sum_of_digits(k) % 2) != 0):
            count = count + 1

    return count


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
