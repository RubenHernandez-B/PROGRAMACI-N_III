# MANUAL DE USUARIO
Este programa implementa una *lista doblemente enlazada* para almacenar información de personas (nombre, apellido y carnet) y permite:

* Insertar nodos al *inicio* o al *final* de la lista.
* Eliminar nodos por número de carnet.
* Visualizar la lista completa en consola.
* Generar gráficas en PNG de la lista para ver su estructura.

Cada nodo contiene:

* nombre: Nombre de la persona.
* apellido: Apellido de la persona.
* carnet: Identificador único.
* siguiente: Apunta al siguiente nodo de la lista.
* anterior: Apunta al nodo anterior de la lista.

* Requisitos Previos *

1. Tener instalado Python 3.
2. Tener instalado Graphviz para generar gráficos.

* Uso del Programa *

Al ejecutar el programa, se mostrará un menú interactivo:

--- MENÚ ---
1. Insertar al principio
2. Insertar al final
3. Eliminar por carnet
4. Mostrar lista
5. Salir

1. Insertar al Principio

* Selecciona `1`.
* Ingresa `Nombre`, `Apellido` y `Carnet`.
* El nodo se agregará al inicio de la lista.
* Se generará automáticamente una gráfica PNG mostrando la nueva estructura.

2. Insertar al Final

* Selecciona `2`.
* Ingresa `Nombre`, `Apellido` y `Carnet`.
* El nodo se agregará al final de la lista.
* Se generará automáticamente una gráfica PNG mostrando la nueva estructura.

3. Eliminar por Carnet

* Selecciona `3`.
* Ingresa el número de `Carnet` que deseas eliminar.
* El nodo correspondiente será eliminado de la lista, con actualización de la estructura.
* Se generará automáticamente una gráfica PNG de la lista después de la eliminación.
* Si el carnet no existe, mostrará `CARNET NO ENCONTRADO.`

4. Mostrar Lista

* Selecciona `4`.
* La lista se mostrará en consola en el formato:

```
None <- Nombre Apellido (Carnet) <-> Nombre Apellido (Carnet) -> None
```

* `None` indica los extremos de la lista.
* `<->` indica la doble conexión entre nodos.

5. Salir

* Selecciona `5` para cerrar el programa.

Generación de Gráficas

* Cada operación de inserción o eliminación genera un archivo `.png` de la lista.
* Los archivos se nombran según la operación y un contador:

  * Ejemplo: `insertar_inicio_0.png`, `eliminar_1.png`.
* Estas gráficas permiten visualizar **la conexión de cada nodo** de forma clara.


Ejemplo

1. Inserta al inicio: Juan Pérez (2026001)
2. Inserta al final: Ana López (2026002)
3. Mostrar lista → `None <- Juan Pérez (2026001) <-> Ana López (2026002) -> None`
4. Eliminar por carnet: 2026001
5. Mostrar lista → `None <- Ana López (2026002) -> None`

 
