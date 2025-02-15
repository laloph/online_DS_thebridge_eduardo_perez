import numpy as np
import random
from variables import DIMENSION_TABLERO, BARCOS

class Tablero:
    def __init__(self, id_jugador):
        self.id_jugador = id_jugador
        self.tablero = np.full((DIMENSION_TABLERO, DIMENSION_TABLERO), " ")
        self.vidas = sum([barco["cantidad"] * barco["eslora"] for barco in BARCOS])
        self.historial_disparos = np.full((DIMENSION_TABLERO, DIMENSION_TABLERO), " ")

    def colocar_barcos(self):
        for barco in BARCOS:
            for _ in range(barco["cantidad"]):
                self._colocar_barco_aleatorio(barco["eslora"])

    def _colocar_barco_aleatorio(self, eslora):
        orientacion = random.choice(["N", "S", "E", "O"])
        colocado = False
        while not colocado:
            fila, columna = random.randint(0, DIMENSION_TABLERO - 1), random.randint(0, DIMENSION_TABLERO - 1)
            # Lógica para verificar si el barco cabe en la orientación y si el área está libre
            # Si todo está bien, colocar barco con 'O'
            # (Agregar lógica detallada aquí)

    def disparar(self, x, y):
        if self.tablero[x, y] == "O":
            self.tablero[x, y] = "X"
            self.historial_disparos[x, y] = "X"
            self.vidas -= 1
            return True
        else:
            self.tablero[x, y] = "-"
            self.historial_disparos[x, y] = "-"
            return False

class Jugador:
    def __init__(self, id_jugador):
        self.id_jugador = id_jugador
        self.tablero = Tablero(id_jugador)
        self.tablero.colocar_barcos()

    def mostrar_tablero(self):
        print(self.tablero.tablero)

    def mostrar_historial_disparos(self):
        print(self.tablero.historial_disparos)
