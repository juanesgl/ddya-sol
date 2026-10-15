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

- Temporal: 
  

- Espacial: 

"""

class Node:
  def __init__(self, key: Any):
    self.key: Any = key
    self.next: Node | None = None
    self.prev: Node | None = None

  def __repr__(self) -> str:
    return f"Node[{self.key}]"


  def insert_node(z: Node, x: Node):
    assert z is not None
    assert x is not None
    z.next = x.next
    z.prev = x
    if x.next is not None:
        x.next.prev = z
    x.next = z

class LinkedList:
  def __init__(self):
    self.head: Node | None = None

  def prepend(self, key: Any):
    x = Node(key)
    x.next = self.head
    x.prev = None
    if self.head is not None:
      self.head.prev = x
    self.head = x

  def search(self, k: Any) -> Node | None:
    x = self.head
    while x is not None and x.key != k:
      x = x.next
    return x

  def delete(self, x: Node):
    assert x is not None
    if x.prev is not None:
      x.prev.next = x.next
    else:
      self.head = x.next

    if x.next is not None:
      x.next.prev = x.prev

  def __repr__(self) -> str:
    values = []
    x = self.head
    while x is not None:
      values.append(x)
      x = x.next
    return str(values)


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
        Node.insert_node(new_node, cursor) 

        if cursor == tail:
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
        line = line.strip()
        if line: 
           res = solve(line)
           print(res)

main(sd)
