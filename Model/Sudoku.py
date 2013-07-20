from Cell import Cell

class Sudoku(object):
    pass

    '''
    def __init__(self):
        self.matrix = []
        li = []
        for i in range(0,9):
            for j in range(0,9):
                aux = Cell(1,1,0)
                li.append(aux)
            self.matrix.append(li)
    '''

    def __init__(self):
        self.matrix = []
        self.matrix.append([9,0,0,0,2,0,7,5,0])
        self.matrix.append([6,0,0,0,5,0,0,4,0])
        self.matrix.append([0,2,0,4,0,0,0,1,0])
        self.matrix.append([2,0,8,0,0,0,0,0,0])
        self.matrix.append([0,7,0,5,0,9,0,6,0])
        self.matrix.append([0,0,0,0,0,0,4,0,1])
        self.matrix.append([0,1,0,0,0,5,0,8,0])
        self.matrix.append([0,9,0,0,7,0,0,0,4])
        self.matrix.append([0,8,2,0,4,0,0,0,6])

    def setCell(self, i = int, j = int, c = Cell):
        self.matrix[i][j] = c

    def printS(self):
        for i in range(0,9):
            for j in range(0,9):
                print self.matrix[i][j] , "\t "
            print "\n"

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
            return False
        for i in range(0,len(ls)):
            if ls[i].getValue() == b.getValue():
                return True
        return False

    def usedInRow(self, row = int, num = int):
        for col in range(0,9):
            #if (self.getCell(row,col).getValue == num ):
            if (self.matrix[row][col] == num ):
                return False
        return True

    def usedInCol(self, col = int, num = int):
        for row in range(0,9):
            #if (self.getCell(row,col).getValue() == num):
            if (self.matrix[row][col] == num ):
                return False
        return True

    def usedInBox(self, startRow = int, startCol = int, num = int):
        for i in range(0,3):
            for j in range(0,3):
                #if(self.getCell(i + startRow,j + startCol).getValue() == num):
                if(self.matrix[i + startRow][j + startCol] == num):
                    return False
        return True

    def noConflicts(self, row = int, col = int, num = int):
        resp = (self.usedInRow(row, num)) and (self.usedInCol(col,num))
        resp = resp and (self.usedInBox(row - row%3, col - col%3,num))
        return resp

    def next(self, row = int, col = int):
        if col < 8:
            self.solve(row, col + 1)
        else :
            self.solve (row + 1, 0)    
        

    def solve(self, row, col):
        if row > 8:
            return 0
        if self.matrix[row][col] != 0:
            self.next(row, col)
        else:
            for num in range(1,9+1):
                if self.noConflicts(row, col, num):
                    self.matrix[row][col] = num
                    self.next(row, col)
            self.matrix[row][col] = 0
                
    def solveAll(self):
        self.solve(0,0)
