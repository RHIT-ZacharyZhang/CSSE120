"""
This module demonstrates:
  -- Simple ANIMATION in RoseGraphics, using LOOPS to do so.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Delvin Defoe, Curt Clifton, Matt Boutell,
         and their colleagues. December 2013.
"""
# ----------------------------------------------------------------------
# Students: Read and run this program.  There is nothing else
#           for you to do in here.  Just use it as an example.
# ----------------------------------------------------------------------

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    simple_animation()


def simple_animation():
    """ Animates a Circle. """
    # ------------------------------------------------------------------
    # Students: This is the same as  example4  from m1e,
    # except I removed some of the comments here.
    # See  example4  in m1e if you want to see all the comments.
    # ------------------------------------------------------------------
    window = rg.RoseWindow(900, 300)
    circle = rg.Circle(rg.Point(50, 100), 25)
    circle.fill_color = 'DarkOrange1'
    circle.attach_to(window)

    window.render(1)  # Pauses for 1 second after drawing

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
