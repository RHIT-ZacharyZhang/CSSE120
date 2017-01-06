"""
Previous modules showed how to:
  -- CALL a function defined in another module
  -- capture the RETURNED VALUE in a variable

as in these examples:

   s = math.sin(3.5)
   random1 = random.uniform(-30, 10)
   y = max(s, random1)

This module shows how to do the same, but with functions
that are  defined in THIS module itself.  For example:

1. The function  exp_approximation(x, n)
   is defined below.  It computes an approximation of (e ** x)
   [the bigger that n is, the better the approximation].

2. Subsequent functions CALL  exp_approximation  to do what they
   need done, passing whatever arguments are appropriate to solve
   their problems.

This module also shows how to DEFINE functions with PARAMETERS,
although we will not study that topic until a subsequent session.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti,
         Claude Anderson, Katie Dion, Delvin Defoe, Curt Clifton
         and their colleagues, based on the work of Jacob Bernoulli
         and other mathematicians.  December 2013.
"""
# ----------------------------------------------------------------------
# Students: Read and run this program.  There is nothing else
#           for you to do here.  Just use it as an example to see how
#           code that your write can:
#
#   1. CALL functions defined in OTHER modules,
#         as in    math.sin(0.53)
#
#   2. CALL functions defined in THIS module,
#         as in    exp_approximation(4.5, 100)
#      where   exp_approximation   is defined in THIS module.
#
#   3. Capture a RETURNED VALUE from a function,
#        storing it in a VARIABLE for subsequent use.
#
# ----------------------------------------------------------------------
import math


def main():
    """ Calls the other functions herein to demonstrate them. """
    print()
    print('-----------------------------------------------------------')
    print('Demonstrating the   bad_better_best   function:')
    print('-----------------------------------------------------------')
    bad_better_best()

    print()
    print('-----------------------------------------------------------')
    print('Demonstrating the   practice_using_exp_approximation   function:')
    print('-----------------------------------------------------------')
    practice_using_exp_approximation()

    print()
    print('-----------------------------------------------------------')
    print('Demonstrating the   example_of_function_composition   function:')
    print('-----------------------------------------------------------')
    example_of_function_composition()


def exp_approximation(x, n):
    """
    RETURNs the sum:
       0  +  (x / 1!)  +  (x**2 / 2!)  +  (x**3 / 3!)  +
                                                   ... +  (x**n / n!)
    where n! is (n factorial), that is, n * (n-1) * (n-2) * ... * 2 * 1.

    It so happens that this sum is a good approximation to (e ** x)
    (that is, e raised to the xth power, where e is about 2.618),
    when n is large.

    Preconditions: x is a number and n is a positive integer.
    """
    total = 0
    for k in range(n + 1):
        total = total + ((x ** k) / math.factorial(k))

    return total

# ----------------------------------------------------------------------
# Students: Note how the following functions CALL the ABOVE function
#    exp_approximation
#
# Note that to use (call)  exp_approximation  in solving the problems
# below, the author:
#   -- did NOT need to understand the CODE in  exp_approximation
#   -- DID need to understand the green doc-string that says what
#        exp_approximation  does.
# ----------------------------------------------------------------------


def bad_better_best():
    """
    Computes and prints e to the 4.5th power computed in various ways.
    Computes and prints e computed in various ways.
    """
    total1 = exp_approximation(4.5, 3)
    total2 = exp_approximation(4.5, 15)
    total3 = exp_approximation(4.5, 100)
    print()
    print('Three approximations of e to the 4.5th power are:')
    print('   ', total1)
    print('   ', total2)
    print('   ', total3)
    print('My computer claims that e to the 4.5th power is: ',
          math.pow(math.e, 4.5))

    lousy_approximation = exp_approximation(1, 2)
    better_approximation = exp_approximation(1, 5)
    good_approximation = exp_approximation(1, 1000)
    print()
    print('A lousy approximation of e is: ', lousy_approximation)
    print('A better approximation of e is:', better_approximation)
    print('A good approximation of e is:  ', good_approximation)
    print('My computer claims that e is:  ', math.e)


def practice_using_exp_approximation():
    """
    Prompts for and inputs a floating-point number X.

    Then prints (each on its own line):
      -- e ** X
      -- e ** (e ** X)
      -- sine of (e ** (e ** X))

    Then prints (each on its own line):
      -- BAD approximations of each of the first 3 items above
      -- GOOD approximations of each of the first 3 items above
    """
    # ------------------------------------------------------------------
    # Implementation requirements:
    #   -- Compute all the NON-approximations by using  math.exp.
    #   -- Compute all the APPROXIMATIONS by calling  exp_approximation
    #        (defined above) as many times as needed.
    # ------------------------------------------------------------------
    x = float(input('Enter a number between -41 and 6.5: '))

    # Values per the  math.exp  function.
    eX = math.exp(x)
    eeX = math.exp(eX)
    seeX = math.sin(eeX)

    print()
    print('Values for the 3 quantities per the  math.exp  function:')
    print(eX)
    print(eeX)
    print(seeX)

    # Bad approximations (any small integer like 3 works for this):
    bad_eX = exp_approximation(x, 3)
    bad_eeX = exp_approximation(bad_eX, 3)
    bad_seeX = math.sin(bad_eeX)

    print()
    print('Bad approximations for the 3 quantities:')
    print(bad_eX)
    print(bad_eeX)
    print(bad_seeX)

    # Good approximations (large integers like 100  work for this):
    good1 = exp_approximation(x, 100)
    good2 = exp_approximation(good1, 100)
    good3 = math.sin(good2)

    print()
    print('Good approximations for the 3 quantities:')
    print(good1)
    print(good2)
    print(good3)


def example_of_function_composition():
    """
    Same as the previous function, but uses function COMPOSITION,
    i.e. functions that call functions that call functions ...
    """
    # ------------------------------------------------------------------
    # Students: compare this code to that of the previous example.
    # They both accomplish the same thing.
    # Which feels 'better' to you?
    #   (Both have their good and bad points.)
    #
    # Also, try runs in which you enter numbers that are:
    #  -- too big (6.6 or more)
    #  -- too small (-42 or less)
    # You will see in doing so that floating point numbers have limits
    # on their size and precision.
    # ------------------------------------------------------------------
    x = float(input('Enter a number between -41 and 6.5: '))

    print()
    print('Values for the 3 quantities per the  math.exp  function:')
    print(math.exp(x))
    print(math.exp(math.exp(x)))
    print(math.sin(math.exp(math.exp(x))))

    print()
    print('Bad approximations for the 3 quantities:')
    print(exp_approximation(x, 3))
    print(exp_approximation(exp_approximation(x, 3), 3))
    print(math.sin(exp_approximation(exp_approximation(x, 3), 3)))

    print()
    print('Good approximations for the 3 quantities:')
    print(exp_approximation(x, 100))
    print(exp_approximation(exp_approximation(x, 100), 100))
    print(math.sin(exp_approximation(exp_approximation(x, 100), 100)))

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
