"""
PRACTICE Test 2, problem 4.

Authors: David Mutchler, Chandan Rupakheti, Matt Boutell, Dave Fisher,
         Claude Anderson, and Yang Zhang.  September 2013.
"""  # TODO: PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg
import simple_testing as st


def main():
    """ Calls the   TEST   functions in this module. """
    test_problem4()


# ----------------------------------------------------------------------
# Students: Some of the testing code below uses SimpleTestCase objects,
#           from the imported   simple_testing (st)   module.
# ----------------------------------------------------------------------

def test_problem4():
    """ Tests the   problem4   function. """
    # ------------------------------------------------------------------
    # READ and use the following tests that we have supplied for you.
    # See   problem4_pictures.pdf   for what these tests display.
    # ------------------------------------------------------------------

    window1 = rg.RoseWindow(325, 300, 'Test 1 for draw_lines')

    points1 = [rg.Point(100, 100),
               rg.Point(110, 200),
               rg.Point(50, 250),
               rg.Point(90, 90)]

    colors1 = ('cyan', 'green', 'magenta')

    correct_lines1 = [rg.Line(rg.Point(100, 100), rg.Point(110, 200)),
                      rg.Line(rg.Point(110, 200), rg.Point(50, 250)),
                      rg.Line(rg.Point(50, 250), rg.Point(90, 90))]
    correct_lines1[0].color = "cyan"
    correct_lines1[0].thickness = 1
    correct_lines1[1].color = "green"
    correct_lines1[1].thickness = 3
    correct_lines1[2].color = "magenta"
    correct_lines1[2].thickness = 5
    test1 = st.SimpleTestCase(problem4,
                              [points1, window1, colors1],
                              correct_lines1)

    st.SimpleTestCase.run_tests('problem4', [test1])
    window1.render()
    window1.close_on_mouse_click()

    window2 = rg.RoseWindow(500, 300, 'Test 2 for draw_lines')

    points2 = [rg.Point(116, 189),
               rg.Point(492, 192),
               rg.Point(64, 98),
               rg.Point(360, 22),
               rg.Point(43, 70),
               rg.Point(126, 259),
               rg.Point(107, 205),
               rg.Point(328, 15),
               rg.Point(235, 249),
               rg.Point(232, 199)]

    colors2 = ('red', 'black', 'blue', 'green')

    correct_lines2 = [rg.Line(rg.Point(116, 189), rg.Point(492, 192)),
                      rg.Line(rg.Point(492, 192), rg.Point(64, 98)),
                      rg.Line(rg.Point(64, 98), rg.Point(360, 22)),
                      rg.Line(rg.Point(360, 22), rg.Point(43, 70)),
                      rg.Line(rg.Point(43, 70), rg.Point(126, 259)),
                      rg.Line(rg.Point(126, 259), rg.Point(107, 205)),
                      rg.Line(rg.Point(107, 205), rg.Point(328, 15)),
                      rg.Line(rg.Point(328, 15), rg.Point(235, 249)),
                      rg.Line(rg.Point(235, 249), rg.Point(232, 199))]
    correct_lines2[0].color = "red"
    correct_lines2[0].thickness = 1
    correct_lines2[1].color = "black"
    correct_lines2[1].thickness = 3
    correct_lines2[2].color = "blue"
    correct_lines2[2].thickness = 5
    correct_lines2[3].color = "green"
    correct_lines2[3].thickness = 7
    correct_lines2[4].color = "red"
    correct_lines2[4].thickness = 9
    correct_lines2[5].color = "black"
    correct_lines2[5].thickness = 11
    correct_lines2[6].color = "blue"
    correct_lines2[6].thickness = 13
    correct_lines2[7].color = "green"
    correct_lines2[7].thickness = 15
    correct_lines2[8].color = "red"
    correct_lines2[8].thickness = 17
    test2 = st.SimpleTestCase(problem4,
                              [points2, window2, colors2],
                              correct_lines2)

    st.SimpleTestCase.run_tests('problem4', [test2])
    window2.render()
    window2.close_on_mouse_click()


def problem4(points, window, colors):
    """
    See   problem4_pictures.pdf   in this project for pictures
    that may help you better understand the following specification:

    For the given list of rg.Point's, constructs and draws rg.Line's
    on the given rg.RoseWindow.  Each line goes from one point
    in the given list to the next point in the given list.
    The last point in the list does NOT go anywhere.

    Furthermore, the first line drawn has width 1, then next line drawn
    has width 3, the one after that has width 5, and so forth.

    Also, the first line is drawn with the first color in the given
    sequence of colors, the next line with the next color in that
    sequence, and so forth.  If the list of colors is exhausted,
    the colors to be used 'wrap' in the list: for example,
    if the colors are ['red', 'white', 'blue'] and there are 7 lines,
    then the lines are drawn using:
      'red'  'white'  'blue'  'red'  'white'  'blue'  'red'
    in that order.

    RETURNs a list containing the constructed lines.

    Preconditions:
      :type: points: (list, tuple)
      :type window: rg.RoseWindow
    and the points sequence contains one or more rg.Point objects.
    """
    # ------------------------------------------------------------------
    # TODO: Implement and test this function.
    # ------------------------------------------------------------------
    n = len(points) - 1
    colors_1 = []
    for k in range(n):
        color = colors[k % len(colors)]
        colors_1 += [color]
    lines = []
    for k in range(n):
        point1 = points[k]
        point2 = points[k + 1]
        line = rg.Line(point1, point2)
        line.color = colors_1[k % len(colors)]
        w = 2 * k + 1
        line.thickness = w
        line.attach_to(window)
        lines += [line]
    window.render()
    return lines

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
