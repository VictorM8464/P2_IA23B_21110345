from collections import defaultdict

class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)

    def agregar_arista(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)  # En un grafo no dirigido, las aristas van en ambas direcciones

    def busqueda_en_amplitud(self, nodo_inicial):
        visitados = set()
        cola = [nodo_inicial]

        while cola:
            nodo_actual = cola.pop(0)
            if nodo_actual not in visitados:
                print(nodo_actual, end=' ')
                visitados.add(nodo_actual)
                for vecino in self.grafo[nodo_actual]:
                    if vecino not in visitados:
                        cola.append(vecino)

    def busqueda_en_profundidad(self, nodo_actual, visitados):
        visitados.add(nodo_actual)
        print(nodo_actual, end=' ')

        for vecino in self.grafo[nodo_actual]:
            if vecino not in visitados:
                self.busqueda_en_profundidad(vecino, visitados)

# Ejemplo de uso
grafo = Grafo()
grafo.agregar_arista(0, 1)
grafo.agregar_arista(0, 2)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(2, 0)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(3, 3)

print("Recorrido BFS (Búsqueda en Amplitud) a partir del nodo 2:")
grafo.busqueda_en_amplitud(2)

print("\nRecorrido DFS (Búsqueda en Profundidad) a partir del nodo 2:")
visitados_dfs = set()
grafo.busqueda_en_profundidad(2, visitados_dfs)
