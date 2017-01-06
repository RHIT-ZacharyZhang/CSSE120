"""
This module lets you practice  ** using objects **,
including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA
       -- via INSTANCE VARIABLES (aka FIELDS) and GETTERS.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Yang Zhang.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # ------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #
    #   ** IMPORTANT NOTE: **
    #   You will see "implement and test" a lot.
    #   Here is what they mean for us at this point of the course:
    #
    #     -- IMPLEMENT:
    #          1. Read the green doc-string that precedes the TODO.
    #             It says what the function should do.
    #          2. Write code below the pink TODO that makes the function
    #             do what the green doc-string said it should do.
    #
    #     -- TEST:
    #          1. Run the function after implementing it.
    #          2. If the function behaves as hoped for, you are done
    #             with the exercise.  If not, fix your implementation
    #             and re-test.
    #
    #   The  main  function says:
    #      "Calls the other functions to demonstrate and/or test them."
    #   So, implementing this  main  function simply means
    #   calling the other functions in this file (that you implement).
    #
    #   Later in the course, we will discuss and you will use
    #   more elaborate processes for implement/test.
    # ------------------------------------------------------------------
    two_circles()
    circle_and_rectangle()
    lines()
    olympic_rings()


def two_circles():
    """
    -- Constructs a window, i.e., a rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window such that:
         -- They fit in the window and are easily visible.
         -- They have different radii.
         -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #       ANY two rg.Circle objects that meet the criteria are fine.
    #
    # HINT:
    #   See the   NamedColors.pdf   file included in this project
    #   for a list of named colors that you can use as strings
    #   in    outline_color    and    fill_color.
    #   FYI, that list came from   http://wiki.tcl.tk/37701
    #   It shows what each color looks like.
    # ------------------------------------------------------------------
    Window = rg.RoseWindow(500, 500)
    center1 = rg.Point(150, 150)
    center2 = rg.Point(300, 300)
    circle1 = rg.Circle(center1, 100)
    circle2 = rg.Circle(center2, 50)
    circle1.fill_color = 'red'
    circle1.attach_to(Window)
    circle2.attach_to(Window)
    Window.render()
    Window.close_on_mouse_click()


def circle_and_rectangle():
    """
    -- Constructs a window, i.e., a rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
          -- The rg.Rectangle is outlined with 'red'.
    -- Prints (on the console) the following data associated
         with your rg.Rectangle:
          -- Its outline thickness.
          -- Its outline color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.

       Here is an example of the output on the console,
       for one particular rectangle:
           1
           black
           Point(225.0, 150.0)
           225.0
           150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    #            -- ANY objects that meet the criteria are fine.
    # HINT:    Use the DOT TRICK to figure out how to
    #          construct a Rectangle and do stuff with it.
    # ------------------------------------------------------------------
    window = rg.RoseWindow(600, 300)

    circle = rg.Circle(rg.Point(150, 80), 30)
    circle.fill_color = 'blue'
    circle.attach_to(window)

    corner1 = rg.Point(300, 200)
    corner2 = rg.Point(200, 50)
    rectangle = rg.Rectangle(corner1, corner2)
    rectangle.outline_color = 'red'
    rectangle.outline_thickness = 2
    rectangle.attach_to(window)

    window.render()

    x1 = rectangle.corner_1.x
    x2 = rectangle.corner_2.x
    y1 = rectangle.corner_1.y
    y2 = rectangle.corner_2.y

    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    center = rg.Point(x, y)

    print(rectangle.outline_thickness)
    print(rectangle.outline_color)
    print(center)
    print(x)
    print(y)

    window.close_on_mouse_click()


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5,150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # TODO: 5. Implement and test this function.
    window = rg.RoseWindow(700, 400)

    line1 = rg.Line(rg.Point(100, 200), rg.Point(400, 300))
    line2 = rg.Line(rg.Point(500, 200), rg.Point(250, 400))
    line1.thickness = 20
    line1.attach_to(window)
    line2.attach_to(window)
    window.render()
    center = line1.get_midpoint()
    x = center.x
    y = center.y
    print(center)
    print(x)
    print(y)
    window.close_on_mouse_click()

def olympic_rings():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window the Olympic rings,
        colored per the (approximate) Olympic colors.
          ** See the  m2_olympic_rings.pdf  file in this project. **
    -- Waits for the user to press the mouse, then closes the window.

    This problem is taken from page 83 of Python for Everyone,
      by Horstmann and Necaise.
    """
    # ------------------------------------------------------------------
    # TODO: 6. Implement and test this function.
    # HINTs:
    #   -- See the   NamedColors.pdf   file included in this project
    #        for a list of named colors that you can use as strings
    #        in    outline_color    and    fill_color.
    #
    #   -- FYI, that list came from   http://wiki.tcl.tk/37701
    #        It shows what each color looks like.
    #
    #   -- Work an example BY HAND to figure out the GEOMETRY
    #        required for a solution to this problem.
    #
    #   -- Do not attempt to make the COLORS just right,
    #        but DO get the geometry just right.
    #        Ask for help as needed.
    # ------------------------------------------------------------------
    window = rg.RoseWindow(800, 800)
    circle1 = rg.Circle(rg.Point(200, 200), 100)
    circle2 = rg.Circle(rg.Point(420, 200), 100)
    circle3 = rg.Circle(rg.Point(640, 200), 100)
    circle4 = rg.Circle(rg.Point(300, 300), 100)
    circle5 = rg.Circle(rg.Point(530, 300), 100)
    circle1.outline_thickness = 20
    circle2.outline_thickness = 20
    circle3.outline_thickness = 20
    circle4.outline_thickness = 20
    circle5.outline_thickness = 20
    circle1.outline_color = 'RoyalBlue1'
    circle2.outline_color = 'black'
    circle3.outline_color = 'red'
    circle4.outline_color = 'gold'
    circle5.outline_color = 'green4'
    circle1.attach_to(window)
    circle2.attach_to(window)
    circle3.attach_to(window)
    circle4.attach_to(window)
    circle5.attach_to(window)
    window.render()
    window.close_on_mouse_click()

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
