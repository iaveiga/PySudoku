from Cell import Cell

import math

class Sudoku(object):
    pass
    
    def __init__(self):
        self.matrix = []
        self.centros = []
        li = []
        for i in range(0,9):
            for j in range(0,9):
                aux = Cell(1,1,0)
                li.append(aux)
            self.matrix.append(li)

        a = Cell(1,1,0), self.centros.append(a)
        b = Cell(1,4,0), self.centros.append(b)
        c = Cell(1,7,0), self.centros.append(c)
        d = Cell(4,1,0), self.centros.append(d)
        e = Cell(4,4,0), self.centros.append(e)
        f = Cell(4,7,0), self.centros.append(f)
        g = Cell(7,1,0), self.centros.append(g)
        h = Cell(7,4,0), self.centros.append(h)
        i = Cell(7,7,0), self.centros.append(i)
    

    def setCell(self, i = int, j = int, c = Cell):
        self.matrix[i][j] = c

    def getCell(self, i = int ,j = int):
        return self.matrix[i][j]

    def distance(Cell c, Cell d):
        answer = 0.0
        answer = math.sqrt( (c.getX() - d.getX()) ** 2 + (c.getY() - d.getY()) ** 2)
        return answer

    def checkCol(self, Cell c):
        reales = []
        imaginarios = []
        j = c.getY()
        for i in range(0,9):
            if inList(reales,self.matrix[i][j]):
                imaginarios.append(self.matrix[i][j])
            else:
                reales.append(self.matrix[i][j])
                    
    def inList(list ls, Cell b):
        if len(ls) == 0:
            return false
        for i in range(0,len(ls)):
            if ls[i].getValue() == b.getValue():
                return true
        return false
