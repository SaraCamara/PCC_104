def traveling_salesman_BB(graph):
    # Initialize the best tour and its cost.
    min_path = None
    min_cost = float('inf')

    # Recursively explore all possible tours.
    def branch_and_bound(path, cost):
        nonlocal min_path, min_cost  # Use nonlocal to modify the outer variables

        if len(path) == len(graph):
            # If the tour is complete, check its cost.
            if cost + graph[path[-1]][path[0]] < min_cost:
                min_path = path + [path[0]]
                min_cost = cost + graph[path[-1]][path[0]]

        for node in graph[path[-1]]:
            if node not in path:
                new_path = path + [node]
                new_cost = cost + graph[path[-1]][node]
                branch_and_bound(new_path, new_cost)

    # Start the recursive search.
    initial_node = list(graph.keys())[0]
    branch_and_bound([initial_node], 0)

    # Return the best tour.
    return min_path, min_cost


# Test the algorithm.
graph = {
    1: {2: 2, 3: 1, 4: 2, 5: 2},
    2: {1: 2, 3: 2, 4: 2, 5: 3},
    3: {1: 1, 2: 2, 4: 1, 5: 2},
    4: {1: 2, 2: 2, 3: 1, 5: 1},
    5: {1: 2, 2: 3, 3: 2, 4: 1}
}


min_path, min_cost = traveling_salesman_BB(graph)
print("Custo mínimo:", min_cost)
print("Caminho:", min_path)