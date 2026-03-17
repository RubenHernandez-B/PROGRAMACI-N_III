import os

class Nodo:
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.carnet})"


class Lista:
    def __init__(self):
        self.cabeza = None
        self.contador_graficas = 0 

    # graficos
    def graficar(self, operacion="lista"):
        nombre_archivo = f"{operacion}_{self.contador_graficas}"
        archivo = open(nombre_archivo + ".dot", "w", encoding="utf-8")

        archivo.write("digraph G {\n")
        archivo.write("rankdir=LR;\n")
        archivo.write("node [shape=record];\n")

        actual = self.cabeza
        i = 0

        # crear nodos
        while actual:
            etiqueta = f"<ant> | {actual.nombre}\\n{actual.apellido}\\n{actual.carnet} | <sig>"
            archivo.write(f'n{i} [label="{etiqueta}"];\n')

            actual = actual.siguiente
            i += 1

        # crear enlaces
        actual = self.cabeza
        i = 0

        while actual and actual.siguiente:
            archivo.write(f"n{i}:sig -> n{i+1}:ant;\n")
            archivo.write(f"n{i+1}:ant -> n{i}:sig;\n")

            actual = actual.siguiente
            i += 1

        archivo.write("}\n")
        archivo.close()

        # generar imagen PNG
        os.system(f"dot -Tpng {nombre_archivo}.dot -o {nombre_archivo}.png")

        print(f"Gráfica generada: {nombre_archivo}.png")

        self.contador_graficas += 1


    # INSERTAR inicio
    def principio(self, nombre, apellido, carnet):
        nuevo = Nodo(nombre, apellido, carnet)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo

        print("NODO INSERTADO AL PRINCIPIO.")

       
        self.graficar("insertar_inicio")


    # INSERTAFINAL
    def final(self, nombre, apellido, carnet):
        nuevo = Nodo(nombre, apellido, carnet)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente

            actual.siguiente = nuevo
            nuevo.anterior = actual

        print("NODO INSERTADO AL FINAL.")

        # GRAFICAR
        self.graficar("insertar_final")


    # ELIMINACION POR CARNET
    def eliminar(self, carnet):
        actual = self.cabeza

        while actual:
            if actual.carnet == carnet:

                # único nodo
                if actual.anterior is None and actual.siguiente is None:
                    self.cabeza = None

                # primero
                elif actual.anterior is None:
                    self.cabeza = actual.siguiente
                    self.cabeza.anterior = None

                # último
                elif actual.siguiente is None:
                    actual.anterior.siguiente = None

                # medio
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior

                print("Nodo eliminado.")

                # GRAFICAR
                self.graficar("eliminar")

                return

            actual = actual.siguiente

        print("CARNET NO ENCONTRADO.")


    
    def mostrar_lista(self):
        if self.cabeza is None:
            print("None <- -> None")
            return

        actual = self.cabeza
        texto = "None <- "

        while actual:
            texto += str(actual)
            if actual.siguiente:
                texto += " <-> "
            actual = actual.siguiente

        texto += " -> None"
        print(texto)


def menu():
    lista = Lista()

    while True:
        print("\n--- MENÚ ---")
        print("1. Insertar al principio")
        print("2. Insertar al final")
        print("3. Eliminar por carnet")
        print("4. Mostrar lista")
        print("5. Salir")

        opcion = input("HAGA SU SELECCIÓN: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            carnet = input("Carnet: ")
            lista.principio(nombre, apellido, carnet)

        elif opcion == "2":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            carnet = input("Carnet: ")
            lista.final(nombre, apellido, carnet)

        elif opcion == "3":
            carnet = input("Carnet a eliminar: ")
            lista.eliminar(carnet)

        elif opcion == "4":
            lista.mostrar_lista()

        elif opcion == "5":
            print("Saliendo.....")
            break

        else:
            print("Opcion inválida.")


menu()
