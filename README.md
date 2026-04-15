### Opciones del menú

1. Insertar  
Permite agregar uno o varios números al árbol AVL.

Formatos válidos:
- Un solo número: 50  
- Números separados por comas: 50,30,70  
- Números separados por espacios: 50 30 70  


2. Buscar  
Permite buscar un valor dentro del árbol.

- Si el valor existe:
  - Se muestra un mensaje indicando que fue encontrado.
  - Se genera una imagen con el nodo encontrado.

- Si el valor no existe:
  - Se muestra el mensaje "No encontrado".

3. Eliminar  
Permite eliminar un valor del árbol.

- El árbol se reestructura automáticamente para mantener el balance (propiedad AVL).


4. Cargar desde CSV  
Permite cargar múltiples valores desde un archivo CSV.

- Si el archivo está en la misma carpeta del proyecto, se puede ingresar solo el nombre:
  ejemplo1.csv

- También se puede ingresar la ruta completa del archivo.


5. Visualizar con Graphviz  
Genera una representación gráfica del árbol AVL.

- Se crea una imagen del árbol completo.
- La imagen se abre automáticamente.



6. Salir  
Finaliza la ejecución del programa.

---

### Consideraciones

- Solo se permiten números enteros.
- El árbol se mantiene balanceado automáticamente mediante rotaciones.
- Las imágenes generadas se guardan en la carpeta del proyecto.