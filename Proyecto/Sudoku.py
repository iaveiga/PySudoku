# -*- coding: cp1252 -*-
from Cell import Cell
import sys
import random


class Sudoku(object):
    pass


    def __init__(self):
        """
            Constructor de la clase Sudoku. Aquí se almacena toda la información
            de un tablero de Sudoku.
            @author Iván Aveiga.
        """
        self.matrix = [[0 for x in xrange(9)] for x in xrange(9)] #Crea una matriz vacia de 9 x 9
        li = []
        for i in range(0,9):
            for j in range(0,9):
                aux = Cell(i,j,0)
                self.matrix[i][j] = aux

    def setCell(self, i = int, j = int, c = Cell):
        """
            Almacena una celda en la posición ij.
            @param i Coordenada en i.
            @param j Coordenada en j.
            @param c Celda a ser almacenada en la posición ij.
            @author Iván Aveiga.
        """
        self.matrix[i][j] = c

    def getCell(self, i = int ,j = int):
        """
            Obtiene la celda de la posición ij.
            @param i Coordeanda en i.
            @param j Coordenada en j.
            @return Celda de la posición ij
            @author Iván Aveiga.
        """
        return self.matrix[i][j]

    def cleanBoard(self):
        """
            Deja por defecto un tablero de sudoku, todos los valores en 0.
            @author Iván Aveiga.
        """
        for i in range(0,9):
            for j in range(0,9):
                self.getCell(i,j).setValue(0)

    def parse(self, board):
        """
            Pasa los valores de una matriz de enteros 9 x 9 a la matriz de celdas
            @param board matriz de 9x 9 enteros.
        """
        for i in range(0,9):
            for j in range(0,9):
                c = Cell(i,j,board[i][j])
                if board[i][j] != 0:
                    c.setOccupied(True)
                self.setCell(i,j,c)

    def compare(self, other):
        """
            Compara dos sudokus, devuelve las celdas distintas entre sí..
            @param other Sudoku a comparar, no toma en cuenta las celdas vacías.
            @return lista de celdas distintas.
            @author Iván Aveiga.
        """
        li = []
        for i in range(0,9):
            for j in range(0,9):
                if int(other.getCell(i,j).getValue()) != 0:
                    if self.getCell(i,j).getValue() != other.getCell(i,j).getValue():
                        li.append(other.getCell(i,j))
        return li
