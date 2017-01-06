"""
This module lets you practice the ACCUMULATOR pattern
in several classic forms:
   SUMMING:    total = total + number
   COUNTING:   count = count + 1
   AVERAGING:  summing and counting combined
and
   FACTORIAL:  x = x * k

Subsequent modules let you practice the ACCUMULATOR pattern
in its "in graphics" form:
   IN GRAPHICS:   x = x + pixels

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Yang Zhang.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math
import random
import builtins  # Never necessary, but here for pedagogical reasons


# ----------------------------------------------------------------------
# Students: As you work each of these problems, ask yourself:
#   1. Do I need a loop?
#      If so, HOW MANY LOOPS?
#
#   2. Where I need a loop, what needs to happen:
#        -- BEFORE the loop?
#        -- IN the loop?
#        -- AFTER the loop?
# ----------------------------------------------------------------------
def main():
    """ Calls the   TEST   functions in this module. """
    test_sum_from()
    test_factorial()
    test_count_cosines_from()
    test_average()
    test_sum_unit_fractions_from()


# ----------------------------------------------------------------------
# TODO 2: READ the  test_sum_from  function (below).
#
#   When you have read it, asking questions as needed,
#   and you feel that you (mostly, at least) understand it,
#   and you feel that you understand from the example:
#     -- what an ORACLE answer is
#     -- what a KNOWN answer is
#     -- what a FORMULA answer is
#     -- how the above are used in testing
#   THEN:
#
#     ** Put  I GET IT  anywhere in this pink comment **
#     (but don't put yours on the preceding line, where it already is)
#
#   You can put that phrase on a new comment line (that begins
#   with a # or on an existing line, your choice.
# ----------------------------------------------------------------------
def test_sum_from():
    """ Tests the   sum_from   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_from   function:')
    print('--------------------------------------------------')

    # ------------------------------------------------------------------
    # These first two tests use an ORACLE for testing,
    # that is, a way to get the answer by using some other approach.
    #   The oracle here is the built-in    sum    function.
    # ------------------------------------------------------------------
    actual_answer = sum_from(6, 9)
    oracle_answer = builtins.sum(range(6, 10))
    test_case = 'sum_from(6, 9).  Actual, Oracle answers:'
    print('   Called ', test_case, actual_answer, oracle_answer)

    actual_answer = sum_from(100, 10000)
    oracle_answer = builtins.sum(range(100, 10001))
    test_case = 'sum_from(100, 10000).  Actual, Oracle answers:'
    print('   Called ', test_case, actual_answer, oracle_answer)

    # ------------------------------------------------------------------
    # This test uses a KNOWN answer
    #   (Everyone "knows" that the sum from 0 to 0 is 0.)
    # ------------------------------------------------------------------
    actual_answer = sum_from(0, 0)
    known_answer = 0
    test_case = 'sum_from(0, 0).  Actual, Known answers:'
    print('   Called ', test_case, actual_answer, known_answer)

    # ------------------------------------------------------------------
    # This test uses a FORMULA answer
    #   (which is a kind of ORACLE answer) that uses the formula:
    #     m + (m+1) + (m+2) +  ...  + n  =  (m + n) * (n - m + 1) / 2
    # ------------------------------------------------------------------
    actual_answer = sum_from(53, 4999)
    formula_answer = (53 + 4999) * (4999 - 53 + 1) // 2
    test_case = 'sum_from(53, 4999).  Actual, Formula answers:'
    print('   Called ', test_case, actual_answer, formula_answer)


def sum_from(m, n):
    """
    Returns the sum of the integers from m to n, inclusive.
    For example, sum_from(6, 9) returns 6 + 7 + 8 + 9, that is, 30.

    Precondition: m and n are integers and m <= n.
    """
    # ------------------------------------------------------------------
    # TODO: 3. Implement and test this function
    #          using an explicit    for ... in range(...)     statement.
    # ------------------------------------------------------------------
    result = 0
    for k in range(m , n + 1):
        result = result + k
    return result


def test_factorial():
    """ Tests the   factorial   function. """
    # ------------------------------------------------------------------
    # TODO: 4a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 4 tests.
    #
    # ** Use the  math.factorial  function as an ORACLE for testing. **
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   factorial   function:')
    print('--------------------------------------------------')
    actual_answer1 = factorial(5)
    oracle_answer1 = math.factorial(5)
    test_case1 = 'factorial(5)'
    print('Called', test_case1, actual_answer1, oracle_answer1)

    actual_answer2 = factorial(6)
    oracle_answer2 = math.factorial(6)
    test_case2 = 'factorial(6)'
    print('Called', test_case2, actual_answer2, oracle_answer2)

    actual_answer3 = factorial(10)
    oracle_answer3 = math.factorial(10)
    test_case3 = 'factorial(10)'
    print('Called', test_case3, actual_answer3, oracle_answer3)

    actual_answer4 = factorial(3)
    oracle_answer4 = math.factorial(3)
    test_case4 = 'factorial(5)'
    print('Called', test_case4, actual_answer4, oracle_answer4)


def factorial(n):
    """
    Returns n!, that is, n x (n-1) x (n-2) x ... x 1.
    For example, factorial(5) returns 5 x 4 x 3 x 2 x 1, that is, 120.

    Precondition: n is a non-negative integer.
    """
    # ------------------------------------------------------------------
    # TODO: 4b. Implement and test this function
    #          using an explicit    for ... in range(...)     statement.
    # ------------------------------------------------------------------
    result = 1
    for k in range(1, n + 1):
        result = result * k
    return result


