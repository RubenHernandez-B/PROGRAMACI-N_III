import csv
from graphviz import Digraph


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1



class ABB:
    def insertar(self, raiz, valor):
        if not raiz:
            return Nodo(valor)
        if valor < raiz.valor:
            raiz.izq = self.insertar(raiz.izq, valor)
        else:
            raiz.der = self.insertar(raiz.der, valor)
        return raiz

    def buscar(self, raiz, valor):
        if not raiz or raiz.valor == valor:
            return raiz
        if valor < raiz.valor:
            return self.buscar(raiz.izq, valor)
        return self.buscar(raiz.der, valor)

    def minimo(self, nodo):
        actual = nodo
        while actual.izq:
            actual = actual.izq
        return actual

    def eliminar(self, raiz, valor):
        if not raiz:
            return raiz

        if valor < raiz.valor:
            raiz.izq = self.eliminar(raiz.izq, valor)
        elif valor > raiz.valor:
            raiz.der = self.eliminar(raiz.der, valor)
        else:
            if not raiz.izq:
                return raiz.der
            elif not raiz.der:
                return raiz.izq

            temp = self.minimo(raiz.der)
            raiz.valor = temp.valor
            raiz.der = self.eliminar(raiz.der, temp.valor)

        return raiz


class AVL(ABB):

    def altura(self, nodo):
        return nodo.altura if nodo else 0

    def balance(self, nodo):
        return self.altura(nodo.izq) - self.altura(nodo.der) if nodo else 0

    def rotar_derecha(self, y):
        x = y.izq
        T2 = x.der

        x.der = y
        y.izq = T2

        y.altura = 1 + max(self.altura(y.izq), self.altura(y.der))
        x.altura = 1 + max(self.altura(x.izq), self.altura(x.der))

        return x

    def rotar_izquierda(self, x):
        y = x.der
        T2 = y.izq

        y.izq = x
        x.der = T2

        x.altura = 1 + max(self.altura(x.izq), self.altura(x.der))
        y.altura = 1 + max(self.altura(y.izq), self.altura(y.der))

        return y

    def insertar(self, raiz, valor):
        raiz = super().insertar(raiz, valor)

        raiz.altura = 1 + max(self.altura(raiz.izq), self.altura(raiz.der))

        balance = self.balance(raiz)

       
        if balance > 1 and valor < raiz.izq.valor:
            return self.rotar_derecha(raiz)

        if balance < -1 and valor > raiz.der.valor:
            return self.rotar_izquierda(raiz)

        if balance > 1 and valor > raiz.izq.valor:
            raiz.izq = self.rotar_izquierda(raiz.izq)
            return self.rotar_derecha(raiz)

        if balance < -1 and valor < raiz.der.valor:
            raiz.der = self.rotar_derecha(raiz.der)
            return self.rotar_izquierda(raiz)

        return raiz

    def eliminar(self, raiz, valor):
        raiz = super().eliminar(raiz, valor)

        if not raiz:
            return raiz

        raiz.altura = 1 + max(self.altura(raiz.izq), self.altura(raiz.der))
        balance = self.balance(raiz)

     
        if balance > 1 and self.balance(raiz.izq) >= 0:
            return self.rotar_derecha(raiz)

        if balance > 1 and self.balance(raiz.izq) < 0:
            raiz.izq = self.rotar_izquierda(raiz.izq)
            return self.rotar_derecha(raiz)

        if balance < -1 and self.balance(raiz.der) <= 0:
            return self.rotar_izquierda(raiz)

        if balance < -1 and self.balance(raiz.der) > 0:
            raiz.der = self.rotar_derecha(raiz.der)
            return self.rotar_izquierda(raiz)

        return raiz

def graficar_nodo(valor):
    dot = Digraph(format="png")
    dot.node(str(valor), style="filled", fillcolor="lightgreen")
    dot.render("nodo_encontrado", view=True)


def graficar_arbol(raiz):
    dot = Digraph(format="png")
    def agregar_nodos(nodo):
        if nodo:
            dot.node(str(nodo.valor))
            if nodo.izq:
                dot.edge(str(nodo.valor), str(nodo.izq.valor))
                agregar_nodos(nodo.izq)
            if nodo.der:
                dot.edge(str(nodo.valor), str(nodo.der.valor))
                agregar_nodos(nodo.der)

    agregar_nodos(raiz)
    dot.render("arbol_avl", view=True, format="png")



def cargar_csv(ruta, arbol, raiz):
    try:
        with open(ruta, newline='') as archivo:
            reader = csv.reader(archivo)
            for fila in reader:
                for valor in fila:
                    raiz = arbol.insertar(raiz, int(valor))
        print("Datos cargados correctamente.")
    except Exception as e:
        print("Error al cargar CSV:", e)

    return raiz


def menu():
    arbol = AVL()
    raiz = None

    while True:
        print("\n--- MENÚ AVL ---")
        print("1. Insertar")
        print("2. Buscar")
        print("3. Eliminar")
        print("4. Cargar desde CSV")
        print("5. Visualizar con Graphviz")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            entrada = input("Ingrese número(s) (Separados por coma o espacio): ")

            try:
                valores = [int(x) for x in entrada.replace(",", " ").split()]

                for valor in valores:
                    raiz = arbol.insertar(raiz, valor)

                print("Valores insertados correctamente.")

            except ValueError:
                print("Error: ingrese solo números validos.")

        elif opcion == "2":
            try:
                valor = int(input("Buscar numero: "))
                encontrado = arbol.buscar(raiz, valor)

                if encontrado:
                    print("Valor encontrado, mostrando nodo...")
                    graficar_nodo(valor)
                else:
                    print("No encontrado")

            except ValueError:
                print("Ingrese un número valido.")

        elif opcion == "3":
            try:
                valor = int(input("Eliminar numero: "))
                raiz = arbol.eliminar(raiz, valor)
            except ValueError:
                print("Ingrese un numero válido.")

        elif opcion == "4":
            ruta = input("Ruta del CSV: ")
            raiz = cargar_csv(ruta, arbol, raiz)

        elif opcion == "5":
            graficar_arbol(raiz)

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción invalida")


if __name__ == "__main__":
    menu()