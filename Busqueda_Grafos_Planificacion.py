import heapq

# Definición de una clase para representar nodos del grafo
class Nodo:
    def __init__(self, estado, padre, costo_g, costo_h):
        self.estado = estado  # El estado actual del nodo
        self.padre = padre    # El nodo padre
        self.costo_g = costo_g  # Costo acumulado desde el nodo inicial
        self.costo_h = costo_h  # Heurística (costo estimado al objetivo)

    def __lt__(self, otro):
        return (self.costo_g + self.costo_h) < (otro.costo_g + otro.costo_h)

# Función de búsqueda A*
def busqueda_a_estrella(grafo, estado_inicial, estado_objetivo):
    # Crear el nodo inicial y lo agregamos a la lista abierta
    nodo_inicial = Nodo(estado_inicial, None, 0, 0)
    lista_abierta = [nodo_inicial]
    lista_cerrada = set()

    while lista_abierta:
        # Seleccionar el nodo con el menor costo f de la lista abierta
        nodo_actual = heapq.heappop(lista_abierta)

        if nodo_actual.estado == estado_objetivo:
            # Hemos encontrado el camino
            camino = []
            while nodo_actual:
                camino.append(nodo_actual.estado)
                nodo_actual = nodo_actual.padre
            return list(reversed(camino))

        lista_cerrada.add(nodo_actual.estado)

        for vecino, costo in grafo[nodo_actual.estado].items():
            if vecino not in lista_cerrada:
                costo_g = nodo_actual.costo_g + costo
                costo_h = heuristica(vecino, estado_objetivo)
                nuevo_nodo = Nodo(vecino, nodo_actual, costo_g, costo_h)
                heapq.heappush(lista_abierta, nuevo_nodo)

    return None  # No se encontró un camino

# Función de heurística (en este caso, distancia euclidiana)
def heuristica(estado, estado_objetivo):
    x1, y1 = estado
    x2, y2 = estado_objetivo
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Grafo de ejemplo (representado como un diccionario)
grafo = {
    (0, 0): {(0, 1): 1, (1, 0): 1},
    (0, 1): {(0, 0): 1, (1, 1): 1},
    (1, 0): {(0, 0): 1, (1, 1): 1},
    (1, 1): {(0, 1): 1, (1, 0): 1}
}

estado_inicial = (0, 0)
estado_objetivo = (1, 1)

camino = busqueda_a_estrella(grafo, estado_inicial, estado_objetivo)

if camino:
    print("Camino encontrado:", camino)
else:
    print("No se encontró un camino.")

