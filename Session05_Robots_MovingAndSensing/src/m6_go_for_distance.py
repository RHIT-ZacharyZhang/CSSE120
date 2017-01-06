"""
This module lets you practice using Create MOVEMENT and SENSORS,
in particular the DISTANCE and ANGLE sensors.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Dave Fisher, Matt Boutell, Curt Clifton,
         their colleagues, and Yang Zhang.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import new_create
import time


def main():
    """ Tests the   go_by_time  function. """
    port = 3  # Use YOUR laptop's COM number
    robot = new_create.Create(port)
    robot.toFullMode()

    go_by_time(robot, 90, 30)  # Test 1.

    # ----------------------------------------------------------------------
    # The next statement is simply a way to make the program PAUSE until
    # the human presses the ENTER key.  That makes it easier for you to
    # measure how far the robot actually went, and to make sure that your
    #  go_by_time  function is working correctly.
    # ----------------------------------------------------------------------
    input("Press ENTER to continue")

    go_by_time(robot, 30, 15)  # Test 2.

    input("Press ENTER to continue")

    go_by_time(robot, 100, 50)  # Test 3, full speed.

    # ----------------------------------------------------------------------
    # Students, you are welcome to try additional tests if you wish.
    # Just be sure to put them BEFORE the   robot.shutdown()  that follows.
    # ----------------------------------------------------------------------

    robot.shutdown()


def go_by_time(robot, centimeters, centimeters_per_second):
    """
    Makes the given robot go straight FORWARD the given number of
    centimeters at the given speed (in centimeters per second), then stop.
    
    RETURNs the number of centimeters that the robot reports that it went.
    
    IMPLEMENTATION REQUIREMENT:  Use this algorithm
       (which we'll call the   "time"   algorithm):
         0. Compute the TIME the robot must move to achieve the
              requested DISTANCE at the requested SPEED.
         1. Start the robot moving at the requested speed.
         2. Sleep the computed time.
         3. Stop the robot.

    Preconditions: The arguments satisfy:
      :type robot: new_create.Create
      :type centimeters: float
      :type centimeters_per_second: float
          with centimeters and centimeters_per_second being positive.
    """
    # ------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    # NOTE: Use the REQUIRED ALGORITHM TO IMPLEMENT.
    #
    # HINT: *** First solve this problem BY HAND on an example! ***
    # ------------------------------------------------------------------
    assert(isinstance(robot, new_create.Create))
    assert(isinstance(centimeters, (int, float)))
    assert(isinstance(centimeters_per_second, (int, float)))
    assert(centimeters_per_second > 0)

    robot.driveDirect(centimeters_per_second, centimeters_per_second)
    seconds = centimeters / centimeters_per_second
    time.sleep(seconds)
    robot.stop()
    sensor1 = new_create.Sensors.distance
    reflectance1 = robot.getSensor(sensor1)
    return(reflectance1)

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
