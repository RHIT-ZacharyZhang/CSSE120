"""
This module lets you practice making the Create robot MOVE.
Create methods of interest include:

The   driveDirect   method STARTs the robot moving:
    robot.driveDirect(left_wheel_speed, right_wheel_speed)

where the units are  centimeters per second
and range from -50 cm/sec (backwards at full speed, approximately)
             to 50 cm/sec (forwards at full speed, approximately).

and the   stop   method STOPS the robot:
    robot.stop()

In between, you can do a time.sleep(...) to give the robot time to move.
So the "go by time" way to MOVE takes the form:
    robot.driveDirect(..., ...)    [or another movement method, like go]
    time.sleep(...)
    robot.stop()

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Dave Fisher, Matt Boutell, Curt Clifton,
         their colleagues, and Yang Zhang.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import new_create
import time

# ----------------------------------------------------------------------
# TODO: 2. READ the above explanation (in green) of how to make a robot
#       ** move for a specified time. **
#   When you have read it, asking questions as needed,
#   and you feel that you (mostly, at least) understand it, THEN:
#
#     ** Put  I GET IT  anywhere in this pink comment ** other than this line.
#
#   You can put that phrase on a new comment line (that begins
#   with a # or on an existing line, your choice.
# I GET IT!
# ----------------------------------------------------------------------


def main():
    """
    1. Constructs (and hence connects to) a Create robot.
         Puts the robot in full mode.
    2. Moves the robot FORWARD (in a straight line)
         at a reasonable speed for 3 seconds (and then STOPS the robot).
    3. Shuts down the robot.
    """
    # ------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    # ------------------------------------------------------------------
    port = 3
    robot = new_create.Create(port)
    robot.toFullMode()
    robot.driveDirect(10, 10)
    time.sleep(3)
    robot.stop()
    robot.shutdown()

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
