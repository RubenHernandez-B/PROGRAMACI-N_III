from graphviz import Digraph
import csv


class BTreeNode:

    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []


class BTree:

    def __init__(self, grado):

        self.grado = grado
        self.max_keys = grado - 1
        self.min_keys = self.max_keys // 2
        self.root = BTreeNode(True)

    def search(self, key, node=None):

        if node is None:
            node = self.root

        i = 0

        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and node.keys[i] == key:
            return node, i

        if node.leaf:
            return None

        return self.search(key, node.children[i])

    def insert(self, key):

        root = self.root

        if len(root.keys) == self.max_keys:

            new_root = BTreeNode(False)

            new_root.children.append(root)

            self.split_child(new_root, 0)

            self.root = new_root

            self.insert_non_full(new_root, key)

        else:
            self.insert_non_full(root, key)

    def insert_non_full(self, node, key):

        i = len(node.keys) - 1

        if node.leaf:

            node.keys.append(None)

            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1

            node.keys[i + 1] = key

        else:

            while i >= 0 and key < node.keys[i]:
                i -= 1

            i += 1

            if len(node.children[i].keys) == self.max_keys:

                self.split_child(node, i)

                if key > node.keys[i]:
                    i += 1

            self.insert_non_full(node.children[i], key)

    def split_child(self, parent, index):

        full_child = parent.children[index]

        new_child = BTreeNode(full_child.leaf)

        mid = self.max_keys // 2

        promoted_key = full_child.keys[mid]

        new_child.keys = full_child.keys[mid + 1:]

        full_child.keys = full_child.keys[:mid]

        if not full_child.leaf:

            new_child.children = full_child.children[mid + 1:]

            full_child.children = full_child.children[:mid + 1]

        parent.children.insert(index + 1, new_child)

        parent.keys.insert(index, promoted_key)

    def delete(self, key):

        self.delete_internal(self.root, key)

        if len(self.root.keys) == 0 and not self.root.leaf:
            self.root = self.root.children[0]

    def delete_internal(self, node, key):

        idx = self.find_key(node, key)

        if idx < len(node.keys) and node.keys[idx] == key:

            if node.leaf:
                node.keys.pop(idx)

            else:
                self.delete_internal_node(node, key, idx)

        else:

            if node.leaf:
                print("La clave no existe.")
                return

            flag = idx == len(node.keys)

            if len(node.children[idx].keys) <= self.min_keys:
                self.fill(node, idx)

            if flag and idx > len(node.keys):
                self.delete_internal(node.children[idx - 1], key)
            else:
                self.delete_internal(node.children[idx], key)

    def delete_internal_node(self, node, key, idx):

        left_child = node.children[idx]
        right_child = node.children[idx + 1]

        if len(left_child.keys) > self.min_keys:

            predecessor = self.get_predecessor(left_child)

            node.keys[idx] = predecessor

            self.delete_internal(left_child, predecessor)

        elif len(right_child.keys) > self.min_keys:

            successor = self.get_successor(right_child)

            node.keys[idx] = successor

            self.delete_internal(right_child, successor)

        else:

            self.merge(node, idx)

            self.delete_internal(left_child, key)

    def get_predecessor(self, node):

        current = node

        while not current.leaf:
            current = current.children[-1]

        return current.keys[-1]

    def get_successor(self, node):

        current = node

        while not current.leaf:
            current = current.children[0]

        return current.keys[0]

    def fill(self, node, idx):

        if idx != 0 and len(node.children[idx - 1].keys) > self.min_keys:

            self.borrow_from_prev(node, idx)

        elif idx != len(node.children) - 1 and len(node.children[idx + 1].keys) > self.min_keys:

            self.borrow_from_next(node, idx)

        else:

            if idx != len(node.children) - 1:
                self.merge(node, idx)
            else:
                self.merge(node, idx - 1)

    def borrow_from_prev(self, node, idx):

        child = node.children[idx]

        sibling = node.children[idx - 1]

        child.keys.insert(0, node.keys[idx - 1])

        node.keys[idx - 1] = sibling.keys.pop()

        if not child.leaf:
            child.children.insert(0, sibling.children.pop())

    def borrow_from_next(self, node, idx):

        child = node.children[idx]

        sibling = node.children[idx + 1]

        child.keys.append(node.keys[idx])

        node.keys[idx] = sibling.keys.pop(0)

        if not child.leaf:
            child.children.append(sibling.children.pop(0))

    def merge(self, node, idx):

        child = node.children[idx]

        sibling = node.children[idx + 1]

        child.keys.append(node.keys[idx])

        child.keys.extend(sibling.keys)

        if not child.leaf:
            child.children.extend(sibling.children)

        node.keys.pop(idx)

        node.children.pop(idx + 1)

    def find_key(self, node, key):

        idx = 0

        while idx < len(node.keys) and node.keys[idx] < key:
            idx += 1

        return idx

    def count_keys(self, node=None):

        if node is None:
            node = self.root

        total = len(node.keys)

        for child in node.children:
            total += self.count_keys(child)

        return total

    def load_csv(self, filename):

        try:

            with open(filename, newline='', encoding='utf-8') as file:

                reader = csv.reader(file)

                for row in reader:

                    for value in row:

                        try:
                            number = int(value.strip())

                            self.insert(number)

                        except:
                            pass

            print("Datos cargados correctamente.")

        except FileNotFoundError:
            print("Archivo no encontrado.")

    def graph(self, output_name="arbol_b", highlight_key=None):

        dot = Digraph()

        dot.attr(rankdir='TB')

        dot.attr(splines='polyline')

        dot.attr(size='35,60')

        dot.attr(ratio='compress')

        dot.attr(nodesep='0.15')
        dot.attr(ranksep='2.0')

        dot.attr(dpi='300')

        total_keys = self.count_keys()

        if total_keys > 100:
            dot.attr(nodesep='0.10')
            dot.attr(ranksep='2.0')

        if total_keys > 300:
            dot.attr(nodesep='0.05')
            dot.attr(ranksep='3.0')

        if total_keys > 500:
            dot.attr(nodesep='0.02')
            dot.attr(ranksep='4.0')

        self._graph_node(dot, self.root, highlight_key)

        dot.render(output_name, format='png', cleanup=True)

        print(f"Imagen generada: {output_name}.png")

    def _graph_node(self, dot, node, highlight_key=None, parent_id=None):

        node_id = str(id(node))

        label = " | ".join(str(k) for k in node.keys)

        if highlight_key in node.keys:

            dot.node(
                node_id,
                label,
                shape='record',
                style='filled',
                fillcolor='lightgreen'
            )

        else:

            dot.node(
                node_id,
                label,
                shape='record'
            )

        if parent_id:
            dot.edge(parent_id, node_id)

        for child in node.children:
            self._graph_node(dot, child, highlight_key, node_id)


