"""
This module lets you practice using Create SENSORS,
in particular the DISTANCE and ANGLE sensors.

The    getSensor   method is used for ALL sensor accesses, like this:
   sensor_value = robot.getSensor(...)

where the argument is a constant that indicates the sensor whose value
is sought:
  -- The   new_create.Sensors.distance   data attribute indicates
     LINEAR distance traveled 
        ** SINCE you last asked for that sensor reading. **
  -- The   new_create.Sensors.angle   data attribute indicates
     ANGULAR distance traveled
        ** SINCE you last asked for that sensor reading. **

The former is in MILLIMETERS (NOT centimeters).
The latter is in DEGREES.
Each is returned as an INTEGER.

So, to obtain linear distance traveled, the usual approach is:
  1. Use the  getSensor  method with the  new_create.Sensors.distance
     to get a DISTANCE
     sensor reading (but ignoring the value of that reading).
  2. Make the robot move, e.g. by:
       a. robot.driveDirect(..., ...)
       b. time.sleep(...)
       c. robot.stop()
  3. Use getSensor(Sensors.distance) to get ANOTHER DISTANCE sensor
       reading.  This NEW reading is the distance the robot traveled.

Authors: David Mutchler, Amanda Stouder, Chandan Rupakheti, Katie Dion,
         Claude Anderson, Dave Fisher, Matt Boutell, Curt Clifton,
         their colleagues, and Yang Zhang.  December 2013.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import new_create
import time


# ----------------------------------------------------------------------
# TODO: 2. READ the above explanation (in green) of how to find the
#       ** distance a robot thinks that it moved. **
#   When you have read it, asking questions as needed,
#   and you feel that you (mostly, at least) understand it, THEN:
#
#     ** Put  I GET IT  anywhere in this pink comment ** other than this line.
#
#   You can put that phrase on a new comment line (that begins
#   with a # or on an existing line, your choice.
# ----------------------------------------------------------------------

def main():
    """
    1. Prompts for and inputs two speeds (one for each wheel)
         and the number of seconds to move at that speed.
         (The user should enter speeds that are between -50 and 50
         and seconds between 0.5 and 5.0 or so).

         For example, where the user's input is shown to the right
         of the colons:
           Enter the left wheel speed: -25
           Enter the right wheel speed:  18
           Enter the number of seconds to move at that speed: 1.2

    2. Constructs (and hence connects to) a Create robot.
         Puts the robot in full mode.

    3. Repeats the following 3 times:
       a. Moves the robot at the requested wheel speeds for the
          requested number of seconds (and then stops the robot).
       c. Prints the LINEAR distance traveled.
       d. Prints the ANGULAR distance traveled.
       e. Waits for the user to press the ENTER key.
            Implement this by using this statement:
               input('Press the Enter key')
            Note that this statement waits for input but ignores
            the actual input.  That is what we want here.

    3. Shuts down the robot.
    """
    # ------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #
    # IMPORTANT: Do your work using what is called
    #    an ITERATIVE ENHANCEMENT PLAN, here:
    #      Step 1: Implement and test just the speeds/seconds input
    #                and the motion ONE time (not yet 3 times).
    #      Step 2: Implement and test the printing
    #                of the linear and angular distances.
    #      Step 3: Implement the loop that does the movement/sensing
    #                THREE (not just 1) times.
    # ------------------------------------------------------------------

    left_speed = input('Enter the left wheel speed:')
    right_speed = input('Enter the right wheel speed')
    seconds = input('Enter the number of seconds to move at that speed:')
    l = float(left_speed)
    r = float(right_speed)
    s = float(seconds)
    port = 3
    robot = new_create.Create(port)
    robot.toFullMode()
    robot.driveDirect(l, s)
    time.sleep(s)
    robot.stop()
    sensor1 = new_create.Sensors.distance
    reflectance1 = robot.getSensor(sensor1)
    print('The linear distance traveled is', reflectance1)
    sensor2 = new_create.Sensors.angle
    reflectance2 = robot.getSensor(sensor2)
    print('The angular distance traveled is', reflectance2)
    input('Press the Enter key')
    print()
    robot.shutdown()

    left_speed = input('Enter the left wheel speed:')
    right_speed = input('Enter the right wheel speed')
    seconds = input('Enter the number of seconds to move at that speed:')
    l = float(left_speed)
    r = float(right_speed)
    s = float(seconds)
    port = 3
    robot = new_create.Create(port)
    robot.toFullMode()
    robot.driveDirect(l, s)
    time.sleep(s)
    robot.stop()
    sensor1 = new_create.Sensors.distance
    reflectance1 = robot.getSensor(sensor1)
    print('The linear distance traveled is', reflectance1)
    sensor2 = new_create.Sensors.angle
    reflectance2 = robot.getSensor(sensor2)
    print('The angular distance traveled is', reflectance2)
    input('Press the Enter key')
    print()
    robot.shutdown()

    left_speed = input('Enter the left wheel speed:')
    right_speed = input('Enter the right wheel speed')
    seconds = input('Enter the number of seconds to move at that speed:')
    l = float(left_speed)
    r = float(right_speed)
    s = float(seconds)
    port = 3
    robot = new_create.Create(port)
    robot.toFullMode()
    robot.driveDirect(l, s)
    time.sleep(s)
    robot.stop()
    sensor1 = new_create.Sensors.distance
    reflectance1 = robot.getSensor(sensor1)
    print('The linear distance traveled is', reflectance1)
    sensor2 = new_create.Sensors.angle
    reflectance2 = robot.getSensor(sensor2)
    print('The angular distance traveled is', reflectance2)
    input('Press the Enter key')
    print()
    robot.shutdown()

# ----------------------------------------------------------------------
# TODO: 4.  After implementing the above, experiment to learn a bit
#   about the ACCURACY of the sensors and movement, as follows:
#     -- 1. Run the program with just linear speed
#             (i.e., left and right wheel speeds are the same)
#             for a speed and time that you choose.
#     -- 2. COMPUTE how far SHOULD the robot have moved, if it really
#             moved at the requested speed for the requested time.
#     -- 3. MEASURE how far the robot ACTUALLY moved.
#             (Measure it, with a yardstick, converting units to cm.)
#     -- 4. EXAMINE the output to see how far the robot REPORTED
#             that it moved.
#   Nothing to write down for this one, just DO it.
#   A single run is enough, but you might try varying the speed/time
#   if you want a better idea of the accuracy of the sensors/movement.
# ----------------------------------------------------------------------
    port = 3
    robot = new_create.Create(port)
    robot.toFullMode()
    robot.driveDirect(30, 30)
    time.sleep(2.0)
    robot.stop()
    sensor1 = new_create.Sensors.distance
    reflectance1 = robot.getSensor(sensor1)
    print('The linear distance traveled:', reflectance1)

    robot.driveDirect(20, 20)
    time.sleep(1.5)
    robot.stop()
    sensor1 = new_create.Sensors.distance
    reflectance1 = robot.getSensor(sensor1)
    print('The linear distance traveled:', reflectance1)

    robot.shutdown()
# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
