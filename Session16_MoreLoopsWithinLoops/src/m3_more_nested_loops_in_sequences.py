"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of SEQUENCES OF SUB-SEQUENCES.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and PUT YOUR NAME HERE.  February 2014.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the other functions to test them. """
    test_largest_negative_number()
    test_keep_integers()


def test_largest_negative_number():
    """ Tests the    largest_negative_number    function. """
    # ------------------------------------------------------------------
    # TODO: 2a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include enough tests to give you confidence that your solution
    #   to this challenging problem is indeed correct.
    # ------------------------------------------------------------------
    print()
    print('-------------------------------------------------')
    print('Testing the   LARGEST_NEGATIVE_NUMBER   function:')
    print('-------------------------------------------------')
    seq1 = 


def largest_negative_number(seq_seq):
    """
    Returns the largest NEGATIVE number in the given sequence of
    sequences of numbers.  Returns None if there are no negative numbers
    in the sequence of sequences.

    For example, if the given argument is:
        [(30, -5, 8, -20),
         (100, -2.6, 88, -40, -5),
         (400, 500)
        ]
    then this function returns -2.6.

    As another example, if the given argument is:
      [(200, 2, 20), (500, 400)]
    then this function returns None.

    Preconditions:
      :type seq_seq: (list, tuple)
    and the given argument is a sequence of sequences,
    where each subsequence contains only numbers.
    """
    # ------------------------------------------------------------------
    # TODO: 2b. Implement and test this function.
    # ------------------------------------------------------------------


def test_keep_integers():
    """ Tests the    keep_integers    function. """
    # ------------------------------------------------------------------
    # TODO: 3a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include enough tests to give you confidence that your solution
    #   to this challenging problem is indeed correct.
    #
    # IMPORTANT: Be sure to ** test ** that your  keep_integers
    #   function below MUTATES its argument, per its specification.
    #   Your  keep_integers  function should return None
    #   since no return value is specified.
    # ------------------------------------------------------------------
    print()
    print('---------------------------------------')
    print('Testing the   KEEP_INTEGERS   function:')
    print('---------------------------------------')


def keep_integers(seq_seq):
    """
    MUTATES the given list of sequences as follows:  It keeps ONLY
    the items in the list that contain ONLY integers.
    For example, if the given argument is:
        [(3, 1, 4),
         (10, 'hi', 10),
         [1, 2.5, 3, 4],
         'hello',
         [],
         ['oops'],
         [30, -4]
        ]
    then this function MUTATES that argument into:
        [(3, 1, 4),
         [],
         [30, -4]
        ]
    Preconditions:  the given argument is a list of sequences.
    """
    # ------------------------------------------------------------------
    # TODO: 3b. Implement and test this function.
    #
    # HINTS:
    #  -- An elegant way to keep the indexing consistent while
    #     deleting items from the exterior sequence is to go through the
    #     exterior sequence BACKWARDS.
    #  -- One way to delete an item from a list is like this:
    #        del x[r]
    #     This example deletes the item at index r in the list x.
    #  -- Also, there is a completely different approach to this problem
    #     that uses the   copy, clear, append   list methods.
    # ------------------------------------------------------------------

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
