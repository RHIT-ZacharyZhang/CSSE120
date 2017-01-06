"""
A simple program in which you can try out the DEBUGGER.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, Matt Boutell,
         and their colleagues. December 2013.
"""
# ----------------------------------------------------------------------
# Students:
#   Run this program   ** in the DEBUGGER **
#   by using the   ** "BUG" symbol **.
#
#   The "bug" is just to the left of the usual RUN (green arrow) symbol.
#
#   EXPERIMENT with the Debugger, by doing the following:
#      1. Set (and later remove) some breakpoints.
#      2. Run to the next breakpoint(s).
#      3. Try Step Into.
#      4. Try Step Over and Step Return.
#      5. Examine variables.  Expand some objects to see their fields.
#      6. Terminate, then restart the debugger.
#      7. Note the interaction between the debugger and the
#           graphics window, especially when the graphics window
#           is waiting for a mouse click.
#
#   When you are done experimenting, be sure to return to the PyDev120
#   perspective.  One way to do so is to select:
#       Window ~ Open Perspective ~ Other ~ PyDev120
#
#   There is nothing for you to turn in from this file,
#   but be sure to do the above so you have a feel for the Debugger.
# ----------------------------------------------------------------------

import math
import rosegraphics as rg


def main():
    """ Calls  draw_circles   to demonstrate it. """
    draw_circles(5, 'green')  # Draws 5 green circles
    draw_circles(3, 'blue')  # Draws 3 blue circles


def draw_circles(n, color):
    """
    Constructs a rg.GraphWin and draws n circles on it.
    Also prints some variables, just to serve as examples.
    """
    window = rg.RoseWindow(400, 200)
    x = 100
    y = 50
    radius = 25
    for k in range(n):
        sink = math.sin(k)
        k_to_kth = k ** k
        print(k, sink, k_to_kth, x, y)

        p = rg.Point(x, y)
        c = rg.Circle(p, radius)
        c.fill_color = color

        c.attach_to(window)
        p.attach_to(window)
        window.render(0.5)

        p.move_by(10, 10)
        window.render(0.5)

        x = x + (2 * radius)
        y = y + radius

    window.close_on_mouse_click()

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
