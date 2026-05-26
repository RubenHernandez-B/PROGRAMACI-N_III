from graphviz import Digraph


def generar_grafo_partida(id_partida, movimientos):

    dot = Digraph(comment=f"Partida {id_partida}")

    for i, movimiento in enumerate(movimientos):

        jugador, posicion = movimiento

        dot.node(str(i), f"{jugador} -> {posicion}")

        if i > 0:
            dot.edge(str(i - 1), str(i))

    dot.render(f"grafos/partida_{id_partida}", format="png", cleanup=True)

    print(f"Grafo generado: partida_{id_partida}.png")