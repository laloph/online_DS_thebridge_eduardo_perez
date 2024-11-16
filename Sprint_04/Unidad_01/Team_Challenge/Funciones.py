import random

def disparo_aleatorio(jugador_objetivo):
    x, y = random.randint(0, DIMENSION_TABLERO - 1), random.randint(0, DIMENSION_TABLERO - 1)
    resultado = jugador_objetivo.tablero.disparar(x, y)
    return resultado

def disparo_manual(jugador_objetivo, x, y):
    if jugador_objetivo.tablero.historial_disparos[x, y] != " ":
        print("Ya disparaste en esta posición.")
        return None
    return jugador_objetivo.tablero.disparar(x, y)
