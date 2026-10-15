from collections import deque
from sys import stdin as sd

"""
Especificación: 

- Entrada: 
  Una secuencia de números enteros positivos P = [p1,p2,p3...pN]
  de longitud n, que representan el nivel de prrioridad de un 
  conjunto de elementos ordenados en una estructura de fila. 
  
- Salida  
  Un número entero que representa la cantidad de unidades de tiempo 
  transcurridas hasta que el elemento situado en la posición m 
  completa su procesamiento y sale de la estructura, bajo la regla 
  de que si hay algún elemento con mayor prioridad en la fila, el 
  elemento actual se desplaza al final de la misma. 
  
Diseño

- El código debe seguir lo siguiente: 
  
  - Modelado de la fila: Los elementos se procesan en orden de llegada, 
  permitiendo reubicar elementos al final si no cumplen con la prioridad requerida.

  - Verificación de prioridad: En cada turno se compara el elemento al frente con el 
  resto de elementos restantes para determinar si posee la máxima prioridad disponible.

  - Simulación de turnos: Si existe otro elemento de mayor prioridad, el elemento actual 
  se mueve al final de la fila; de lo contrario, se procesa y se registra el tiempo 
  transcurrido, actualizando el seguimiento de la posición de interés hasta que esta 
  sea atendida.

Complejidad Temporal y Espacial: 

- Temporal: O(n^2)


- Espacial: O(n)

"""


def solve(jobs: list, m: int) -> int:

    queue = deque()
    for i, priority in enumerate(jobs):
        queue.append((priority, i == m))

    ts = 0

    while len(queue) > 0:
        act_prior, is_our = queue.popleft()

        high_pri = False

        for something in queue:
            if something[0] > act_prior:
                high_pri = True
                break

        if high_pri == True:
            queue.append((act_prior, is_our))
        else:
            ts += 1

            if is_our == True:
                return ts


def main(sd):

    n = int(sd.readline())

    for _ in range(n):
        n, m = map(int, sd.readline().split())
        jobs = list(map(int, sd.readline().split()))

        print(solve(jobs, m))


main(sd)
