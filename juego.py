from graphviz_utils import generar_grafo_partida


class JuegoTotito:

    def __init__(self, historial, arbol=None):
        self.tablero = [" " for _ in range(9)]
        self.turno = "X"
        self.historial = historial
        self.arbol = arbol
        self.id_partida = historial.obtener_total() + 1
        self.movimientos = []
        self.movimientos_ia = []

    def mostrar_tablero(self):

        print()
        print(f" {self.tablero[0]} | {self.tablero[1]} | {self.tablero[2]}")
        print("-----------")
        print(f" {self.tablero[3]} | {self.tablero[4]} | {self.tablero[5]}")
        print("-----------")
        print(f" {self.tablero[6]} | {self.tablero[7]} | {self.tablero[8]}")
        print()

    def verificar_ganador(self):

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

            if self.tablero[a] == self.tablero[b] == self.tablero[c] != " ":
                return self.tablero[a]

        if " " not in self.tablero:
            return "Empate"

        return None

    def guardar_partida(self, ganador):

        resumen = f"Ganador: {ganador}"

        self.historial.insertar({
            "id": self.id_partida,
            "resultado": resumen,
            "tablero": self.tablero.copy()
        })

        generar_grafo_partida(self.id_partida, self.movimientos)

    def jugar_manual(self):

        while True:

            self.mostrar_tablero()

            posicion = int(input(f"Jugador {self.turno}, posición (0-8): "))

            if self.tablero[posicion] == " ":

                self.tablero[posicion] = self.turno
                self.movimientos.append((self.turno, posicion))

                ganador = self.verificar_ganador()

                if ganador:

                    self.mostrar_tablero()
                    print(f"Resultado: {ganador}")

                    self.guardar_partida(ganador)
                    break

                self.turno = "O" if self.turno == "X" else "X"

            else:
                print("Casilla ocupada")

    def jugar_ia(self):

        while True:

            self.mostrar_tablero()

            if self.turno == "X":

                posicion = int(input("Tu movimiento (0-8): "))

                if self.tablero[posicion] != " ":
                    print("Casilla ocupada")
                    continue

            else:

                disponibles = [i for i in range(9) if self.tablero[i] == " "]

                posicion = self.arbol.obtener_mejor_movimiento(disponibles)

                self.movimientos_ia.append(posicion)

                print(f"IA juega en posición: {posicion}")

            self.tablero[posicion] = self.turno
            self.movimientos.append((self.turno, posicion))

            ganador = self.verificar_ganador()

            if ganador:

                self.mostrar_tablero()
                print(f"Resultado: {ganador}")

                if ganador == "O":
                    self.arbol.aumentar_pesos(self.movimientos_ia)

                elif ganador == "X":
                    self.arbol.disminuir_pesos(self.movimientos_ia)

                self.arbol.mostrar_pesos()

                self.guardar_partida(ganador)

                break

            self.turno = "O" if self.turno == "X" else "X"