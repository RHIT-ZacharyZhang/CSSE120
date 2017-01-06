"""
Test 1, problem 2.

Authors: David Mutchler, Chandan Rupakheti, their colleagues,
         and Yang Zhang.  Summer 2015.
"""  # DONE: PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem2a()
    test_problem2b()


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


def test_problem2a():
    """ Tests the   problem2a   function. """
    # ------------------------------------------------------------------
    # TODO: Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 4 tests, i.e., 4 calls to the function to test.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2a   function:')
    print('--------------------------------------------------')
    print(problem2a(4, 2))
    print(problem2a(105, 2))
    print(problem2a(2, 5))
    print(problem2a(3, 6))



def problem2a(m, p):
    """
    Returns the number of prime numbers from m
    to (m to the pth power), where m and p are the given arguments.
    Do NOT include (m to the pth power) as one of the integers
    that you check, as it is definitely NOT a prime number.

    For example, if m is 4 and p is 2, this function examines
    the primes numbers from 4 to 15.  Those prime numbers are:
       5   7   11   13
    so this function returns 4 in this case.

    Other tests you can use:
      -- When m is 105 and p is 2, this function should return 1309.
      -- When m is 2 and p is 5, this function should return 11.

    Preconditions: m and p are integers and each is at least 2.
    """
    # ------------------------------------------------------------------
    # TODO: Implement and test this function.
    # IMPLEMENTATION REQUIREMENT:
    #    Use (call) the above  function(s) as appropriate.
    # ------------------------------------------------------------------
    total = 0
    for k in range(m, m ** p):
        if is_prime(k):
            total = total + 1
    return total


def test_problem2b():
    """ Tests the   problem2b   function. """
    # ------------------------------------------------------------------
    # TODO: Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 4 tests, i.e., 4 calls to the function to test.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   problem2b   function:')
    print('--------------------------------------------------')
    print(problem2b(4, 2))
    print(problem2b(105, 2))
    print(problem2b(2, 5))
    print(problem2b(3, 6))


def problem2b(m, p):
    """
    Returns the sum of the digits of the prime numbers from m
    to (m to the pth power), where m and p are the given arguments.
    Do NOT include (m to the pth power) as one of the integers
    that you check, as it is definitely NOT a prime number.

    For example, if m is 4 and p is 2, this function examines
    the primes numbers from 4 to 15.  Those prime numbers are:
       5   7   11   13
    The sum of the digits of all those prime numbers is
       5 + 7 + (1 + 1) + (1 + 3), which is 18,
    so that is what this function returns in this case.

    Other tests you can use:
      -- When m is 105 and p is 2, this function should return 23536.
      -- When m is 2 and p is 5, this function should return 61.

    Preconditions: m and p are integers and each is at least 2.
    """
    # ------------------------------------------------------------------
    # TODO: Implement and test this function.
    # IMPLEMENTATION REQUIREMENT:
    #    Use (call) the above  function(s) as appropriate.
    # ------------------------------------------------------------------
    result = 0
    for k in range(m, m ** p):
        if is_prime(k):
            result = result + sum_of_digits(k)
    return result


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
