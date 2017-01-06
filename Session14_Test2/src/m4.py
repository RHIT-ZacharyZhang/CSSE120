"""
Test 2, problem 4.

Authors: David Mutchler, Chandan Rupakheti, their colleagues,
         and Yang Zhang.  April 2014.
"""  # DONE: PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem4a()
    test_problem4b()


def test_problem4a():
    """ Tests the   problem4a   function. """
    # -------------------------------------------------------------------
    # TODO:  READ and use the following tests that we have supplied
    #        for you.  The tests produce the same pictures shown in
    #            problem4a_picture.pdf.
    # -------------------------------------------------------------------
    window1 = rg.RoseWindow(600, 300, 'Problem 4a, tests 1 and 2')

    # Test 1:
    center = rg.Point(50, 50)
    circle = rg.Circle(center, 20)

    corner1 = rg.Point(150, 120)
    corner2 = rg.Point(210, 200)
    rectangle = rg.Rectangle(corner1, corner2)

    problem4a(window1, circle, rectangle, 'blue', 'red')

    # Test 2:
    center = rg.Point(350, 200)
    circle = rg.Circle(center, 60)

    corner1 = rg.Point(400, 80)
    corner2 = rg.Point(500, 140)
    rectangle = rg.Rectangle(corner1, corner2)

    problem4a(window1, circle, rectangle, 'yellow', 'green')

    window1.close_on_mouse_click()

    # Test 3:
    window2 = rg.RoseWindow(300, 200, 'problem 4a, test 3')

    center = rg.Point(250, 80)
    circle = rg.Circle(center, 25)

    corner1 = rg.Point(50, 30)
    corner2 = rg.Point(150, 130)
    rectangle = rg.Rectangle(corner1, corner2)

    problem4a(window2, circle, rectangle, 'cyan', 'black')

    window2.close_on_mouse_click()


def problem4a(window, circle, rectangle, circle_color, rectangle_color):
    """
    See   problem4a_picture.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws a circle, a rectangle and 4 lines as follows:
      -- All the shapes should have their width (i.e., line thickness)
           set to 3 (instead of the default 1).
      -- The circle should be the given circle,
           but with its FILL color set to the given  circle_color.
      -- The rectangle should be the given rectangle,
           but with its OUTLINE color set to the given   rectangle_color.
      -- The 4 lines each have one end at the center of the given circle
           and the other end at a corner of the rectangle.
           (The rectangle has 4 corners; one line to each.)
           The lines should be drawn AFTER drawing the circle and rectangle
           so that the lines are on TOP of the circle and rectangle.

    See   problem4a_picture.pdf   for examples.

    Preconditions:
      :type window: rg.RoseWindow
      :type circle: rg.Circle
      :type rectangle: rg.Rectangle
    and the other two arguments are colors appropriate for rosegraphics.
    """
    # -------------------------------------------------------------------
    # TODO: Implement and test this function.
    # NOTE: Partial credit is available if you can draw
    #       only parts of what is asked for.
    # -------------------------------------------------------------------
    circle.fill_color = circle_color
    circle.outline_thickness = 3
    rectangle.outline_color = rectangle_color
    rectangle.outline_thickness = 3
    circle.attach_to(window)
    rectangle.attach_to(window)
    circle_center = circle.center
    corner1 = rectangle.corner_1
    corner2 = rectangle.corner_2
    corner3 = rg.Point(corner2.x , corner1.y)
    corner4 = rg.Point(corner1.x , corner2.y)
    new_list = [corner1,corner2, corner3, corner4]
    for k in new_list:
        line = rg.Line(circle_center,k)
        line.attach_to(window)
        line.thickness = 3
    window.render()
        


