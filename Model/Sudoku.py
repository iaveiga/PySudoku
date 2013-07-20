from Cell import Cell

class Sudoku(object):
    pass
    
    def __init__(self):
        self.matrix = []
        li = []
        for i in range(0,9):
            for j in range(0,9):
                aux = Cell(1,1,0)
                li.append(aux)
            self.matrix.append(li)

    def setCell(self, i = int, j = int, c = Cell):
        self.matrix[i][j] = c

    def getCell(self, i = int ,j = int):
        return self.matrix[i][j]

    def checkCol(self, c = Cell):
        reales = []
        imaginarios = []
        j = c.getY()
        for i in range(0,9):
            if inList(reales,self.matrix[i][j]):
                imaginarios.append(self.matrix[i][j])
            else:
                reales.append(self.matrix[i][j])
                    
    def inList(ls = list, b = Cell):
        if len(ls) == 0:
            return false
        for i in range(0,len(ls)):
            if ls[i].getValue() == b.getValue():
                return true
        return false

    def usedInRow(self, row = int, num = int):
        for col in range(0,9):
            if (self.getCell(row,col).getValue == num ):
                return true
        return false

    def usedInCol(self, col = int, num = int):
        for row in range(0,9):
            	if (self.getCell(row,col).getValue() == num  ):
                    return true
        return false

    def usedInBox(self, startRow = int, startCol = int, num = int):
        for i in range(0,3):
            for j in range(0,3):
                if(self.getCell(i + startRow,j + startCol).getValue() == num):
                    return true
        return false

    def noConflicts(self, row = int, col = int, num = int):
        resp = (not self.usedInRow(self, row, num)) and (not self.usedInCol(self,col,num))
        resp = resp and (not self.usedInBox(self,row - row%3, col - col%3,num))
        return resp

    def next(self, row = int, col = int):
        if col < 8:
            solve(self,row, col + 1)
        else :
            solve (self, row + 1, 0)    
        

    def solve(self, row, col):
        if self.matrix[i][j] != 0:
            next(self, row, col)
        else:
            for i in range(0,9):
                if noConflicts(self, row, col, num):
                    self.matrix[i][j] = num
                next(self, row, col)
        self.matrix[i][j] = 0
                
    def solveAll(self):
        solve(self,0,0)

    


    
