import csv
import graphviz


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None



class ABB:
    def __init__(self):
        self.raiz = None

  
    def insertar(self, valor):
        self.raiz = self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izq = self._insertar(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._insertar(nodo.der, valor)
        return nodo

    
    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        elif valor < nodo.valor:
            return self._buscar(nodo.izq, valor)
        else:
            return self._buscar(nodo.der, valor)


    def eliminar(self, valor):
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo, valor):
        if nodo is None:
            return nodo

        if valor < nodo.valor:
            nodo.izq = self._eliminar(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._eliminar(nodo.der, valor)
        else:
            # Sin hijos
            if nodo.izq is None and nodo.der is None:
                return None
            # Un hijo
            if nodo.izq is None:
                return nodo.der
            if nodo.der is None:
                return nodo.izq
            # Dos hijos
            sucesor = self._minimo(nodo.der)
            nodo.valor = sucesor.valor
            nodo.der = self._eliminar(nodo.der, sucesor.valor)

        return nodo

    def _minimo(self, nodo):
        while nodo.izq is not None:
            nodo = nodo.izq
        return nodo


    def graficar(self, resaltado=None):
        dot = graphviz.Digraph()

        dot.attr(rankdir='TB')
        dot.attr('node', shape='circle')

        def recorrer(nodo):
            if nodo:
               
                if nodo.valor == resaltado:
                    dot.node(str(nodo.valor), style='filled', fillcolor='red')
                else:
                    dot.node(str(nodo.valor), style='filled', fillcolor='lightblue')

              
                if nodo.izq:
                    dot.edge(str(nodo.valor), str(nodo.izq.valor), label="L")
                    recorrer(nodo.izq)
                else:
                    null_izq = f"nullL{nodo.valor}"
                    dot.node(null_izq, shape="point")
                    dot.edge(str(nodo.valor), null_izq)

             
                if nodo.der:
                    dot.edge(str(nodo.valor), str(nodo.der.valor), label="R")
                    recorrer(nodo.der)
                else:
                    null_der = f"nullR{nodo.valor}"
                    dot.node(null_der, shape="point")
                    dot.edge(str(nodo.valor), null_der)

        recorrer(self.raiz)
        dot.render("arbol", format="png", view=True)



def cargar_csv(arbol, ruta):
    try:
        with open(ruta, newline='') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                for valor in fila:
                    arbol.insertar(int(valor))
        print("Datos cargados correctamente.")
    except Exception as e:
        print("Error al cargar archivo:", e)



def menu():
    arbol = ABB()

    while True:
        print("\n--- MENU ABB ---")
        print("1. Insertar")
        print("2. Buscar")
        print("3. Eliminar")
        print("4. Cargar desde CSV")
        print("5. Mostrar árbol (Graphviz)")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                valor = int(input("Ingrese número: "))
                arbol.insertar(valor)
                print("Insertado.")
                arbol.graficar()
            except:
                print("Ingrese un número válido.")

        elif opcion == "2":
            try:
                valor = int(input("Ingrese número a buscar: "))
                if arbol.buscar(valor):
                    print("Valor encontrado.")
                    arbol.graficar(resaltado=valor)
                else:
                    print("El valor NO está en el árbol.")
            except:
                print("Ingrese un número válido.")

        elif opcion == "3":
            try:
                valor = int(input("Ingrese número a eliminar: "))
                arbol.eliminar(valor)
                print("Eliminado.")
                arbol.graficar()
            except:
                print("Ingrese un número válido.")

        elif opcion == "4":
            ruta = input("Ingrese ruta del archivo CSV: ")
            cargar_csv(arbol, ruta)
            arbol.graficar()

        elif opcion == "5":
            arbol.graficar()

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()