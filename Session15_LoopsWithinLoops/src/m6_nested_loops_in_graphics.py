"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Yang Zhang.  February 2014.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE..

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate them. """
    nested_loops_in_graphics_example()
    test_draw_wall_on_right()

def nested_loops_in_graphics_example():
    """
    Demonstrates nested loops in a TWO-DIMENSIONAL GRAPHICS example.
    """
    width = 800
    height = 600
    title = 'Rectangles and Triangles of Circles'
    window = rg.RoseWindow(width, height, title)

    starting_point = rg.Point(50, 50)

    window.continue_on_mouse_click()

    # ------------------------------------------------------------------
    # First set of circles
    # ------------------------------------------------------------------
    radius = 20
    starting_circle = rg.Circle(starting_point, radius)

    rectangle_of_circles(window, starting_circle, 4, 12)
    window.continue_on_mouse_click()

    # ------------------------------------------------------------------
    # Second set of circles
    # ------------------------------------------------------------------
    starting_circle.move_by(180, 400)

    rectangle_of_circles(window, starting_circle, 14, 2)
    window.continue_on_mouse_click()

    # ------------------------------------------------------------------
    # Third and last set of circles
    # ------------------------------------------------------------------
    starting_circle.move_by(200, -400)

    triangle_of_circles(window, starting_circle, 8)
    window.close_on_mouse_click()


def rectangle_of_circles(window, circle, m, n):
    """
    Draws an m x n rectangle of circles (i.e. m columns and n rows)
    on the given rg.RoseWindow.  The given rg.Circle specifies:
      - The position of the upper-left circle drawn and also
      - The radius that all the circles have.
    After drawing each circle, pauses briefly (0.1 second).

    Preconditions:
      :type window: rg.RoseWindow
      :type circle: rg.Circle
      :type m: int
      :type n: int
    and m and n are small, positive integers.
    """
    # TODO: 2. Implement this with your professor in class




def triangle_of_circles(window, circle, n):
    """
    Draws an n x n right-triangle of circles
    (1 circle in the top row, 2 in the next row, etc., until n rows)
    on the given rg.RoseWindow.  The given rg.Circle specifies:
      - The position of the upper-left circle drawn and also
      - The radius that all the circles have.
    After drawing each circle, pauses briefly (0.1 second).

    Preconditions:
      :type window: rg.RoseWindow
      :type circle: rg.Circle
      :type m: int
      :type n: int
    and m is a small, positive integer.
    """
    # ------------------------------------------------------------------
    # NOTE: The solution below is IDENTICAL to the rectangle_of_circles
    #       solution except that the INNER loop has  j+1  instead of m.
    # Make sure you understand why this works!
    # ------------------------------------------------------------------
    # TODO: 3. Implement this with your professor in class


def test_draw_wall_on_right():
    """ Tests the    draw_wall_on_right    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Wall on the right, Tests 1 and 2')

    rectangle1 = rg.Rectangle(rg.Point(250, 30), rg.Point(250 + 30, 30 + 20))
    draw_wall_on_right(rectangle1, 8, window)

    rectangle2 = rg.Rectangle(rg.Point(470, 40), rg.Point(470 + 50, 40 + 50))
    draw_wall_on_right(rectangle2, 4, window)

    window.close_on_mouse_click()


def draw_wall_on_right(rectangle, n, window):
    """
    See   Walls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an n x n RIGHT-justified triangle of rectangles
    (1 rectangle in the top row, 2 in the next row, etc., until n rows)
    on the given rg.RoseWindow.  The given rg.Rectangle specifies:
      - The position of the upper-right rectangle drawn and also
      - The width and height that all the rectangles have.
    After drawing each rectangle, pauses briefly (0.1 second).

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is a small, positive integer.
    """
    # TODO: 4. Implement and test this function.
    #     The testing code is already written for you (above).
    x_1 = rectangle.corner_1.x
    y1 = rectangle.corner_1.y
    x_2 = rectangle.corner_2.x
    y2 = rectangle.corner_2.y
    a = x_2 - x_1
    b = y2 - y1

    for k in range(n):
        for i in range(k + 1):
            x1 = x_1 - i * a
            x2 = x_2 - i * a
            rectangle = rg.Rectangle(rg.Point(x1, y1), rg.Point(x2, y2))
            rectangle.attach_to(window)
            window.render(0.1)
        y1 = y1 + b
        y2 = y2 + b
# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
