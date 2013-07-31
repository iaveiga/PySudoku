from Sudoku import Sudoku
from Generator import Generator
import copy

class Juego(object):

    def __init__(self, nombre, dif = int):
        self.nombre = nombre
        self.dif = dif
        self.time = 0
        self.juego = Sudoku() #tablero a jugar
        self.tablero = Sudoku()   #tablero lleno
        self.create(dif)

    def create(self, dif = int):
        g = Generator()
        g.poblar_board()
        g.gen_puzzle(dif)
        self.juego.parse(g.puzzle)
        self.juego.parse(g.board)
        



