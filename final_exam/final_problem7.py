# Desc: Final Exam - Problem 7.
# Author: Javier Herrero Arnanz.

class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
        
def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    inserted = False
    while (not inserted):
        if (newFrob.myName() >= atMe.myName()):
            after = atMe.getAfter()
            if (after == None): # Position found.
                newFrob.setBefore(atMe)
                atMe.setAfter(newFrob)
                inserted = True
            else:
                if (newFrob.myName() <= after.myName()): # Position found.
                    newFrob.setBefore(atMe)
                    newFrob.setAfter(after)
                    atMe.setAfter(newFrob)
                    after.setBefore(newFrob)
                    inserted = True
                else: # Increase position.
                    atMe = after
                    
        elif (newFrob.myName() < atMe.myName()):
            before = atMe.getBefore()
            if (before == None): # Position found.
                newFrob.setAfter(atMe)
                atMe.setBefore(newFrob)
                inserted = True
            else:
                if (newFrob.myName() >= before.myName()): # Position found.
                    newFrob.setBefore(before)
                    newFrob.setAfter(atMe)
                    atMe.setBefore(newFrob)
                    before.setAfter(newFrob)
                    inserted = True
                else: # Decrease position.
                    atMe = before

def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    if (start.getBefore() == None): # Base case.
        return start
    else: # Recursive case.
        return findFront(start.getBefore())