def menu():

    print("\n========== ÁRBOL B ==========")
    print("1. Insertar claves")
    print("2. Buscar clave")
    print("3. Eliminar clave")
    print("4. Cargar archivo CSV")
    print("5. Generar gráfico")
    print("6. Salir")


grado = int(input("Ingrese el grado del Árbol B: "))

btree = BTree(grado)

while True:

    menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        entrada = input(
            "Ingrese las claves separadas por comas:\n"
        )

        try:

            claves = [int(x.strip()) for x in entrada.split(",")]

            for clave in claves:
                btree.insert(clave)

            print("Claves insertadas correctamente.")

        except:
            print("Error al ingresar las claves.")

    elif opcion == "2":

        clave = int(input("Ingrese la clave a buscar: "))

        result = btree.search(clave)

        if result:

            print("Clave encontrada.")

            nombre = f"busqueda_{clave}"

            btree.graph(nombre, highlight_key=clave)

        else:
            print("Clave NO encontrada.")

    elif opcion == "3":

        clave = int(input("Ingrese la clave a eliminar: "))

        btree.delete(clave)

        print("Proceso completado.")

    elif opcion == "4":

        archivo = input("Ingrese el nombre del archivo CSV: ")

        btree.load_csv(archivo)

    elif opcion == "5":

        nombre = input("Nombre de salida para la imagen: ")

        btree.graph(nombre)

    elif opcion == "6":

        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida.")