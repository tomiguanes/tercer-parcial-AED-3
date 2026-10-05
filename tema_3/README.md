# Tema 3 - Examen Parcial AED 3

Resolución completa de los ejercicios del Tema 3 correspondientes al examen parcial.

## Resumen de Ejercicios y Soluciones

### Punto 1: Programación Dinámica (`punto_uno.py`)
- **Secuencia:**
  $$s_k = \begin{cases} 1 & \text{si } 1 \le k \le 3 \\ 2s_{k-1} + 3s_{k-2} + 4s_{k-3} & \text{si } k > 3 \end{cases}$$
- **Implementaciones:**
  1. `calcularSk(k)`: Versión Bottom-Up (tabulación) con diccionario `dp`. Valida $k \ge 1$, llena casos base $1..3$ e itera en `range(4, k + 1)`. Complejidad: $O(k)$ tiempo, $O(k)$ espacio.
  2. `calcularSkTopDown(k, memo=None)`: Versión recursiva con memoización y parámetro por defecto `memo=None`.

### Punto 2: Listas Simplemente Enlazadas (`punto_dos.py`)
- **Método:** `SingleLinkedList.eliminarUltimo(self)`
- **Casos contemplados:**
  - Lista vacía (`not self.head`): no hace nada ("en caso de existir").
  - Un solo nodo (`self.head == self.tail`): desconecta `head` y `tail` a `None`.
  - Dos o más nodos: avanza con `while curr.next is not self.tail:`, desconecta el último nodo, actualiza `self.tail = curr` y decrementa `self.size`.

### Punto 3: Listas Doblemente Enlazadas (`punto_tres.py`)
- **Método:** `DoubleLinkedList.insertarElemento(self, x, i)`
- **Casos contemplados:**
  - Validación del índice: `0 <= i <= self.size`.
  - Inserción en cabeza ($i = 0$): actualiza `self.head.prev = new` (si existe) y `self.head = new`.
  - Inserción en el medio o final ($i > 0$): itera $i-1$ veces, enlaza `new.next = curr.next`, `new.prev = curr`, y si `curr.next` existe actualiza `curr.next.prev = new`. Finalmente `curr.next = new`.
  - Mantiene actualizado `self.size += 1`.

### Punto 4: Stacks y Node con Lista Doblemente Enlazada (`punto_cuatro.py`)
- **Clases:**
  - `Node`:
    - `validar(self, f)`: aplica `f(self.data)`. Si es `False`, desvincula simétricamente `self.prev.next = self.next` (si tiene anterior) y `self.next.prev = self.prev` (si tiene siguiente), y aísla el nodo fijando sus punteros en `None`.
  - `Stack`:
    - `__init__(self)`: inicializa `self.head = None` y `self.size = 0`.
    - `push(self, x)`: maneja enlace doble (`new.next = self.head` y `self.head.prev = new` si `self.head` existía).
    - `pop(self)`: extrae el valor del tope, avanza `self.head`, limpia `self.head.prev = None` si la lista no quedó vacía, decrementa `self.size` y devuelve el dato.
