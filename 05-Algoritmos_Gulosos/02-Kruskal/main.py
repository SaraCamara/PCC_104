# Implementação do algoritmo Kruskal para a obter a árvore geradora mínima.
# Entrada: Um gráfico conectado ponderado G = {V, E}
# Saída: E_T, o conjunto de arestas que compõem uma árvore geradora mínima de G
# ordenar E em ordem não decrescente dos pesos das arestas.

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {}
        self.rank = {}
        for v in vertices:
            self.parent[v] = v
            self.rank[v] = 0

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                self.rank[root2] += 1


def kruskals(graph):
    edges = []
    for v in graph:
        for u, weight in graph[v]:
            edges.append((weight, v, u))
    edges.sort()

    mst = []
    disjoint_set = DisjointSet(graph.keys())

    for weight, v, u in edges:
        if disjoint_set.find(v) != disjoint_set.find(u):
            mst.append((v, u, weight))
            disjoint_set.union(v, u)

    return mst


# Example usage
graph2 = {
    'A': [('B', 3), ('D', 8), ('E', 9), ('C', 5)],
    'B': [('A', 3), ('D', 2)],
    'C': [('A', 5), ('E', 2), ('D', 8)],
    'D': [('B', 2), ('A', 8), ('E', 1), ('C', 8)],
    'E': [('D', 1), ('A', 9), ('C', 2)]
}

graph = {
    'A': [('B', 1),  ('C', 3)],
    'B': [('A', 1), ('C', 2)],
    'C': [('A', 3), ('B', 2)],
}

mst = kruskals(graph)
print(mst)

