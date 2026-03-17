# TAREA 2 - PROGRAMACIÓN III

Este programa utiliza funciones recursivas para realizar diferentes operaciones matemáticas. La recursividad es una técnica en la que una función se llama a sí misma hasta llegar a un caso base, permitiendo resolver problemas.

Las funciones implementadas son:

convertir_a_binario(n): Convierte un número decimal a binario dividiéndolo entre 2 recursivamente hasta llegar al caso base, y luego construye el resultado con los residuos.

contar_digitos(n): Cuenta la cantidad de dígitos de un número dividiéndolo entre 10 en cada llamada recursiva hasta que el número sea menor que 10.

raiz_cuadrada_entera(n): Calcula la raíz cuadrada entera de un número usando una función auxiliar que prueba candidatos desde 0 hasta encontrar el valor correcto.

convertir_a_decimal(romano): Convierte un número romano a decimal comparando el valor de los símbolos. Si un símbolo es menor que el siguiente, se resta; de lo contrario, se suma.
Nota: Esta función no aplica la restricción tradicional de los números romanos que limita el uso de un mismo símbolo a un máximo de tres veces consecutivas (por ejemplo, III es válido para 3, pero IIII normalmente no se usa para 4). 

suma_numeros_enteros(n): Calcula la suma de todos los números desde n hasta 0.

El programa incluye un menú interactivo que permite al usuario seleccionar la operación que desea realizar y mostrar el resultado correspondiente.