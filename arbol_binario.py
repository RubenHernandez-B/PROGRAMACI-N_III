import random

class NodoBinario:

    def __init__(self, movimiento, peso=1):
        self.movimiento = movimiento
        self.peso = peso
        self.izquierda = None
        self.derecha = None


class ArbolBinario:

    def __init__(self):
        self.raiz = None
        self.pesos = {}

        for i in range(9):
            self.pesos[i] = 1
            self.insertar(i)

    def insertar(self, movimiento, peso=1):

        nuevo = NodoBinario(movimiento, peso)

        if self.raiz is None:
            self.raiz = nuevo
            return

        actual = self.raiz

        while True:

            if movimiento < actual.movimiento:

                if actual.izquierda is None:
                    actual.izquierda = nuevo
                    return

                actual = actual.izquierda

            else:

                if actual.derecha is None:
                    actual.derecha = nuevo
                    return

                actual = actual.derecha

    def obtener_mejor_movimiento(self, disponibles):

        mejor_peso = -1
        mejores = []

        for posicion in disponibles:

            peso = self.pesos[posicion]

            if peso > mejor_peso:
                mejor_peso = peso
                mejores = [posicion]

            elif peso == mejor_peso:
                mejores.append(posicion)

        return random.choice(mejores)

    def aumentar_pesos(self, movimientos):

        for movimiento in movimientos:
            self.pesos[movimiento] += 1

    def disminuir_pesos(self, movimientos):

        for movimiento in movimientos:

            if self.pesos[movimiento] > 1:
                self.pesos[movimiento] -= 1

    def mostrar_pesos(self):

        print("\n===== PESOS ACTUALES =====")

        for posicion, peso in self.pesos.items():
            print(f"Posición {posicion}: {peso}")