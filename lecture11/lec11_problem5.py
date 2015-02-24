# Desc: Lec 11, Problem 5.
# Author: Javier Herrero Arnanz.

class intSet(object):
    """An intSet is a set of integers.
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers."""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self.""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer.
           Returns True if e is in self, and False otherwise."""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self.
           Raises ValueError if e is not in self."""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def intersect(self,other):
        """Returns a new intSet containing elements that appear in self and other."""
        assert type(other) == type(self)
        inter = intSet()
        for i in self.vals:
            if (other.member(i)):
                inter.insert(i)
        return inter

    def __str__(self):
        """Returns a string representation of self."""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def __len__(self):
        """Returns the number of elements in self."""
        return len(self.vals)
