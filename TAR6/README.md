# Árbol B en Python

Proyecto desarrollado en Python que implementa la estructura de datos Árbol B, permitiendo realizar operaciones fundamentales como inserción, búsqueda, eliminación de claves, carga de datos desde archivos CSV y generación gráfica del árbol.

El programa funciona mediante un menú interactivo en consola y permite configurar el grado del Árbol B al iniciar la ejecución.

Funcionalidades
1. Inserción de claves

Permite ingresar múltiples claves separadas por comas para agregarlas al Árbol B.

Ejemplo:

10,20,30,40,50

El árbol realiza automáticamente divisiones de nodos cuando se alcanza el límite permitido según el grado configurado.

2. Búsqueda de claves

Permite buscar una clave dentro del árbol.

Si la clave existe:

El programa indica que fue encontrada.
Se genera automáticamente una imagen PNG del árbol.
La clave encontrada aparece resaltada junto con el bloque completo de claves en color verde.

Si la clave no existe:

El programa muestra un mensaje indicando que no fue encontrada.
3. Eliminación de claves

Permite eliminar claves existentes dentro del Árbol B.

El programa maneja automáticamente:

Reorganización de nodos.
Redistribución de claves.
Fusiones entre nodos.
Sustitución por predecesores o sucesores.

4. Carga de archivos CSV

El sistema puede cargar claves numéricas desde archivos CSV.

Ejemplo:

10,20,30
40,50,60
70,80,90

Todas las claves válidas son insertadas automáticamente en el árbol.

5. Generación gráfica del Árbol B

El programa utiliza Graphviz para generar representaciones visuales del árbol en formato PNG.

Características:

Ajuste automático del tamaño del gráfico.
Organización jerárquica de nodos.
Compatibilidad con árboles grandes.