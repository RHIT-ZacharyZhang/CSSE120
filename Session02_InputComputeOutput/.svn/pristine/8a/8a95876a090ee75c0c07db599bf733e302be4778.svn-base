"""
This module lets you practice:
  -- calling functions defined in  ** THIS **  module
  -- sending ARGUMENTS to those functions
  -- capturing RETURNED VALUES from those functions, in variables
  -- INPUT and OUTPUT

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Yang Zhang.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """
    Calls the   do_sums   and   do_shared_factors   functions
    to demonstrate and test them.
    """
    print()
    print('--------------------------------------------------')
    print('Testing the   do_sums   function:')
    print('--------------------------------------------------')
    do_sums()

    print()
    print('--------------------------------------------------')
    print('Testing the   do_shared_factors   function:')
    print('--------------------------------------------------')
    do_shared_factors()


def sum_of_digits(number):
    """
    Returns the sum of the digits in the given integer.
    For example, if the number is 83135,
    this function returns (8 + 3 + 1 + 3 + 5), which is 20.

    Precondition: the given argument is an integer.
    """
    # ------------------------------------------------------------------
    # Students:
    #   Do NOT touch this function.
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


def do_sums():
    """
    Prompts for and inputs three integers, one at a time
        (i.e., via 3 input statements).
        (The user is responsible for being sure to input integers.
        This function should NOT bother checking for valid input.)
    Then prints (each on its own line):
      -- the sum of the digits of the first integer
      -- the sum of the digits of the second integer
      -- the sum of the digits of the third integer
      -- the sum of those three sums
      -- the product of those three sums
      -- the sum of the digits in that product

    For example, if the user were to input 97, 13 and 204,
    then the function should print (on separate lines):
      16   4   6   26   384   15
    since:
      -- the sum of the digits of 97 is (9 + 7), which is 16
      -- the sum of the digits of 13 is (1 + 3), which is 4
      -- the sun of the digits of 204 is 2 + 0 + 4, which is 6
      -- the sum of those three sums is (16 + 4 + 6), which is 26
      -- the product of those three sums is (16 * 4 * 6), which is 384
      -- the sum of the digits in that product is (3 + 8 + 4), which is 15

    Another example:  if the user were to input 52, 184 and 3000,
    then the function should print (on separate lines):
       7   13   3   23   273   12
    Note: (7 + 13 + 3) = 23 and (7 * 13 * 3) = 273.
    """
    # ------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #   Implementation requirement: ** CALL**, as many times as needed,
    #   the    sum_of_digits    function that is DEFINED ABOVE.
    #   That function returns the sum of the digits of a given integer.
    #
    # HINT: To test this program:
    #   1. Run it, and actually input 97, 13 and 204.
    #      Confirm that your program prints:
    #         16   4   6   26   384   15
    #      per the example in the comment above.
    #
    #   2. Run it again, and actually input 52, 184 and 3000.
    #      Confirm that your program prints:
    #         7   13   3   23   273   12
    #   per the second example in the comment above.
    # ------------------------------------------------------------------
    sum1 = sum_of_digits(int(input('Enter the first interger:')))
    sum2 = sum_of_digits(int(input('Enter the second interger:')))
    sum3 = sum_of_digits(int(input('Enter the third interger:')))
    print(sum1)
    print(sum2)
    print(sum3)
    print(sum1 + sum2 + sum3)
    product = sum1 * sum2 * sum3
    print(product)
    print(sum_of_digits(product))


def number_of_shared_factors(m, n):
    """
    Returns the number of factors shared by m and n.

    For example, if m is 210 and n is 280, then this function returns 8,
    since   1  2  5  7  10  14  35  and 70  are the 8 integers that
    divide evenly into both 210 and 280.
    """
    # ------------------------------------------------------------------
    # Students:
    #   Do NOT touch this function.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    #
    # Ask for help if you are unsure what it means to CALL a function.
    # The ONLY part of this function that you need to understand is
    # the green doc-string above.  Treat this function as a black box.
    # ------------------------------------------------------------------
    count = 0
    for k in range(1, min(m + 1, n + 1)):
        if m % k == 0 and n % k == 0:
            count = count + 1

    return count


def do_shared_factors():
    """
    Prompts for and inputs two integers M and N, one at a time (i.e.,
    via 2 input statements -- no checking for valid input is necessary).
    Then prints:
      -- the number of factors shared by M and N
      -- the number of factors shared by (M * M) and (N * N)
      -- the number of factors shared by (M + 1) and (N + 1)

    Here are two sample runs (where the inputs are to the right of the
    colon signs, in each sample run).

        Enter an integer: 210
        Enter a second integer: 280
        8
        27
        1

        Enter an integer: 1038
        Enter a second integer: 123450
        4
        9
        1
    """
    # ------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #   Implementation requirement: ** CALL**, as many times as needed,
    #   the   number_of_shared_factors   function that is DEFINED ABOVE.
    # ------------------------------------------------------------------
    M = input('Enter an integer')
    N = input('Enter a secont integer')
    M = int(M)
    N = int(N)
    fac1 = number_of_shared_factors(M, N)
    fac2 = number_of_shared_factors(M * M, N * N)
    fac3 = number_of_shared_factors(M + 1, N + 1)
    print(fac1)
    print(fac2)
    print(fac3)

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
