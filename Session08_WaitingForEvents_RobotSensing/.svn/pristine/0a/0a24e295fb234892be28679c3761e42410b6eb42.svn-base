"""
This module lets you practice the WAIT-UNTIL-EVENT pattern:
   while True:
       ...
       if <event has occurred>:
           break
       ...
in the context of waiting for an accumulator to exceed a value.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Yang Zhang.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
import random


def main():
    """ Calls the   TEST   functions in this module. """
    test_wait_for_sum_of_cubes()
    test_random_walk()


def test_wait_for_sum_of_cubes():
    """ Tests the   wait_for_sum_of_cubes    function. """
    # ------------------------------------------------------------------
    # TODO: 2a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include   wait_for_sum_of_cubes(30.33)   as one of your tests
    #   (so figure out by hand what the correct answer is for that).
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   wait_for_sum_of_cubes   function:')
    print('--------------------------------------------------')
    n = wait_for_sum_of_cubes(6)
    print('For x = 6')
    print('Returned, expected:', 2, n)
    n = wait_for_sum_of_cubes(30.33)
    print('For x = 30.33')
    print('Returned, expected:', 3, n)


def wait_for_sum_of_cubes(x):
    """
    Returns the smallest positive integer n such that the sum
      1 cubed  +  2 cubed  +  3 cubed  +  ...  + n cubed
    is greater than or equal to x.

    Some examples:
      -- if x is 4.3 (or any number in the range (1, 9],
            i.e. greater than 1 but less than or equal to 9),
            this function returns 2 because:
              1 cubed = 1 which is less than 4.3
            but
              1 cubed + 2 cubed = 9 which is greater than or equal to 4.3
      -- if x is 58 (or any number in the range (36, 100]),
            this function returns 4 because:
              1 cubed + 2 cubed + 3 cubed = 36
              which is less than 58
            but
              1 cubed + 2 cubed + 3 cubed + 4 cubed = 100
              which is greater than or equal to 58
      -- if x is 1000, this function returns 8 because:
              1 + 8 + 27 + 64 + ... + (7**3) = 784
            but
              1 + 8 + 27 + 64 + ... + (8**3) = 1296
      -- if x is 1296, this function returns 8 (per previous calculation)
      -- if x is -5.2 (or any number less than or equal to 1),
           this function returns 1.

    Precondition: x is a number.
    """
    # ------------------------------------------------------------------
    # TODO: 2b. Implement and test this function.
    #    Implementation requirement:
    #       -- Solve this using the   wait-until-event   pattern.
    #       -- Note for the mathematically inclined:  one could figure
    #            out (or look up) a formula that would allow a faster
    #            computation.  But no fair using that in this function.
    # ------------------------------------------------------------------
    total = 0
    n = 0
    while True:
        n = n + 1
        total = total + n ** 3
        if total >= x:
            break
    return n


def test_random_walk():
    """ Tests the   random_walk    function. """
    # ------------------------------------------------------------------
    # TODO: 3a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    # Note:  Because there is randomness in the function you are to
    #   implement, you cannot easily obtain deterministic tests.
    #   But you CAN do graphical tests (watch the circle move, does
    #   it seem to jiggle up and down right) and sanity checks
    #   (is the returned value reasonable?).
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   random_walk   function:')
    print('--------------------------------------------------')
    window = rg.RoseWindow(700, 700)
    circle1 = rg.Circle(rg.Point(200, 100), 35)
    circle1.fill_color = 'blue'
    probability_up = 0.3
    pixels_to_move = 8
    print('The number of movements:', random_walk(window, circle1, probability_up, pixels_to_move))
    circle2 = rg.Circle(rg.Point(400, 200), 50)
    circle2.fill_color = 'green'
    probability_up = 0.5
    pixels_to_move = 10
    print('The number of movements:', random_walk(window, circle2, probability_up, pixels_to_move))
    circle3 = rg.Circle(rg.Point(600, 300), 45)
    circle3.fill_color = 'red'
    probability_up = 0.8
    pixels_to_move = 10
    print('The number of movements:', random_walk(window, circle3, probability_up, pixels_to_move))
    window.close_on_mouse_click()


def random_walk(window, circle, probability_up, pixels_to_move):
    """
    See the    RandomWalkExample.mp4    movie to see this function
    in action.  The movie shows THREE calls to this function:
       -- Blue circle  with probability_up = 0.4 and pixels_to_move =  1
       -- Green circle with probability_up = 0.5 and pixels_to_move = 10
       -- Red circle   with probability_up = 0.8 and pixels_to_move = 10

    Attaches the given rg.Circle to the given rg.RoseWindow.

    Then repeatedly:
      -- Flips a weighted coin
           -- using random.randrange(100)
           -- HEADS are (by definition) numbers
                strictly less than (probability_up * 100)
           -- TAILS otherwise
      -- Moves the given rg.Circle:
           -- If the coin is HEADS, moves the circle UP
                the given number of pixels.
           -- If the coin is TAILS, moves the circle DOWN
                the given number of pixels.
       -- Draws (renders) the given rg.Circle at its current position,
            pausing a small amount of time after each render
            (to make the animation look good).

    Stops when the circle's center is no longer within
    the given rg.RoseWindow.

    RETURNs the number of movements.

    Preconditions: the first argument is a rg.RoseWindow,
      the second argument is a rg.Circle,
      the third argument is a number between 0 and 1, and
      the fourth argument is a small positive number.
       :type window: rg.RoseWindow
       :type circle: rg.Circle
       :type probability_up: float
       :type pixels_to_move: int
    with   probability_up   between 0 and 1
    and   pixels_to_move   a small integer (typically less than 10).
    """
    # ------------------------------------------------------------------
    # TODO: 3b. Implement and test this function.
    # ------------------------------------------------------------------
    circle.attach_to(window)
    count = 0
    while True:
        n = random.randrange(100)
        if n < probability_up * 100:
            circle.move_by(0, -pixels_to_move)
            window.render(0.1)
        else:
            circle.move_by(0, pixels_to_move)
            window.render(0.1)
        if circle.center.y > window.height or circle.center.y < 0:
            break
        count = count + 1
    return count



# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
