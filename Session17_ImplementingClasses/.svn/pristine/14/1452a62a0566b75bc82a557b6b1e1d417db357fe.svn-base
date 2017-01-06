"""
A simple   Point   class.
NOTE: This is NOT rosegraphics -- it is your OWN Point class.

Authors: David Mutchler, Mark Hays, Michael Wollowski, Amanda Stouder,
         Chandan Rupakheti, Katie Dion, Claude Anderson, Delvin Defoe,
         Curt Clifton, Matt Boutell, Dave Fisher and their colleagues,
         and PUT YOUR NAME HERE.  October 2014.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math


def main():
    """ Calls the   TEST   functions in this module. """
    test_constructor()
    test_repr()
    test_clone()
    test_move_to()
    test_move_by()
    test_distance_from()
    test_distance_from_start()
    test_distance_travelled()
    test_closer_to()
    test_halfway_to()

# ----------------------------------------------------------------------
# TODO:  ** WATCH THE VIDEO IN THE PREPARATION FIRST. **
#        ** It explains HOW to do this exercise.      **
# But briefly:
# Implement a Point class, by implementing each of the TEST
# functions ONE BY ONE.  Do a TEST function, get it to WORK,
# then move to the next TEST function to write MORE of the class.
# Do NOT write all of the Point class at once!!!!!
# ----------------------------------------------------------------------


class Point(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.start_x = x
        self.start_y = y
        self.travel = 0
        
    def __repr__(self):
        return 'Point(' + str(self.x) + ', ' + str(self.y) + ')'
    
    def clone(self):
        return Point(self.x,self.y)
    
    def move_to(self,x,y):
        self.x = x
        self.y = y
    
    def move_by(self,dx,dy):
        self.x += dx
        self.y += dy
        
    def distance_from(self,p1):
        distance = ((self.x - p1.x) ** 2 + (self.y - p1.y) ** 2) ** 0.5
        return distance
    
    def distance_from_start(self):
        return self.distance(Point(self.start_x, self.start_y))
    
    def closer_to(self, p2, p3):
        d2 = self.distance_from(p2)
        d3 = self.distance_from(p3)
        if d2 <= d3:
            return p2
        else:
            return p3
    def halfway_to(self, p1):
        x = (self.x + p1.x) / 2
        y = (self.y + p1.y) / 2
        return Point(x, y)
        
def test_constructor():
    """
    Tests the Point class   __init__   method, that is,
    the method that runs when one constructs a Point.
    """
    print()
    print('--------------------------------------------------')
    print('Testing the Point class   __init__   method.')
    print('--------------------------------------------------')
    p1 = Point(10,10)
    p2 = Point(45.5,1.25)
    print(p1.x,p1.y)
    print(p2.x,p2.y)

def test_repr():
    """
    Tests the Point class   __repr__   method, that is,
    the method that runs when one prints a Point.
    """
    print()
    print('--------------------------------------------------')
    print('Testing the Point class   __repr__   method.')
    print('--------------------------------------------------')
    p1 = Point(10,10)
    p2 = Point(45.5,1.25)
    print(p1)
    print(p2)

def test_clone():
    """
    Tests the Point class   clone   method, that is,
    the method that returns a clone (copy) of the Point.
    """
    print()
    print('--------------------------------------------------')
    print('Testing the Point class   clone   method.')
    print('--------------------------------------------------')
    p1 = Point(10,10)
    p2 = Point(45.5,1.25)
    p3 = p1.clone()
    p4 = p2.clone()
    print(p1,p3)
    print(p2,p4)
    print(p1 == p1)
    print(p1 == p2)
    print(p1 == p3)
    print(p1 == p4)

def test_move_to():
    """
    Tests the Point class   move_to   method, that is,
    the method that takes two numbers, x and y,
    and moves the Point to the given x and y coordinates.
    """
    print()
    print('--------------------------------------------------')
    print('Testing the Point class   move_to   method.')
    print('--------------------------------------------------')
    p1 = Point(10,10)
    p1.move_to(45.5, 1.25)
    print(p1)

def test_move_by():
    """
    Tests the Point class   move_by   method, that is,
    the method that that takes two numbers, x and y,
    and translates the Point by the given x and y amounts.
    """
    print()
    print('--------------------------------------------------')
    print('Testing the Point class   move_by   method.')
    print('--------------------------------------------------')
    p1 = Point(10,10)
    p1.move_by(35.5,-8.75)
    print(p1)

def test_distance_from():
    """
    Tests the Point class   distance_from   method, that is,
    the method that takes another Point
    and returns the distance the Point is from that given Point.
    """
    print()
    print('--------------------------------------------------')
    print('Testing the Point class   distance_from   method.')
    print('--------------------------------------------------')
    p1 = Point(10,10)
    p2 = Point(45.5,1.25)
    distance = p1.distance_from(p2)
    print(distance)

def test_distance_from_start():
    """
    Tests the Point class   distance_from_start   method, that is,
    the method that returns the distance the Point's current position
    is from the position the Point was at when it was constructed.
    """
    print()
    print('--------------------------------------------------')
    print('Testing the Point class   distance_from_start   method.')
    print('--------------------------------------------------')
    start = Point(20,5)
    start.move_by(5, 80)
    start.move_to(1, 1)
    start.move_by(-1,0)
    print(start.distance_from_start())
    
def test_distance_travelled():
    """
    Tests the Point class   distance_travelled   method, that is,
    the method that returns the distance the Point has traveled
    (via move_to and move_by) since it was constructed.
    """
    print()
    print('--------------------------------------------------')
    print('Testing the Point class   distance_travelled   method.')
    print('--------------------------------------------------')


def test_closer_to():
    """
    Tests the Point class   closer_to   method, that is,
    the method that takes two Point objects p2 and p3,
    and returns whichever of p2 and p3 the Point is closer to.
    (Just to be specific, it should return p2 in the case of a tie.)
    """
    print()
    print('--------------------------------------------------')
    print('Testing the Point class   closer_to   method.')
    print('--------------------------------------------------')
    p1 = Point(0, 0)
    p2 = Point(50, 50)
    p3 = Point(100, 60)
    closer = p1.closer_to(p2, p3)
    print(closer)

def test_halfway_to():
    """
    Tests the Point class   halfway_to   method, that is,
    the method that takes another point p2
    and returns a new Point that is halfway between the Point and p2.
    That is, the x coordinate of the new Point is the average of the
    x coordinate of the Point and the x coordinate of p2,
    and likewise for the new Point's y coordinate.
    """
    print()
    print('--------------------------------------------------')
    print('Testing the Point class   halfway_to   method.')
    print('--------------------------------------------------')
    point = Point(20, 40)
    p1 = Point(40, 80)
    new_point = point.halfway_to(p1)
    print(new_point)


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
