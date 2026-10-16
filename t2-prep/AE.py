from sys import stdin as sd


"""
Especificación: 

- Entrada: 
 Dos secuencias de números enteros positivos distintos, I y P, de longitud N 
 donde cada valor. 
 I representa el recorrido en inorden (inorder) y P representa el recorrido 
 en posorden (postorder) de un mismo árbol binario.

- Salida: 
  Un número entero que corresponde al valor de la hoja terminal del camino 
  desde la raíz cuya suma de nodos sea mínima. En caso de existir múltiples 
  caminos con la misma suma mínima, se selecciona la hoja con el menor 
  valor individual.

Diseño:

- En un recorrido en posorden, el último elemento representa la raíz del árbol 
  o subárbol actual.

- La posición de la raíz dentro del recorrido en inorden divide los elementos 
  en dos segmentos: los que están a su izquierda pertenecen al subárbol izquierdo 
  y los de su derecha al subárbol derecho.

- Se reconstruye recursivamente la estructura jerárquica del árbol binario enlazando 
  cada raíz con sus respectivos subárboles izquierdo y derecho a partir de estas divisiones.

- Se evalúan recursivamente los caminos desde la raíz acumulando la suma de los valores 
  hasta alcanzar las hojas (nodos sin hijos).

- Al llegar a cada hoja, se compara la suma acumulada contra el mínimo global encontrado, 
  actualizando el valor de la hoja seleccionada y aplicando el valor numérico menor como 
  criterio de desempate.

Complejidad Temporal y Espacial: 

- Temporal: O(N^2) con búsqueda secuencial y cortes de lista (o O(N) si se indexa con diccionario).

- Espacial: O(N) para el almacenamiento de los nodos en memoria y la pila de recursión del árbol.

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree(inorder, postorder):
    if not inorder:
        return None

    root_v = postorder[-1]
    root = Node(root_v)

    idx = inorder.index(root_v)

    root.left = build_tree(inorder[:idx], postorder[:idx])
    root.right = build_tree(inorder[idx + 1:], postorder[idx:-1])

    return root


min_sum = float("inf")
best_leaf = float("inf")


def check_path(node, curr_sum):
    global min_sum, best_leaf

    if node is None:
        return

    curr_sum += node.val

    if node.left is None and node.right is None:
        if curr_sum < min_sum:
            min_sum = curr_sum
            best_leaf = node.val
        elif curr_sum == min_sum and node.val < best_leaf:
            best_leaf = node.val
        return

    check_path(node.left, curr_sum)
    check_path(node.right, curr_sum)


def main(sd):
    global min_sum, best_leaf

    lines = sd.read().splitlines()
    i = 0

    while i < len(lines):
        if not lines[i].strip():
            i += 1
            continue

        inorder = list(map(int, lines[i].split()))
        postorder = list(map(int, lines[i + 1].split()))
        i += 2  

        min_sum = float("inf")
        best_leaf = float("inf")

        tree = build_tree(inorder, postorder)
        check_path(tree, 0)
        print(best_leaf)

main(sd)