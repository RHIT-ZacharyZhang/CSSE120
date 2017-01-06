"""
PRACTICE Test 1, problem 3.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and PUT YOUR NAME HERE.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem3a()
    test_problem3b()


def test_problem3a():
    """ Tests the   problem3a   function. """
    # ------------------------------------------------------------------
    # TODO: 2a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least 3 tests, i.e., 3 calls to the function to test,
    #   of which at least 2 are on the SAME window.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   problem3a   function:')
    print('--------------------------------------------------')
    print('See the window(s) that pop up.')
    window1 = rg.RoseWindow (600, 600, 'one test')
    center1 = rg.Point(150, 150)
    center2 = rg.Point(400, 400)
    circle1 = rg.Circle(center1, 80)
    circle1.fill_color = 'yellow'
    circle2 = rg.Circle(center2, 50)
    circle2.fill_color = 'red'
    circle1.attach_to(window1)
    circle2.attach_to(window1)
    problem3a(window1, circle1)
    problem3a(window1, circle2)
    window1.render()
    window1.close_on_mouse_click()
    window2 = rg.RoseWindow(600, 600, 'third test')
    center3 = rg.Point(300, 300)
    circle3 = rg.Circle(center3, 50)
    circle3.fill_color = 'pink'
    circle3.attach_to(window2)
    problem3a(window2, circle3)
    window2.render()
    window2.close_on_mouse_click()

def problem3a(window, circle):
    """
    See   problem3a_picture.pdf   in this project for pictures that may
    help you better understand the following specification:

    1. Draws four rg.Circle's on the given rg.RoseWindow, as follows:

        a. The first rg.Circle is the given rg.Circle.

        b. The second rg.Circle is a new rg.Circle whose center
           is the same as the center of the given rg.Circle
           but whose radius is HALF the radius of the given rg.Circle.
           Also, this second rg.Circle has 'red' as its fill color.

        c. The third rg.Circle is a new rg.Circle that:
             -- has the same radius as the second (red) circle
             -- is immediately to the LEFT of, and barely touching,
                the second (red) circle, and
             -- has 'green' as its fill color.

        d. The fourth rg.Circle is a new rg.Circle that:
             -- has the same radius as the second (red) circle
             -- is immediately to the RIGHT of, and barely touching,
                the second (red) circle, and
             -- has 'blue' as its fill color.

    2. Waits for a mouse-click,
         with an appropriate message displayed to prompt the user.

    3. UN-draws all of the rg.Circle's just drawn,
       one at a time with a 1 second pause between each un-draw.

    Note: Drawing the circles in the order listed ensures that
    the new ones are visible on top of the (larger) first one drawn.

    Preconditions:
        :type window: rg.RoseWindow
        :type circle: rg.Circle
      and the circle fits inside the window.
    """
    # ------------------------------------------------------------------
    # TODO: 2b. Implement and test this function.
    # HINT: Do NOT attempt to use loops to solve this problem;
    # it is simpler (at this point of the course) if done WITHOUT loops.
    # ------------------------------------------------------------------
    center = circle.center
    radius = circle.radius
    X = center.x
    Y = center.y
    circle2 = rg.Circle(center, radius / 2)
    circle2.fill_color = 'red'
    circle2.attach_to(window)
    center3 = rg.Point(X - radius, Y)
    circle3 = rg.Circle(center3, radius / 2)
    circle3.fill_color = 'green'
    circle3.attach_to(window)
    center4 = rg.Point(X + radius, Y)
    circle4 = rg.Circle(center4, radius / 2)
    circle4.fill_color = 'blue'
    circle4.attach_to(window)
    window.render()
    window.continue_on_mouse_click('continue on mouse click', 150, 250)
    circle4.detach_from(window)
    window.render(2)
    circle3.detach_from(window)
    window.render(2)
    circle2.detach_from(window)
    window.render(2)
    circle.detach_from(window)


def test_problem3b():
    """ Tests the   problem3b  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem3b   function:')
    print('--------------------------------------------------')
    print('See the window(s) that pop up.')

    # ------------------------------------------------------------------
    # In the following test, your code should cause 4 dots
    # (i.e., small filled circles) where the user clicks.
    # The 5th click should close the window.
    # ------------------------------------------------------------------
    problem3b(4)

    # ------------------------------------------------------------------
    # In the following test, your code should place 7 dots
    # (i.e., small filled circles) where the user clicks.
    # The 8th click should close the window.
    # ------------------------------------------------------------------
    problem3b(7)


def problem3b(n):
    """
    See   problem3b_SampleRuns.mp4  in this project for a short video
    that may help you better understand the following specification:

    Creates a new rg.RoseWindow and allows the user to click the mouse
    in that window repreatedly.  Each time the user clicks,
    draws a small filled circle (a "dot") whose center is at
    the location of the mouse click.  After  n  mouse clicks
    (where n is the given argument) and hence  n  dots,
    the NEXT click causes the window to close.

    Preconditions: The given argument is a non-negative integer.
    """
    # ------------------------------------------------------------------
    # TODO: 3. Implement and this function this function.
    #
    # HINT: The   get_next_mouse_click   method from the  rg.RoseWindow
    #       class will be useful.  Note that it RETURNs a rg.Point that
    #       represents the coordinates of where the mouse is clicked.
    # ------------------------------------------------------------------
    window = rg.RoseWindow(500, 500, 'prblem3b')
    window.render()
    for k in range(n):
        center = window.get_next_mouse_click()
        circle = rg.Circle(center, 5)
        circle.fill_color = 'red'
        circle.attach_to(window)
        window.render()
    window.continue_on_mouse_click('continue on mouse click', 250, 200)
    window.close()


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
