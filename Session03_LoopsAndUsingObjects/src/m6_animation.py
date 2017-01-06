"""
This module lets you practice using objects,
including:
  -- CONSTRUCTING objects.
  -- Applying METHODS to them.
  -- ANIMATING them, using LOOPS to do so.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, their colleagues,
         and Yang Zhang.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # TODO: 2. Implement and test this function.
    your_animation()


def your_animation():
    """
    -- Constructs a window, i.e., a rg.RoseWindow.
    -- Draws anything that you want -- 1 or more objects.
    -- Makes at least 1 of those objects "animate", that is,
         makes it move in a way similar to that shown in m5e.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # TODO: 3. Implement and test this function.
    Window = rg.RoseWindow(500, 500)
    corner1 = rg.Point(0, 0)
    corner2 = rg.Point(20, 40)
    corner3 = rg.Point(500, 0)
    corner4 = rg.Point(480, 40)
    rectangle1 = rg.Rectangle(corner1, corner2)
    rectangle1.fill_color = 'pink'
    rectangle1.outline_color = 'pink'
    rectangle1.attach_to(Window)
    rectangle2 = rg.Rectangle(corner3, corner4)
    rectangle2.fill_color = 'purple'
    rectangle2.outline_color = 'purple'
    rectangle2.attach_to(Window)
    Window.render(1)
    for k in range(9):
        rectangle1.move_by(50, 50)
        rectangle2.move_by(-50, 50)
        Window.render(0.5)
    Window.continue_on_mouse_click()
    for k in range(450):
        rectangle1.move_by(-1, -1)
        rectangle2.move_by(1, -1)
        Window.render(0.001)
    Window.close_on_mouse_click()


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
