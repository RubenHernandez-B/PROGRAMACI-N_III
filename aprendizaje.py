import random


class Entrenamiento:

    def __init__(self, historial, arbol):
        self.historial = historial
        self.arbol = arbol

    def verificar_ganador(self, tablero):

        combinaciones = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]

        for a, b, c in combinaciones:

            if tablero[a] == tablero[b] == tablero[c] != " ":
                return tablero[a]

        if " " not in tablero:
            return "Empate"

        return None

    def simular(self, cantidad):

        for _ in range(cantidad):

            tablero = [" " for _ in range(9)]
            jugador = "X"
            movimientos_ia = []

            while True:

                disponibles = [i for i in range(9) if tablero[i] == " "]

                if not disponibles:

                    self.historial.insertar({
                        "id": self.historial.obtener_total() + 1,
                        "resultado": "Ganador: Empate",
                        "tablero": tablero.copy()
                    })

                    break

                if jugador == "O":

                    posicion = self.arbol.obtener_mejor_movimiento(disponibles)
                    movimientos_ia.append(posicion)

                else:

                    posicion = random.choice(disponibles)

                tablero[posicion] = jugador

                ganador = self.verificar_ganador(tablero)

                if ganador:

                    if ganador == "O":
                        self.arbol.aumentar_pesos(movimientos_ia)

                    elif ganador == "X":
                        self.arbol.disminuir_pesos(movimientos_ia)

                    self.historial.insertar({
                        "id": self.historial.obtener_total() + 1,
                        "resultado": f"Ganador: {ganador}",
                        "tablero": tablero.copy()
                    })

                    break

                jugador = "O" if jugador == "X" else "X"

        print(f"\nSe simularon {cantidad} partidas")

        self.arbol.mostrar_pesos()