# Desc: Lec 11, Problem 6.
# Author: Javier Herrero Arnanz.

class Queue(object):
    """A Queue is a first-in-first-out (FIFO) data object."""
    
    def __init__(self):
        """Create an empty queue."""
        self.vals = []
        
    def insert(self,e):
        """Inserts one element in the queue."""
        self.vals.append(e)
        
    def remove(self):
        """Removes one element from the queue and returns it."""
        try:
            return self.vals.pop(0)
        except:
            raise ValueError('Queue is empty')
