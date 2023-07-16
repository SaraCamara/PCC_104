# Implementação do algoritmo Prim para a obter a árvore geradora mínima.
# Entrada: Um gráfico conectado ponderado G = {V, E}
# Saída: E_T, o conjunto de arestas que compõem uma árvore geradora mínima de G.

import heapq


def prim(graph):

    # Initialize a set to keep track of the tree vertices
    visited_v = set()
    start_v = list(graph.keys())[0]  # Start with any vertex

    # Create a heap to store the edges (weight, vertex1, vertex2)
    heap = []
    heapq.heappush(heap, (0, start_v, None))

    # Stores the selected edges of the Minimum Spanning Tree
    mst = []

    while heap:
        weight, current_v, parent_v = heapq.heappop(heap)  # Pop the edge with the minimum weight

        if current_v in visited_v:
            continue

        # Mark the current vertex as a tree vertex
        visited_v.add(current_v)

        if parent_v is not None:
            # Add the selected edge to the Minimum Spanning Tree
            mst.append((weight, parent_v, current_v))

        # Explore the neighbors of the current vertex
        for neighbor, edge_weight in graph[current_v]:
            if neighbor not in visited_v:
                # Add the edge to the heap
                heapq.heappush(heap, (edge_weight, neighbor, current_v))

    return mst


# Example usage
graph = {
    'A': [('B', 3), ('D', 8), ('E', 9), ('C', 5)],
    'B': [('A', 3), ('D', 2)],
    'C': [('A', 5), ('E', 2), ('D', 8)],
    'D': [('B', 2), ('A', 8), ('E', 1), ('C', 8)],
    'E': [('D', 1), ('A', 9), ('C', 2)]
}

print(prim(graph))
