from clases import Jugador
from funciones import disparo_aleatorio, disparo_manual

def main():
    print("Bienvenido al juego Hundir la flota.")
    jugador = Jugador("Humano")
    maquina = Jugador("IA")

    turno_jugador = True
    while jugador.tablero.vidas > 0 and maquina.tablero.vidas > 0:
        if turno_jugador:
            print("Tu turno.")
            x = int(input("Introduce coordenada X (0-9): "))
            y = int(input("Introduce coordenada Y (0-9): "))
            impacto = disparo_manual(maquina, x, y)
            if impacto:
                print("¡Le has dado a un barco!")
                if maquina.tablero.vidas == 0:
                    print("¡Ganaste!")
                    break
            else:
                print("Agua.")
                turno_jugador = False
        else:
            print("Turno de la máquina.")
            if disparo_aleatorio(jugador):
                print("La máquina te ha dado.")
                if jugador.tablero.vidas == 0:
                    print("Perdiste.")
                    break
            else:
                print("La máquina falló.")
                turno_jugador = True

if __name__ == "__main__":
    main()
