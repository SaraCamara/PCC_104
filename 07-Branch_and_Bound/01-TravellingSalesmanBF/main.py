def generate_permutations(nums):
    permutations = [[]]
    for num in nums:
        new_permutations = []
        for permutation in permutations:
            for i in range(len(permutation) + 1):
                new_permutations.append(permutation[:i] + [num] + permutation[i:])
        permutations = new_permutations
    return permutations

def calculate_path_cost(path, graph):
    cost = 0
    for i in range(len(path) - 1):
        node = path[i]
        next_node = path[i + 1]
        edge_weight = None
        if next_node in graph[node]:
            edge_weight = graph[node][next_node]
        if edge_weight is None:
            return None
        cost += edge_weight
    return cost

def traveling_salesman_BF(graph):
    nodes = list(graph.keys())
    permutations = generate_permutations(nodes[1:])  # Exclude the first node from permutations

    min_cost = float('inf')
    min_path = None

    for path in permutations:
        path = [nodes[0]] + path  # Prepend the start node to the path
        path.append(nodes[0])  # Append the start node to the end of the path
        cost = calculate_path_cost(path, graph)
        if cost is not None and cost < min_cost:
            min_cost = cost
            min_path = path

    return min_path, min_cost

# Example usage with the corrected graph
graph = {
    1: {2: 2, 3: 1, 4: 2, 5: 2},
    2: {1: 2, 3: 2, 4: 2, 5: 3},
    3: {1: 1, 2: 2, 4: 1, 5: 2},
    4: {1: 2, 2: 2, 3: 1, 5: 1},
    5: {1: 2, 2: 3, 3: 2, 4: 1}
}


min_path, min_cost = traveling_salesman_BF(graph)
print("Custo mínimo:", min_cost)
print("Caminho:", min_path)