"""
This module is a VERY BASIC introduction to the Create robot.
We'll use it to:
  -- Help you figure out the mechanics of establishing and using
       a Bluetooth connection to the robot.
  -- Serve as a basic example.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Dave Fisher, Matt Boutell, Curt Clifton,
         their colleagues, and Yang Zhang.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import new_create
import time


def main():
    # ------------------------------------------------------------------
    # Set the port to whatever COM number YOUR laptop is using
    # for its connection to the BAM on the Create robot.
    # Then connect to a Create via that port.
    # Put the robot in "full mode" so that sensors don't stop the robot.
    # ------------------------------------------------------------------
    port = 3  # Use YOUR laptop's COM number
    robot = new_create.Create(port)
    robot.toFullMode()

    # ------------------------------------------------------------------
    # Start moving:
    #   -- left wheel at 30 centimeters per second forwards,
    #   -- right wheel at 25 centimeters per second forwards.
    # (so forward but veering to the right).
    # Sleep for 2 seconds (while doing the above motion),
    # then stop.
    # ------------------------------------------------------------------
    robot.driveDirect(30, 25)
    time.sleep(4.0)
    robot.stop()

    # ------------------------------------------------------------------
    # All sensor data is obtained by the   getSensor   method.
    # The  Sensors  class has constants for all sensor names available.
    # ------------------------------------------------------------------
    sensor = new_create.Sensors.cliff_front_left_signal
    reflectance = robot.getSensor(sensor)
    print('Current value of the front left cliff sensor:', reflectance)

    # ------------------------------------------------------------------
    # ALWAYS execute the following before your program ends.  Otherwise,
    # your robot may be left in a funky state and on the NEXT run,
    # it might fail to connect or it might run incorrectly.
    # ------------------------------------------------------------------
    robot.shutdown()

# ----------------------------------------------------------------------
# TODO 2: The above is (almost) the same program as in m1_first_robot.py.
#   In the  m1  exercise, you used the DOT trick on a  robot  constructed
#   via the   new_create  library.  Now, use the DOT trick on the
#     new_create.Sensors  class, to see a list of ALL the sensor names
#   that you can use as the argument to a  getSensor(...)  method call.
#   That is, type:
#             new_create.Sensors.
#  (note the DOT) and pause.  Scroll through what it shows.
#  The items it shows are  data attributes  of the  Sensors  class
#  in the  new_create  module.  You can use any of them as the
#  argument to the robot's  getSensor  method.
#
#   When you have done the above, asking questions as needed,
#   and you feel that you understand how to find the name
#   for ANY sensor that a Create robot can access,
#
#     ** Put  I GET IT  anywhere in this pink comment ** other than this line.
#
#   You can put that phrase on a new comment line (that begins
#   with a # or on an existing line, your choice.
# I GET IT
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# TODO 3: RUN this program (again) (with your robot if you can
#         or the simulator if your robot is not working for you today).
#
#   This time, examine what gets PRINTED in the CONSOLE.
#   You will see that the  new_create
#   When you have read it, asking questions as needed,
#   and you feel that you (mostly, at least) understand it, THEN:
#
#     ** Put  I GET IT  anywhere in this pink comment ** other than this line.
#
#   You can put that phrase on a new comment line (that begins
#   with a # or on an existing line, your choice.
# I GET IT
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