def test_problem4b():
    """ Tests the   problem4b   function. """
    # -------------------------------------------------------------------
    # TODO:  READ and use the following tests that we have supplied
    #        for you.  The tests produce the same pictures shown in
    #            problem4b_picture.pdf.
    # -------------------------------------------------------------------

    # Test 1:
    window1 = rg.RoseWindow(600, 650, 'Problem 4b, tests 1 and 2')
    point1 = rg.Point(250, 80)
    rectangle1 = rg.Rectangle(rg.Point(50, 30), rg.Point(100, 60))
    colors1 = ['blue', 'red', 'green', 'white', 'cyan', 'yellow',
               'brown', 'pink']

    problem4b(window1, 7, point1, rectangle1, colors1)

    # Test 2 (on same window as Test 1):
    point2 = rg.Point(400, 80)
    rectangle2 = rg.Rectangle(rg.Point(500, 100), rg.Point(580, 150))
    colors2 = ['blue', 'red', 'green']

    problem4b(window1, 3, point2, rectangle2, colors2)

    window1.close_on_mouse_click()

    # Test 3:
    window2 = rg.RoseWindow(500, 650, 'Problem 4b, tests 3 and 4')
    point3 = rg.Point(40, 40)
    rectangle3 = rg.Rectangle(rg.Point(100, 20), rg.Point(140, 30))
    colors2 = ['blue', 'red', 'green']

    problem4b(window2, 8, point3, rectangle3, colors2)

    # Test 4 (on same window as Test 3):
    point4 = rg.Point(200, 80)
    rectangle4 = rg.Rectangle(rg.Point(400, 100), rg.Point(480, 150))

    problem4b(window2, 6, point4, rectangle4, colors2)

    window2.close_on_mouse_click()


def problem4b(window, n, point, rectangle, colors):
    """
    See   problem4b_picture.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws  n  "things" as follows:
      -- Each "thing" consists of a circle, a rectangle, and 4 lines,
           as in problem3a.
      -- The first "thing" has:
           -- Its rectangle is the given rectangle.
           -- Its circle is centered at the given point.
           -- The radius of the circle is half of the width of the rectangle.
           -- Its 4 lines go from the center of the circle to the 4 corners
                of the rectangle, as in problem3a.
           -- The fill color of the circle is the first (beginning) color
                in the given list of colors.
           -- The outline color of the rectangle is the second color
                in the given list of colors.
      -- Each succeeding "thing" has the same size and relationships
           as the first thing, but is shifted 70 pixels down
           from the previous "thing".
      -- Also, the circles have fill colors per the given list of colors,
           one after the other, starting at the first (beginning) color,
           wrapping as necessary.
      -- Also, the rectangles have outline colors per the given
           list of colors, one after the other, wrapping as necessary,
           but starting at the second color.

    See   problem4b_picture.pdf   for examples.

    Preconditions:
      :type window: rg.RoseWindow
      :type n: int
      :type point: rg.Point
      :type rectangle: rg.Rectangle
    and the last argument is a list of colors
    appropriate for rosegraphics.
    Also, the second argument  n  is nonnegative.
    """
    # -------------------------------------------------------------------
    # TODO: Implement and test this function.  Partial credit
    #       is available if you get only part of this to work.
    #
    # IMPLEMENTATION REQUIREMENT:
    #     For full credit,
    #     this function must  ** CALL problem4a **  appropriately.
    #
    # NOTE: If your program works correctly EXCEPT that it crashes
    #       on the second test window for this problem,
    #       you may still receive most of the credit on this problem.
    # -------------------------------------------------------------------
    blank = 70
    width = rectangle.corner_2.x - rectangle.corner_1.x
    circle_color = colors
    rectangle_color = colors
    for k in range(n):
        center = rg.Point(point.x,point.y + blank * k)
        circle1 = rg.Circle(center,width/2)
        rectangle1 = rg.Rectangle(rg.Point(rectangle.corner_1.x,rectangle.corner_1.y - blank * k),rg.Point(rectangle.corner_2.x,rectangle.corner_2.y - blank * k))
    problem4a(window, circle1, rectangle1, circle_color, rectangle_color)
# -----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# -----------------------------------------------------------------------
if __name__ == '__main__':
    main()
