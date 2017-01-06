"""
Test 1, problem 3.

Authors: David Mutchler, Chandan Rupakheti, their colleagues,
         and PUT YOUR NAME HERE.  Summer 2015.
"""  # TODO: PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem3a()
    test_problem3b()
    test_problem3c()


def test_problem3a():
    """ Tests the   problem3a   function. """
    # ------------------------------------------------------------------
    # TODO: Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 3 tests, i.e., 3 calls to the function to test,
    #   of which at least 2 are on the SAME window.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   problem3a   function:')
    print('--------------------------------------------------')
    print('See the window(s) that pop up.')
    window1 = rg.RoseWindow(350, 250, 'Test_Problem3a_1')
    point1 = rg.Point(100, 100)
    point2 = rg.Point(150, 180)
    rectangle_left = rg.Rectangle(point1, point2)
    rectangle_left.attach_to(window1)
    point3 = rg.Point(250, 100)
    point4 = rg.Point(200, 180)
    rectangle_right = rg.Rectangle(point3, point4)
    rectangle_right.attach_to(window1)
    problem3a(window1, rectangle_left)
    problem3a(window1, rectangle_right)
    window1.render()
    window1.close_on_mouse_click()

    window2 = rg.RoseWindow(400, 200, 'Test_Problem3a_2')
    point1 = rg.Point(100, 100)
    point2 = rg.Point(200, 150)
    rectangle = rg.Rectangle(point1, point2)
    rectangle.attach_to(window2)
    problem3a(window2, rectangle)
    window2.render()
    window2.close_on_mouse_click()


def problem3a(window, rectangle):
    """
    See   problem3a_picture.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws the given rg.Rectangle on the given window.
    Also draws two lines forming an X inside the rg.Rectangle,
    and with the lines each having arrow-heads on them.
    See problem3a_picture.pdf for examples.

    Preconditions:
        :type window: rg.RoseWindow
        :type rectangle: rg.Rectangle
    """
    # ------------------------------------------------------------------
    # TODO: 2b. Implement and test this function.
    # NOTE: Partial credit is available
    #       if you do not get the arrow-heads to work.
    # ------------------------------------------------------------------
    p1 = rectangle.corner_1
    p2 = rectangle.corner_2
    p3 = rg.Point(p2.x, p1.y)
    p4 = rg.Point(p1.x, p2.y)
    l1 = rg.Line(p1, p2)
    l2 = rg.Line(p3, p4)
    l1.arrow = "both"
    l2.arrow = "both"
    l1.attach_to(window)
    l2.attach_to(window)


def test_problem3b():
    # ------------------------------------------------------------------
    # TODO: Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 2 tests
    #   (on the same window or separate windows, your choice).
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   problem3b   function:')
    print('--------------------------------------------------')
    print('See the window(s) that pop up.')
    window1 = rg.RoseWindow(900, 600, 'Test_problem3b_1')
    problem3b(window1, 8, rg.Point(50, 10), rg.Point(150, 80))
    window1.close_on_mouse_click()
    window2 = rg.RoseWindow(350, 500, 'Test_problem3b_2')
    problem3b(window2, 5, rg.Point(50, 50), rg.Point(100, 130))
    window2.close_on_mouse_click()

def problem3b(window, n, point1, point2):
    """
    See   problem3b_picture.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws n rectangles on the given window, as follows:
      -- Each rectangle has two lines inside it that form an X
           with arrow-heads (as in problem3a).
      -- The first (upper-left) rectangle has the two given points
           as opposite corners, where point1 is guaranteed to be
           above and to the left of point2.
      -- For each successive rectangle:
           -- It has the same width and height as the first rectangle.
           -- Its upper-left corner is at the lower-right corner
                of the preceding rectangle.

    Preconditions:
        :type window: rg.RoseWindow
        :type n: int
        :type point1: rg.Point
        :type point2: rg.Point
    and n is a non-negative integer
    and point1 is above and to the left of point2.
    """
    # ------------------------------------------------------------------
    # TODO: Implement and test this function.
    # IMPLEMENTATION REQUIREMENT:
    #     For full credit,
    #     this function must  ** CALL problem3a **  appropriately.
    # ------------------------------------------------------------------
    width = point2.x - point1.x
    height = point2.y - point1.y
    for k in range(n):
        point1_x = point1.x + width * k
        point1_y = point1.y + height * k
        point2_x = point2.x + width * k
        point2_y = point2.y + height * k
        new_point1 = rg.Point(point1_x, point1_y)
        new_point2 = rg.Point(point2_x, point2_y)
        rectangle = rg.Rectangle(new_point1, new_point2)
        rectangle.attach_to(window)
        problem3a(window, rectangle)
    window.render()

def test_problem3c():
    """ Tests the   problem3c   function. """
    # ------------------------------------------------------------------
    # TODO: Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 2 tests
    #   (on the same window or separate windows, your choice).
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   problem3c   function:')
    print('--------------------------------------------------')
    print('See the window(s) that pop up.')
    window1 = rg.RoseWindow(900, 600, 'Test_problem3c_1')
    problem3c(window1, 8, rg.Point(50, 10), rg.Point(150, 80))
    window1.close_on_mouse_click()
    window2 = rg.RoseWindow(350, 500, 'Test_problem3c_2')
    problem3c(window2, 5, rg.Point(50, 50), rg.Point(100, 130))
    window2.close_on_mouse_click()
    window3 = rg.RoseWindow(320, 220, 'Test_problem3c_3')
    problem3c(window3, 3, rg.Point(50, 10), rg.Point(150, 80))
    window3.close_on_mouse_click()


def problem3c(window, n, point1, point2):
    """
    See   problem3c_picture.pdf   in this project for pictures that may
    help you better understand the following specification:

    Same as the previous problem (i.e., problem3b) EXCEPT:
      -- The width and height of each successive rectangle is 75%
           of the width/height of the preceding rectangle.

    Preconditions:
        :type window: rg.RoseWindow
        :type n: int
        :type point1: rg.Point
        :type point2: rg.Point
    and n is a non-negative integer
    and point1 is above and to the left of point2.
    """
    # ------------------------------------------------------------------
    # TODO: Implement and test this function.
    # IMPLEMENTATION REQUIREMENT:
    #     For full credit,
    #     this function must  ** CALL problem3a **  appropriately.
    # NOTE: You may want to begin by copy-and-pasting your solution
    #       to  ** problem3b ** here.
    # NOTE: This problem is only  ** 4 points **  (of 100).
    #       Do NOT freak out if you cannot figure it out!
    # ------------------------------------------------------------------

    width = point2.x - point1.x
    height = point2.y - point1.y
    for k in range(n):
        rectangle = rg.Rectangle(point1, point2)
        rectangle.attach_to(window)
        problem3a(window, rectangle)
        window.render()
        width = 0.75 * width
        height = 0.75 * height
        point1 = point1.clone()
        point2 = point2.clone()
        point1.x = point2.x
        point1.y = point2.y
        point2.x = point2.x + width
        point2.y = point2.y + height
        point2 = rg.Point(point2.x, point2.y)

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