def test_count_cosines_from():
    """ Tests the   count_cosines_from   function. """
    # ------------------------------------------------------------------
    # TODO: 5a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 4 tests.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   count_cosines_from   function:')
    print('--------------------------------------------------')
    num1 = count_cosines_from(3, 9, 0.29)
    print('The number of the result greater than x is', num1)
    num2 = count_cosines_from(3, 9, 0.27)
    print('The number of the result greater than x is', num2)
    num3 = count_cosines_from(3, 9, -5)
    print('The number of the result greater than x is', num3)
    num4 = count_cosines_from(-6, 9, 0.24)
    print('The number of the result greater than x is', num4)


def count_cosines_from(m, n, x):
    """
    Returns the number of integers from m to n, inclusive,
    whose cosine is greater than x.
    For example, since:
       cosine(3) is about -0.99
       cosine(4) is about -0.65
       cosine(5) is about 0.28
       cosine(6) is about 0.96
       cosine(7) is about 0.75
       cosine(8) is about -0.15
       cosine(9) is about -0.91

    count_cosines_from(3, 9, 0.29) returns 2
    count_cosines_from(3, 9, 0.27) returns 3
    count_cosines_from(4, 8, -0.5) returns 4

    Precondition: m and n are integers and m <= n, and x is a number.
    """
    # ------------------------------------------------------------------
    # TODO: 5b. Implement and test this function.
    # ------------------------------------------------------------------
    count = 0
    for k in range (m , n + 1):
        if math.cos(k) > x:
            count = count + 1
    return count


def test_average():
    """ Tests the   average   function. """
    # ------------------------------------------------------------------
    # TODO: 5a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 4 tests.  (We supplied 3 of them for you.)
    # HINT: Since the function to be tested is not deterministic,
    #       your tests may need to be STATISTICAL tests.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   average   function:')
    print('--------------------------------------------------')

    # ------------------------------------------------------------------
    # This is one way to test a randomized function.
    # Here, we set the "seed" to a particular (but arbitrary) value.
    # That determines the sequence of pseudo-random numbers
    # that will be generated.  So, assuming that the function generates
    # the psuedo-random numbers per that sequence, an oracle
    # (namely, your instructor) can predict the answer.
    # ------------------------------------------------------------------
    random.seed(42)

    # ------------------------------------------------------------------
    # Test 1:
    # ------------------------------------------------------------------
    avg = average(3, 100)
    print()
    print('You returned', avg)
    print('If you used the same random sequence as I did (as is likely),')
    print('Then the above should be about 32.666666666666664')

    # ------------------------------------------------------------------
    # Test 2:
    # ------------------------------------------------------------------
    avg = average(5, 10)
    print()
    print('You returned', avg)
    print('If you used the same random sequence as I did (as is likely),')
    print('Then the above should be about 2.6')

    # ------------------------------------------------------------------
    # Test 3: A  ** statistical ** test.
    # ------------------------------------------------------------------
    avg = average(1000, 9)
    print()
    print('You returned', avg)
    print('The above should be about half-way between 0 and 8.')
    print('i.e., about 4')

    # ------------------------------------------------------------------
    # TODO: Add one more STATISTICAL test here:
    # ------------------------------------------------------------------


def average(n, r):
    """
    Selects n random integers, each in the range [0, r).
    (That is, from 0 to r, but not including r.)
    Returns the AVERAGE of the selected numbers,
    that is, the SUM of the numbers divided by the NUMBER of numbers.

    Preconditions: n and r are positive integers.
    """
    # ------------------------------------------------------------------
    # TODO: 5b. Implement and test this function.
    #    HINT: Use the    random.randrange   function:
    #            random.randrange(0, r)
    #    returns a random number in the range [0, r).
    # ------------------------------------------------------------------
    total = 0
    for k in range(n):
        m = random.randrange(0, r)
        total = total + m
    average = total / n
    return average


def test_sum_unit_fractions_from():
    """ Tests the   sum_unit_fractions_from   function. """
    # ------------------------------------------------------------------
    # TODO: 6a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 4 tests.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_unit_fractions_from   function:')
    print('--------------------------------------------------')
    num1 = sum_unit_fractions_from(3, 9)
    print('The sum is', num1)
    num2 = sum_unit_fractions_from(4, 10)
    print('The sum is', num2)
    num3 = sum_unit_fractions_from(10, 9000)
    print('The sum is', num3)
    num4 = sum_unit_fractions_from(6, 9)
    print('The sum is', num4)


def sum_unit_fractions_from(m, n):
    """
    Returns the sum of 1/m + 1/(m+1) + 1/(m+2) + ... + 1/n.

    For example, sum_unit_fractions_from(6, 9) returns
       1/6 + 1/7 + 1/8 + 1/9, which is about 0.545635.

    Another example that you can use for testing:
      sum_unit_fractions_from(10, 9000)  is about  6.853

    Precondition: m and n are positive integers and m <= n.
    """
    # ------------------------------------------------------------------
    # TODO: 6b. Implement and test this function.
    # ------------------------------------------------------------------
    result = 0
    for k in range(m, n + 1):
        result = result + (1 / k)
    return result


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
