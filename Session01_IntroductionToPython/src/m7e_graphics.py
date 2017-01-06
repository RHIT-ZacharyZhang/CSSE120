"""
This module is an example of a simple   GRAPHICS   program.
It demonstrates:
  -- DEFINING functions:
       -- main
       -- wiggle
  -- How    main   CALLS the    wiggle    function.
  -- Giving values to VARIABLES using the ASSIGNMENT
        operator = (read it as "gets")
  -- CONSTRUCTING OBJECTS (GraphWin, Point, Circle, Text)
  -- USING OBJECTS, as in:    circle.move(delta_x, delta_y)
  -- Running a LOOP a fixed number of times (a "counting" loop),
         using a FOR statement and a RANGE expression.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Mark Hays, and their colleagues.  December 2014.
"""
# ----------------------------------------------------------------------
# Students: Read and run this program.  There is nothing else
#           for you to do in here.  Just use it as an example to see:
#   Cool graphics!  (We'll study this example in detail in Session 3.)
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
    width = 400
    height = 300
    window = rg.RoseWindow(width, height, 'Wiggles')

    center = rg.Point(width / 2, height / 2)
    radius = 20
    circle = rg.Circle(center, radius)
    circle.fill_color = 'green'
    circle.attach_to(window)

    for k in range(500):
        delta_x = random.randrange(-12, 13)  # between -12 and 12
        delta_y = random.randrange(-5, 13)  # between -5 and 12

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
