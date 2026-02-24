def convertir_a_binario(n):
    if n < 2:
        return str(n)
    return convertir_a_binario(n // 2) + str(n % 2)

def contar_digitos(n):
    n = abs(n)
    if n < 10:
        return 1
    return 1 + contar_digitos(n // 10)


def calcular_raiz_cuadrada(n, candidato):
    if candidato * candidato > n:
        return candidato - 1
    return calcular_raiz_cuadrada(n, candidato + 1)


def raiz_cuadrada_entera(n):
    if n < 0:
        return None
    return calcular_raiz_cuadrada(n, 0)


def convertir_a_decimal(romano):
    valores = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    if len(romano) == 0:
        return 0

    if len(romano) == 1:
        return valores[romano]

    if valores[romano[0]] < valores[romano[1]]:
        return valores[romano[1]] - valores[romano[0]] + convertir_a_decimal(romano[2:])
    else:
        return valores[romano[0]] + convertir_a_decimal(romano[1:])


def suma_numeros_enteros(n):
    if n == 0:
        return 0
    return n + suma_numeros_enteros(n - 1)


def menu():
    while True:
        print("\n---MENU--")
        print("1. Convertir a Binario")
        print("2. Contar Dígitos")
        print("3. Raíz Cuadrada Entera")
        print("4. Convertir a Decimal desde Romano")
        print("5. Suma de Números Enteros")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero = int(input("Ingrese un número entero: "))
            print("Binario:", convertir_a_binario(numero))

        elif opcion == "2":
            numero = int(input("Ingrese un número entero: "))
            print("Cantidad de dígitos:", contar_digitos(numero))

        elif opcion == "3":
            numero = int(input("Ingrese un número entero: "))
            resultado = raiz_cuadrada_entera(numero)
            print("Raíz cuadrada entera:", resultado)

        elif opcion == "4":
            romano = input("Ingrese un número romano: ").upper()
            print("Decimal:", convertir_a_decimal(romano))

        elif opcion == "5":
            numero = int(input("Ingrese un número entero positivo: "))
            print("Suma:", suma_numeros_enteros(numero))

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción inválida")


menu()