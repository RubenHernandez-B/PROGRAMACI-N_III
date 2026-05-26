class ArbolB:

    def __init__(self, grado=3):
        self.grado = grado
        self.registros = []

    def insertar(self, partida):
        self.registros.append(partida)

    def mostrar(self):

        if not self.registros:
            print("No hay partidas registradas")
            return

        print("\n===== HISTORIAL =====")

        for partida in self.registros:
            
            print(f"ID: {partida['id']}")
            print(f"Resultado: {partida['resultado']}")

            tablero = partida['tablero']

            print(f" {tablero[0]} | {tablero[1]} | {tablero[2]}")
            print("-----------")
            print(f" {tablero[3]} | {tablero[4]} | {tablero[5]}")
            print("-----------")
            print(f" {tablero[6]} | {tablero[7]} | {tablero[8]}")
            
            print("-----------------------")

    def obtener_total(self):
        return len(self.registros)