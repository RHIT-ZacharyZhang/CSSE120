"""
This module demonstrates a simple   GRAPHICS   program.
You can (and should) modify it!

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         their colleagues and Yang Zhang.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# ----------------------------------------------------------------------
# TODO: 2. Play around with this file.  First, run it.
#          Try changing a number, whatever you feel comfortable with,
#          and then run the program again to see the effect.
#          Repeatedly:
#            -- Make a SMALL change, then
#            -- Run the program again, to see the effect of your change.
#
#          You'll probably get red error messages at some point.
#          If so, try briefly to fix them,
#          but fixing errors is what we will learn in the NEXT session.
#          So:
#             ***  IT IS PERFECTLY   OK   IF YOU MESS THIS FILE UP!  ***
#
#  *** YOU ARE ** not ** EXPECTED TO UNDERSTAND EVERYTHING IN HERE.
#  *** Just start getting used to EDITING and RUNNING a PROGRAM.
#
#  *** FULL CREDIT JUST FOR MAKING ** ANY ** CHANGES
#                           AND RUNNING THIS FILE!
# ----------------------------------------------------------------------

import rosegraphics as rg
import random


def main():
    """ Calls the   wiggle   function to demonstrate it. """
    wiggle()


def wiggle():
    """
    Draws circles that start at the center of a graphics window.
    Each circle moves randomly ("wiggles")
    until it hits an edge of the window.
    """
    width = 1000
    height = 1000
    window = rg.RoseWindow(width, height, 'Wiggles')

    center = rg.Point(width / 2, height / 2)
    radius = 200
    circle = rg.Circle(center, radius)
    circle.fill_color = 'green'
    circle.attach_to(window)

    for k in range(500):
        delta_x = random.randrange(-120, 180)  # between -12 and 17
        delta_y = random.randrange(-50, 130)  # between -5 and 12

        circle.move_by(delta_x, delta_y)
        window.render(5 / (k + 5))  # wait less and less time

        x = circle.center.x
        y = circle.center.y
        if x < 0 or x > width or y < 0 or y > height:
            circle = rg.Circle(center, radius)  # A new circle
            # filled with a random color:
            red = random.randrange(255)
            green = random.randrange(255)
            blue = random.randrange(255)
            color = rg.Color(red, green, blue)
            circle.fill_color = color

            circle.attach_to(window)

    window.render()
    window.close_on_mouse_click()

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
