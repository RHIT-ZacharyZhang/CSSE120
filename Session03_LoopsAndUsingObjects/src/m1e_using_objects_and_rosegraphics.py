"""
This module uses ROSEGRAPHICS to demonstrate:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES (aka FIELDS).

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, Matt Boutell,
         Mark Hays, and their colleagues. December 2013.
"""
# ----------------------------------------------------------------------
# Students: Read and run this program.
#
#           Also, WITH YOUR INSTRUCTOR, learn to use the DOT trick:
#               rg.           and rg.Circle().
#           to POP UP help from which you can learn how to use
#           objects of a class that you have never seen before.
#           (And the HOVER over a class or method to get its code.)
#
# There is nothing to turn in from this file.
# Just use it as an example to see and learn:
#   -- How to CONSTRUCT an object
#   -- How to APPLY A METHOD to an object (who_dot_doesWhat_withWhat)
#   -- How to ACCESS an INSTANCE VARIABLE of an object (who_dot_what)
#   -- the DOT andd HOVER pop-up tricks
# ----------------------------------------------------------------------

import rosegraphics as rg


def main():
    """
    Uses ROSEGRAPHICS to demonstrate:
      -- CONSTRUCTING objects,
      -- applying METHODS to them, and
      -- accessing their DATA via INSTANCE VARIABLES (aka FIELDS)
    """
    example1()
    example2()
    example3()
    example4()


def example1():
    """ Displays an empty window. """
    window = rg.RoseWindow(500, 300)
    window.close_on_mouse_click()


def example2():
    """ Displays two Point objects. """
    # ------------------------------------------------------------------
    # Construct the window in which objects will be drawn.
    # ------------------------------------------------------------------
    window = rg.RoseWindow()

    # ------------------------------------------------------------------
    # Construct some rg.Point objects.
    # Note: the y-axis goes DOWN from the TOP.
    # ------------------------------------------------------------------
    point1 = rg.Point(100, 150)
    point2 = rg.Point(200, 50)

    # ------------------------------------------------------------------
    # A RoseGraphics object is not associated with a window,
    # and hence are not drawn, until you ATTACH it to a window.
    # ------------------------------------------------------------------
    point1.attach_to(window)
    point2.attach_to(window)

    # ------------------------------------------------------------------
    # And they still are not DRAWN until you RENDER the window.
    # That will draw ALL the objects on the window.
    # This two-step approach is important for animation (see example 4).
    # ------------------------------------------------------------------
    window.render()

    window.close_on_mouse_click()


def example3():
    """ Displays a Circle and a Rectangle. """
    width = 700
    height = 400
    window = rg.RoseWindow(width, height)

    center_point = rg.Point(300, 100)
    point1 = rg.Point(100, 150)
    point2 = rg.Point(200, 50)

    # ------------------------------------------------------------------
    # Note: In this example, we did not ATTACH the Point objects
    # to a window because, in this example, we chose NOT to DRAW them.
    # We constructed them only to use them in constructing OTHER objects
    # (that ARE attached and drawn).
    # ------------------------------------------------------------------

    radius = 50
    circle = rg.Circle(center_point, radius)
    circle.attach_to(window)

    # ------------------------------------------------------------------
    # Construct a Rectange by giving it two opposite corners.
    # ------------------------------------------------------------------
    rectangle = rg.Rectangle(point1, point2)
    rectangle.attach_to(window)

    circle.fill_color = 'green'
    circle.fill_color = 'blue'

    # Finally, draw ALL the objects attached to this window.
    window.render()

    # More just to show that you can print objects -- see the Console.
    corner1 = rectangle.corner_1
    corner2 = rectangle.corner_2

    print(corner1, corner2)
    print(rectangle)

    window.close_on_mouse_click()


def example4():
    """ Animates a Circle. """
    window = rg.RoseWindow(900, 300)
    circle = rg.Circle(rg.Point(50, 100), 25)
    circle.fill_color = 'DarkOrange1'  # See the file NamedColors for colors
    circle.attach_to(window)

    window.render(1)  # Pauses for 1 second after drawing

    # ------------------------------------------------------------------
    # In the following loop, I chose to use  dummy  as the name for
    # the loop variable.  Any name would work, but  dummy  tells
    # Eclipse that we are not using the loop variable inside the loop.
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # The key ideas for ANIMATION are:
    #   1. You use a loop.
    #   2. You MOVE the object(s) inside the loop.
    #   3. You RENDER (draw the objects) after each movement.
    #   4. You tell RENDER to PAUSE briefly after each RENDER.
    # ------------------------------------------------------------------
    for dummy in range(7):
        circle.move_by(100, 20)
        window.render(0.5)  # Pauses for 0.5 seconds after drawing

    window.continue_on_mouse_click()

    for dummy in range(300):
        circle.move_by(-2, -0.3)
        window.render(0.01)

    window.close_on_mouse_click()

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
