"""
This module lets you practice one form of the ACCUMULATOR pattern,
namely, the "IN GRAPHICS" form which features:
  -- DRAWING OBJECTS via ACCUMULATING positions and/or sizes,
     as in:   x = x + pixels

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Yang Zhang.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


# ----------------------------------------------------------------------
# Students: As you work each of these problems, ask yourself:
#   1. Do I need a loop?
#      If so, HOW MANY LOOPS?
#
#   2. Where I need a loop, what needs to happen:
#        -- BEFORE the loop?
#        -- IN the loop?
#        -- AFTER the loop?
# ----------------------------------------------------------------------
def main():
    """ Calls the   TEST   functions in this module. """
    test_draw_ellipses()


def test_draw_ellipses():
    """ Tests the   draw_ellipses   function. """
    # ------------------------------------------------------------------
    # TODO: 2a. Implement this function, using it to test the NEXT
    #   function. Write the two functions in whichever order you prefer.
    #   Include at least THREE tests (i.e., three DIFFERENT calls
    #   to draw_ovals, e.g. the calls in the attached pictures).
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   draw_ellipses   function:')
    print('See the graphics windows that pop up.')
    print('--------------------------------------------------')
    draw_ellipses(80, 35, 10)

    draw_ellipses(90, 35, 13)

    draw_ellipses(40, 55, 7)


def draw_ellipses(width, height, n):
    """
    See   ellipses.pdf   in this project for pictures that may
    help you better understand the following specification:

    Constructs a rg.RoseWindow and draws 3 SETS of rg.Ellipse objects
    on it, where each SET contains   n   rg.Ellipse objects
    (for the given parameter n).

    The parameters specify:
      -- the width and height, respectively, of each rg.Ellipse
           (all dimensions are in pixels)
      -- the number of rg.Ellipse objects to draw in EACH
           of the three sets.

    The first set of rg.Ellipse objects is a COLUMN on the LEFT side
    of the window, with each rg.Ellipse barely touching the previous one.
    These rg.Ellipse objects should be filled 'blue'.

    The second set of rg.Ellipse objects is a COLUMN on the RIGHT side
    of the window, with each rg.Ellipse barely touching the previous one.
    These rg.Ellipse objects should be filled 'lime green'.

    The third set of rg.Ellipse objects is a DIAGONAL from the
    UPPER-RIGHT side of the window toward the LOWER-LEFT side
    of the window, with each rg.Ellipse INTERSECTING the previous one,
    with nice "even" intersections.  (The exact amount of overlap is up
    to you.  One possibility is to move each oval by half of its width
    and half of its height. That's what I did in the attached pictures.)
    These rg.Ellipse objects should be filled 'red'.

    It is OK if the third set overlaps the first and/or second set
    somewhat.  The third set has to go 'down and to the left', but any
    reasonable choice for how much down and how much to the left is OK.

    Pauses after drawing, waiting for the user to click the mouse
    in the window, then closes the window.
    """
    # ------------------------------------------------------------------
    # TODO: 2b. Implement and test this function.
    # ------------------------------------------------------------------
    w = width
    h = height
    title = 'Ovals, with parameters: width = {}, height = {}, n = {}'.format(w, h, n)
    window = rg.RoseWindow(150 + 3 * w + w * (n - 1) / 2, n * h + 100, title)
    for k in range(n):
        c1 = rg.Point(50, 50 + k * h)
        c2 = rg.Point(50 + w, 50 + (k + 1) * h)
        o = rg.Ellipse(c1, c2)
        o.fill_color = 'blue'
        o.attach_to(window)
    for k in range(n):
        c1 = rg.Point(100 + w + w * (n - 1) / 2 - (n - 1 - k) * w / 2, 50 + (n - 1 - k) * h / 2)
        c2 = rg.Point(100 + 2 * w + w * (n - 1) / 2 - (n - 1 - k) * w / 2, 50 + (n - k + 1) * h / 2)
        o = rg.Ellipse(c1, c2)
        o.fill_color = 'red'
        o.attach_to(window)
    for k in range(n):
        c1 = rg.Point(100 + 2 * w + w * (n - 1) / 2, 50 + k * h)
        c2 = rg.Point(100 + 3 * w + w * (n - 1) / 2, 50 + (k + 1) * h)
        o = rg.Ellipse(c1, c2)
        o.fill_color = 'green'
        o.attach_to(window)
    window.render()
    window.close_on_mouse_click()


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
