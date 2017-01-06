"""
A simple   Point   class.  It is the same as the one developed
in a video that was part of this session's Preparation.

NOTE: This is NOT rosegraphics -- it is your OWN Point class.
It is a barebones example that can:
  -- Serve as an example of ALL the key concepts.
  -- Help you get started in the next exercise.
"""


def main():
    """ Calls the   TEST   functions in this module. """
    test_Point()


def test_Point():
    """ Tests (in a rudimentary way) the Point class. """
    p1 = Point(31, 8)

    print(p1.x)
    print(p1.y)
    print(p1.moves)

    p1.move_by(10, -5)

    print()
    print(p1.x)
    print(p1.y)
    print(p1.moves)

    Point.move_by(p1, 2, 5)

    print()
    print(p1.x)
    print(p1.y)
    print(p1.moves)


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.moves = 0

#         self.move_by(1, 2)

    def move_by(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        self.moves = self.moves + 1


# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
