# Condições:
# grafo genérico
# max_edges_per_node = node - 1
# Não deve ter mais de uma aresta entre nos
# A direção do nó A para o nó B e do nó B para o nó A devem ter o mesmo valor de custo

import random


# Generate a new graph with random edge costs
num_nodes = 5  # Number of nodes (cities)
min_cost = 1   # Minimum cost for an edge
max_cost = 3  # Maximum cost for an edge

graph = {}

# Generate one random edge for each node pair
for node_a in range(1, num_nodes+1):
    for node_b in range(node_a+1, num_nodes+1):
        cost = random.randint(min_cost, max_cost)
        graph.setdefault(node_a, {})[node_b] = cost
        graph.setdefault(node_b, {})[node_a] = cost

print("Generated Graph:")
for node, neighbors in graph.items():
    print(f"{node}: {neighbors}")