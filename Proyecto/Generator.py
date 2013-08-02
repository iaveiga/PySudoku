import random

class Generator():
    def __init__(self):
        """Inicializa el board (tablero) vacio."""
        self.limpiar_board()
        self.puzzle = []

    def limpiar_board(self):
        """Para indicar un casillero vacio, se utiliza la convencion del foro,
        donde se explicita que un casillero vacio se representa con un punto (.)"""
        self.board = []
        for fila in xrange(9):
            self.board.append([None for i in xrange(9)])

    def en_fila(self, board, fila, numero):
        """Devuelve True si 'numero' se encuentra en la fila."""
        if numero in board[fila] and numero != None:
            return True
        else:
            return False

    def en_columna(self, board, col, numero):
        """Devuelve True si 'numero' se encuentra en la columna 'col'"""
        for fila in xrange(9):
            if board[fila][col] == numero and numero != None:
                return True
        return False

    def en_cuadro(self, board, f_cuadro, c_cuadro, numero):
        """Devuelve True si 'numero' se encuentra en el cuadro [f_cuadro, c_cuadro]"""
        for fila in range(3 * f_cuadro, 3 * f_cuadro + 3):
            for col in range(3 * c_cuadro, 3 * c_cuadro + 3):
                if board[fila][col] == numero and numero != None:
                    return True
        return False

    def poblar_board(self):
        """Esta funcion completa el tablero creando un sudoku con las reglas basicas (level-1)"""
        random.seed()
        col = 0
        while col < 9:
            valores_posibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            random.shuffle(valores_posibles)
            fila = 0
            prueba = 0
            # Se prueban los valores por fila unas 200 veces
            while fila < 9 and prueba < 200:
                malas = 0
                parar = 0
                for elem in range(0, len(valores_posibles)):
                    if (self.en_columna(self.board, col, valores_posibles[elem]) or self.en_fila(self.board, fila, valores_posibles[elem]) or self.en_cuadro(self.board, int(round(fila / 3)), int(round(col / 3)), valores_posibles[elem])):
                        malas += 1
                # Si llegue al maximo de malas (valores que quedan por probar), tengo que reiniciar
                if malas == len(valores_posibles):
                    # limpiar todos los valores de la columna
                    for fila_t in xrange(9):
                        self.board[fila_t][col] = None
                    valores_posibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    parar = 1
                    fila = 0
                    prueba += 1
                if parar == 0:
                    numero = random.randint(1, 9)
                    while (self.en_columna(self.board, col, numero) or self.en_fila(self.board, fila, numero) or self.en_cuadro(self.board, int(round(fila / 3)), int(round(col / 3)), numero)):
                        random.seed()
                        numero = random.randint(1, 9)
                    # El numero no se encuentra y cumple las condiciones, entonces asignar...
                    self.board[fila][col] = numero
                    # ... y quitar de valores_posibles para esa columna
                    valores_posibles.remove(numero)
                    fila += 1
            col += 1
            if prueba == 200:
                self.limpiar_board()
                col = 0


    def gen_puzzle(self, dificultad):
        # con el board lleno genera un puzzle, vaciando celdas al azar
        # obtener posicion al azar
        self.puzzle = self.board
        i = 0
        if dificultad == 1:
            casillas = random.randint(36,41)
        elif dificultad == 2:
            casillas = random.randint(32,35)
        elif dificultad == 3:
            casillas = random.randint(28,31)
        else:
            casillas = random.randint(23,27)
            
        casillas = 81 - casillas
        
        while (i < casillas):

            pos = int(random.randint(0, 80))
            fila, col = divmod(pos, 9)
            if self.puzzle[fila][col] != 0:
                self.puzzle[fila][col] = 0
                i = i + 1
