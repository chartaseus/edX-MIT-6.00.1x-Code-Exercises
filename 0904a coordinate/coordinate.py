# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 09:24:25 2022

@author: ASUS
"""

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def __eq__(self, other):
        # assert type(self) == type(other)
        return (self.getX() is other.getX()) and (self.getY() is other.getY())
        
    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ', ' + str(self.getY()) + ')'
    
c1 = Coordinate(2,3)
c2 = Coordinate(2,3)
c3 = Coordinate(2,5)
