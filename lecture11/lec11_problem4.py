# Desc: Lec 11, Problem 4.
# Author: Javier Herrero Arnanz.

class Coordinate(object):
    """A Coordinate is a point in 2D (x,y)."""
    
    def __init__(self,x,y):
        """Initializes the object."""
        self.x = x
        self.y = y

    def getX(self):
        """Getter method for a Coordinate object's x coordinate."""
        return self.x

    def getY(self):
        """Getter method for a Coordinate object's y coordinate."""
        return self.y

    def __str__(self):
        """Print the object data as a string."""
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
        
    def __eq__(self,other):
        """Returns True if coordinates refer to same point in the plane."""
        assert type(other) == type(self)
        return ((self.x == other.x) and (self.y == other.y))
        
    def __repr__(self):
        """Returns a string that looks like a valid Python expression 
        that could be used to recreate an object with the same value."""
        return 'Coordinate('+str(self.x)+', '+str(self.y)+')'
