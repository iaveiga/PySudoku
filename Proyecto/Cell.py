# -*- coding: utf-8 -*-

class Cell(object):
    pass

    def __init__(self, x = int , y = int , value = int):
        """
            Constructor de la clase Celda.
            x: coordenada x en el tablero de la celda
            y: coordenada y en el tablero de la celda
            value: valor de la celda.
            occupied: si la celda forma parte del Sudoku a resolver.
            @author Iván Aveiga
        """
        self.__x = x
        self.__y = y
        self.__value = value
        self.__occupied = False

    #Getters
    def getX(self):
        """
            Devuelve el atributo x.
            @return x.
            @author Iván Aveiga
        """
        return self.__x

    def getY(self):
        """
            Devuelve el atributo y.
            @return y.
            @author Iván Aveiga
        """
        return self.__y

    def getValue(self):
        """
            Devuelve el atributo value.
            @return value.
            @author Iván Aveiga
        """
        return self.__value

    def getOccupied(self):
        """
            Devuelve el atributo occupied.
            @return ocuppied.
        """
        return self.__occupied

    #Setters
    def setX(self, x = int):
        """
            Establece el valor del atributo x.
            @param int x.
            @author Iván Aveiga
        """
        self.__x = x

    def setY(self, y = int):
        """
            Establece el valor del atributo x.
            @param int y.
        """
        self.__y = y

    def setValue(self, value = int):
        """
            Establece el valor del atributo value.
            @param int value.
            @author Iván Aveiga
        """
        self.__value = value

    def setOccupied(self, occupied = bool):
        """
            Establece el valor del atributo occupied.
            @param bool occupied.
            @author Iván Aveiga
        """
        self.__occupied = occupied

    def equals(self, other):
        """
            Compara si dos celdas son iguales en valor y en coordenadas.
            @param other, celda a comparar.
            @author Iván Aveiga
        """
        return self.__x == other.getX() and self.__y == other.getY() and self.__value == other.getValue()

    def printC(self):
        """
            Imprime en consola el valor x,y value de una celda.
            @author Iván Aveiga
        """
        print "x: ", self.__x , " , y:", self.__y, " , v: ", self.__value

