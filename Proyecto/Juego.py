# -*- coding: cp1252 -*-
from Sudoku import Sudoku
from Generator import Generator
import copy

class Juego(object):

    def __init__(self, nombre, dif = int):
        """
            Constructor de la clase Juego. Aquí se almacena toda la información
            correspondiente a un juego de sudoku.
            @param nombre, nombre del jugador.
            @param dif, dificultad del juego.
            @author Iván Aveiga
        """
        self.nombre = nombre
        self.dif = dif
        self.time = 0
        self.hints = 5
        self.juego = Sudoku() #tablero a jugar
        self.tablero = Sudoku()   #tablero lleno
        self.create(dif)

    def create(self, dif = int):
        """
            Crea un nuevo tablero de 9x9 enteros
            @param dif, dificultad del juego.
        """
        g = Generator()
        g.poblar_board()
        self.tablero.parse(g.board)
        g.gen_puzzle(dif)
        self.juego.parse(g.puzzle)






