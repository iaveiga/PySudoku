from Cell import Cell
import sys
import random


class Sudoku(object):
    pass


    def __init__(self):
        self.matrix = [[0 for x in xrange(9)] for x in xrange(9)] #Crea una matriz vacia de 9 x 9
        li = []
        for i in range(0,9):
            for j in range(0,9):
                aux = Cell(i,j,0)
                self.matrix[i][j] = aux

    def setCell(self, i = int, j = int, c = Cell):
        self.matrix[i][j] = c

    def printS(self):
        for i in range(0,9):
            for j in range(0,9):
                print self.matrix[i][j].getValue() , "\t "
            print "\n"

    def getCell(self, i = int ,j = int):
        return self.matrix[i][j]

    def usedInRow(self, row = int, num = int):
        for col in range(0,9):
            if (self.getCell(row,col).getValue == num):
                return False
        return True

    def usedInCol(self, col = int, num = int):
        for row in range(0,9):
            if (self.getCell(row,col).getValue() == num):
                return False
        return True

    def usedInBox(self, startRow = int, startCol = int, num = int):
        for i in range(0,3):
            for j in range(0,3):
                if(self.getCell(i + startRow,j + startCol).getValue() == num):
                    return False
        return True

    def noConflicts(self, row = int, col = int, num = int):
        resp = (self.usedInRow(row, num)) and (self.usedInCol(col,num))
        resp = resp and (self.usedInBox(row - row%3, col - col%3,num))
        return resp

    def next(self, row = int, col = int):
        if col < 7:
            self.solve(row, col + 1)
        else:
            self.solve (row + 1, 0)

    def solve(self, row = int, col = int):
        if row > 8:
            sys.exit()
        elif self.getCell(row,col).getValue() != 0: 
            self.next(row, col) #if a cell is not empty, continue next cell
        else:
            for num in range(1,10):
                if self.noConflicts(row, col, num):
                    c = Cell(row,col,num)
                    self.setCell(row,col, c)
                    self.next(row,col)
            c = Cell(row,col,0)
            self.setCell(row,col,c)


    def solveAll(self):
        self.solve(0,0)

    def load(self):
        f = open("C:/s1.txt","r")
        lines = f.readlines()
        for i in range(0,9):
            p = lines[i].lstrip()
            for j in range(0,9):
                c = Cell(i,j,int(p[j]))
                self.setCell(i,j,c)
        f.close()

    def cleanBoard(self):
        for i in range(0,9):
            for j in range(0,9):
                self.getCell(i,j).setValue(0)

    def parse(self, board):
        for i in range(0,9):
            for j in range(0,9):
                c = Cell(i,j,board[i][j])
                self.setCell(i,j,c)
    def compare(self, other):
    #retorna la listas de celdas en que other difiere de self
    #self (tablero lleno), other tablero a jugar
        li = []
        for i in range(0,9):
            for j in range(0,9):
                if self.getCell(i,j).getValue() != other.getCell(i,j).getValue():
                    li.append(other.getCell(i,j))
        return li
