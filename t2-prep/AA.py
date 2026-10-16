from typing import Any
from sys import stdin as sd

"""
Especificación: 

- Entrada: 
  Una cadena de texto S de longitud L, compuesta por letras, guiones 
  bajos y los caracteres especiales [ (Simula la tecla Home) y 
  ] (Simula la tecla end). 
  
- Salida
  Una cadena de texto resultante que representa el orden final en el 
  que aparecen los caracteres en la pantalla tras simular los saltos 
  de cursor provocados por las teclas especiales. 
  
Diseño

- Se utiliza una secuencia dinámica basada en nodos enlazados junto con 
  un cursor o puntero de posición que indica en qué punto de la estructura
  se insertará el siguiente elemento. 

- Al detectar el comando de inicio ([), el cursor se reubica al principio de 
  la estructura.

- Al detectar el comando de fin (]), el cursor se desplaza al final de la 
  estructura.

- Los caracteres ordinarios se insertan de forma inmediata en la posición 
 señalada por el cursor, avanzando el cursor un paso para preservar el 
 orden relativo del bloque de texto que se esté escribiendo.

- Al finalizar el procesamiento de los caracteres, se recorren los nodos 
  enlazados desde la cabeza hasta el final para generar la cadena resultante.  


Complejidad Temporal y Espacial: 

- Temporal: O(L)
  

- Espacial: O(L)

"""


class Node:
    __slots__ = ("key", "next")
    def __init__(self, key):
        self.key = key
        self.next = None

def solve(s):
    dummy = Node('')
    cursor = dummy
    tail = dummy

    for c in s:
        if c == '[':
            cursor = dummy
        elif c == ']':
            cursor = tail
        else:
            new_node = Node(c)
            new_node.next = cursor.next
            cursor.next = new_node
            if cursor is tail:
                tail = new_node
            cursor = new_node

    ans = []
    curr = dummy.next
    while curr is not None:
        ans.append(curr.key)
        curr = curr.next
    return ''.join(ans)

def main(sd):
    for line in sd:
        line = line.rstrip('\n')
        if line:
            print(solve(line))

main(sd)