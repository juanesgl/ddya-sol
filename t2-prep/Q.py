from sys import stdin as sd

"""
Especificación: 

- Entrada: 
  Un número entero positivo tal que 1 <= N <= 1000. 
  Una secuencia o lista de números enteros 
  P =[a1,a2,a3...aN] de longitud N, la cual es una
  permutación del conjunto {1,2,3...N} 

- Salida  
  Un valor booleano (True o False) que determina si 
  la secuencia ordenada de forma ascendente puede 
  transformarse en la permutación P, mediante 
  una secuencia de operaciones de inserción y extracción 
  sobre una única estructura de tipo Stack (LIFO).

Diseño

- El problema se resuelve mediante una simulación que emplea 
  una estructura de almacenamiento temporal con restricciones 
  de acceso de tipo LIFO.

- La solución debe resolver lo siguiente: 

  1. Ingreso secuencial: Los elementos de la secuencia de origen ingresan uno a uno al almacenamiento temporal.

  2. Tras cada ingreso, si el elemento disponible en el tope coincide con el requerido por la salida objetivo, 
     se retira de inmediato hacia su destino.

  3. Validación final: Al terminar de procesar todos los elementos, si el almacenamiento queda completamente vacío, 
     la secuencia es factible; de lo contrario, se descarta porque algunos elementos quedaron bloqueados.

Complejidad Temporal y Espacial: 

- Temporal: O(n) 
  Cada elemento de la secuencia ingresa a la estructura temporal exactamente una vez y es extraído a lo sumo una vez.

- Espacial: O(n) 
  En el peor de los casos, la estructura temporal almacena simultáneamente todos los elementos de la secuencia.

"""


def solve(n: int, wagons: list[int]) -> bool:
    stack = []
    idx = 0
    for x in range(1, n + 1):
        stack.append(x)
        while len(stack) > 0 and stack[-1] == wagons[idx]:
            stack.pop()
            idx += 1

    return len(stack) == 0


def main(sd):

    n = int(sd.readline().strip())

    while n != 0:
        wagons = [int(i) for i in sd.readline().strip().split()]
        while len(wagons) == n:
            ans = solve(n, wagons)
            if ans:
                print("Yes")
            else:
                print("No")
            wagons = [int(i) for i in sd.readline().strip().split()]

        print()
        n = int(sd.readline().strip())


main(sd)
