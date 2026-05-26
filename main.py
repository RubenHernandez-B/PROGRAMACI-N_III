from juego import JuegoTotito
from aprendizaje import Entrenamiento
from arbol_b import ArbolB
from arbol_binario import ArbolBinario

def mostrar_menu():
    print(" ===== TOTITO =====")
    print("1. Jugar manualmente")
    print("2. Jugar contra la IA")
    print("3. Entrenamiento automático")
    print("4. Ver historial")
    print("5. Ver iteraciones")
    print("6. Reiniciar sistema")
    print("7. Salir")


historial = ArbolB(grado=3)
arbol = ArbolBinario()
iteraciones = 0

while True:

    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        juego = JuegoTotito(historial)
        juego.jugar_manual()

    elif opcion == "2":
        juego = JuegoTotito(historial, arbol)
        juego.jugar_ia()

    elif opcion == "3":

        cantidad = int(input("Cantidad de partidas a simular: "))

        entrenamiento = Entrenamiento(historial, arbol)
        entrenamiento.simular(cantidad)

        iteraciones += cantidad

    elif opcion == "4":
        historial.mostrar()

    elif opcion == "5":
        print(f"Iteraciones realizadas: {iteraciones}")

    elif opcion == "6":
        historial = ArbolB(grado=3)
        arbol = ArbolBinario()
        iteraciones = 0
        print("Sistema reiniciado")

    elif opcion == "7":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")