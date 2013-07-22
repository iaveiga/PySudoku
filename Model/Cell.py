# -*- coding: cp1252 -*-
class Cell(object):
    pass
    
    def __init__(self, x = int , y = int , value = int):
        #Constructor con params
        self.__x = x
        self.__y = y
        self.__value = value

    #Getters
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getValue(self):
        return self.__value

    #Setters
    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def setValue(self, value):
        self.__value = value

    
    def equals(self, other):
        return self.__x == other.getX() and self.__y == other.getY() and self.__value == other.getValue()

    def printC(self):
        print "x: ", self.__x , " , y:", self.__y, " , v: ", self.__value
